"""Device detection module"""

import subprocess
import re


class DeviceDetector:
    """Detect Logitech RGB devices"""

    # Known Logitech keyboard product IDs
    KEYBOARD_PIDS = {
        'c336': 'G213 Prodigy Gaming Keyboard',
        'c330': 'G410 Atlas Spectrum',
        'c33a': 'G413 Carbon',
        'c342': 'G512 Carbon',
        'c33c': 'G513 Carbon',
        'c333': 'G610 Orion',
        'c337': 'G810 Orion Spectrum',
        'c32b': 'G910 Orion Spark',
        'c339': 'G Pro Keyboard',
    }

    # Known Logitech mouse product IDs
    MOUSE_PIDS = {
        'c092': 'G102/G203 LIGHTSYNC Gaming Mouse',
        'c07e': 'G203 Prodigy',
        'c246': 'G305 LIGHTSPEED',
        'c083': 'G403 Prodigy',
        'c08b': 'G502 HERO',
        'c539': 'G502 X LIGHTSPEED',
        'c545': 'G502 X',
        'c087': 'G604 LIGHTSPEED',
        'c087': 'G703 LIGHTSPEED',
        'c088': 'G Pro Wireless',
    }

    def detect_all(self):
        """Detect all Logitech RGB devices

        Returns:
            tuple: (keyboards, mice) lists of device dicts
        """
        keyboards = []
        mice = []

        try:
            # Run lsusb to get USB devices
            result = subprocess.run(['lsusb'], capture_output=True, text=True)
            lines = result.stdout.strip().split('\\n')

            for line in lines:
                if 'Logitech' not in line:
                    continue

                # Parse USB line
                # Format: Bus XXX Device XXX: ID VVVV:PPPP Vendor Device Name
                match = re.search(r'ID ([0-9a-f]{4}):([0-9a-f]{4})', line)
                if not match:
                    continue

                vid = match.group(1)
                pid = match.group(2)

                # Check if it's a known keyboard
                if pid in self.KEYBOARD_PIDS:
                    keyboards.append({
                        'name': self.KEYBOARD_PIDS[pid],
                        'vid': vid,
                        'pid': pid,
                        'type': 'keyboard'
                    })

                # Check if it's a known mouse
                elif pid in self.MOUSE_PIDS:
                    mice.append({
                        'name': self.MOUSE_PIDS[pid],
                        'vid': vid,
                        'pid': pid,
                        'type': 'mouse'
                    })

        except Exception as e:
            print(f"Error detecting devices: {e}")

        return keyboards, mice

    def check_tool_availability(self):
        """Check if required tools are installed

        Returns:
            dict: Tool availability status
        """
        tools = {}

        # Check for g810-led
        try:
            subprocess.run(['which', 'g213-led'],
                         capture_output=True, check=True)
            tools['g810-led'] = True
        except subprocess.CalledProcessError:
            tools['g810-led'] = False

        # Check for ratbagctl
        try:
            subprocess.run(['which', 'ratbagctl'],
                         capture_output=True, check=True)
            tools['ratbagctl'] = True
        except subprocess.CalledProcessError:
            tools['ratbagctl'] = False

        return tools
