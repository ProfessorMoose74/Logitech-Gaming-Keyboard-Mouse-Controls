"""Systemd service management"""

import subprocess
import os


class SystemdManager:
    """Manage systemd services for persistent RGB lighting"""

    def __init__(self):
        self.service_dir = '/etc/systemd/system'
        self.script_dir = '/usr/local/bin'

    def create_services(self, keyboards, mice, color, effect=None, speed=None):
        """Create systemd services for all devices

        Args:
            keyboards (list): List of keyboard devices
            mice (list): List of mouse devices
            color (str): Hex color code
            effect (str): Effect name (optional)
            speed (str): Effect speed (optional)
        """
        from ..devices.keyboard import KeyboardController
        from ..devices.mouse import MouseController

        # Create keyboard services
        for kb in keyboards:
            kb_controller = KeyboardController(kb)
            script_content = kb_controller.get_script_content(color, effect, speed)

            script_name = f"logilight-kb-{kb['pid']}.sh"
            service_name = f"logilight-kb-{kb['pid']}.service"

            self._create_script(script_name, script_content)
            self._create_service(service_name, script_name, "Keyboard")

        # Create mouse services
        for mouse in mice:
            mouse_controller = MouseController(mouse)
            script_content = mouse_controller.get_script_content(color, effect)

            script_name = f"logilight-mouse-{mouse['pid']}.sh"
            service_name = f"logilight-mouse-{mouse['pid']}.service"

            self._create_script(script_name, script_content)
            self._create_service(service_name, script_name, "Mouse", needs_ratbagd=True)

    def _create_script(self, filename, content):
        """Create a shell script

        Args:
            filename (str): Script filename
            content (str): Script content
        """
        script_path = os.path.join(self.script_dir, filename)

        try:
            # Write script
            with open(f'/tmp/{filename}', 'w') as f:
                f.write(content)

            # Copy to system location and set permissions
            subprocess.run(['sudo', 'cp', f'/tmp/{filename}', script_path], check=True)
            subprocess.run(['sudo', 'chmod', '+x', script_path], check=True)

            # Fix line endings if needed
            subprocess.run(['sudo', 'sed', '-i', 's/\\r$//', script_path], check=True)

        except Exception as e:
            print(f"Error creating script: {e}")

    def _create_service(self, service_name, script_name, device_type, needs_ratbagd=False):
        """Create a systemd service

        Args:
            service_name (str): Service filename
            script_name (str): Script filename
            device_type (str): Device type (Keyboard or Mouse)
            needs_ratbagd (bool): Whether service needs ratbagd
        """
        script_path = os.path.join(self.script_dir, script_name)

        service_content = f"""[Unit]
Description=LogiLight {device_type} RGB Lighting
After=multi-user.target
"""

        if needs_ratbagd:
            service_content += "After=ratbagd.service\\nWants=ratbagd.service\\n"

        service_content += f"""
[Service]
Type=oneshot
ExecStart={script_path}
RemainAfterExit=yes
"""

        if needs_ratbagd:
            # Run as user for ratbagctl
            user = os.getenv('SUDO_USER', os.getenv('USER', 'root'))
            service_content += f"""User={user}
Group={user}
SupplementaryGroups=input games
"""

        service_content += """
[Install]
WantedBy=multi-user.target
"""

        service_path = os.path.join(self.service_dir, service_name)

        try:
            # Write service file
            with open(f'/tmp/{service_name}', 'w') as f:
                f.write(service_content)

            # Copy to system location
            subprocess.run(['sudo', 'cp', f'/tmp/{service_name}', service_path], check=True)

            # Reload systemd and enable service
            subprocess.run(['sudo', 'systemctl', 'daemon-reload'], check=True)
            subprocess.run(['sudo', 'systemctl', 'enable', service_name], check=True)

        except Exception as e:
            print(f"Error creating service: {e}")

    def remove_services(self):
        """Remove all LogiLight systemd services"""
        try:
            # Find all logilight services
            result = subprocess.run(
                ['sudo', 'systemctl', 'list-unit-files', 'logilight-*'],
                capture_output=True,
                text=True
            )

            for line in result.stdout.split('\\n'):
                if 'logilight-' in line:
                    service_name = line.split()[0]

                    # Disable and remove service
                    subprocess.run(['sudo', 'systemctl', 'disable', service_name],
                                 capture_output=True)
                    subprocess.run(['sudo', 'systemctl', 'stop', service_name],
                                 capture_output=True)

                    service_path = os.path.join(self.service_dir, service_name)
                    subprocess.run(['sudo', 'rm', '-f', service_path],
                                 capture_output=True)

            # Reload systemd
            subprocess.run(['sudo', 'systemctl', 'daemon-reload'], check=True)

        except Exception as e:
            print(f"Error removing services: {e}")

    def check_status(self):
        """Check status of LogiLight services

        Returns:
            dict: Service name -> active status
        """
        status = {}

        try:
            result = subprocess.run(
                ['systemctl', 'list-units', 'logilight-*', '--no-legend'],
                capture_output=True,
                text=True
            )

            for line in result.stdout.split('\\n'):
                if 'logilight-' in line:
                    parts = line.split()
                    if len(parts) >= 4:
                        service_name = parts[0]
                        active = parts[3] == 'active'
                        status[service_name] = active

        except Exception as e:
            print(f"Error checking status: {e}")

        return status
