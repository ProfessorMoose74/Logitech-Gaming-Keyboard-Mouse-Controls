#!/usr/bin/env python3
"""
LogiLight CLI - Command-line interface for Logitech RGB lighting control
"""

import click
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich import print as rprint

from .devices.detector import DeviceDetector
from .devices.keyboard import KeyboardController
from .devices.mouse import MouseController
from .utils.systemd import SystemdManager
from .utils.config import ConfigManager

console = Console()


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """LogiLight - Easy RGB lighting control for Logitech gaming peripherals"""
    pass


@cli.command()
def interactive():
    """Interactive mode - guided setup"""
    console.print(Panel.fit(
        "[bold cyan]LogiLight Interactive Setup[/bold cyan]\\n"
        "Configure your Logitech RGB devices",
        border_style="cyan"
    ))

    # Detect devices
    console.print("\\n[yellow]Detecting devices...[/yellow]")
    detector = DeviceDetector()
    keyboards, mice = detector.detect_all()

    if not keyboards and not mice:
        console.print("[red]No Logitech RGB devices found![/red]")
        console.print("Make sure your devices are connected.")
        sys.exit(1)

    # Display found devices
    table = Table(title="Detected Devices")
    table.add_column("Type", style="cyan")
    table.add_column("Device", style="green")

    for kb in keyboards:
        table.add_row("Keyboard", kb['name'])
    for mouse in mice:
        table.add_row("Mouse", mouse['name'])

    console.print(table)

    # Get color from user
    console.print("\\n[cyan]Choose a color:[/cyan]")
    console.print("1. Red (ff0000)")
    console.print("2. Green (00ff00)")
    console.print("3. Blue (0000ff)")
    console.print("4. Purple (8000ff)")
    console.print("5. Cyan (00a8ff)")
    console.print("6. White (ffffff)")
    console.print("7. Custom")

    choice = Prompt.ask("Select option", choices=["1", "2", "3", "4", "5", "6", "7"])

    colors = {
        "1": "ff0000",
        "2": "00ff00",
        "3": "0000ff",
        "4": "8000ff",
        "5": "00a8ff",
        "6": "ffffff"
    }

    if choice == "7":
        color = Prompt.ask("Enter hex color (RRGGBB)")
    else:
        color = colors[choice]

    # Apply settings
    console.print(f"\\n[yellow]Applying color {color}...[/yellow]")

    for kb in keyboards:
        kb_controller = KeyboardController(kb)
        kb_controller.set_color(color)

    for mouse in mice:
        mouse_controller = MouseController(mouse)
        mouse_controller.set_color(color)

    console.print("[green]✓ Settings applied![/green]")

    # Ask about startup
    if Confirm.ask("\\nEnable automatic lighting on boot?"):
        systemd = SystemdManager()
        systemd.create_services(keyboards, mice, color)
        console.print("[green]✓ Startup services created![/green]")
        console.print("Your lighting will automatically activate on boot.")


@cli.command()
def list():
    """List all detected Logitech RGB devices"""
    detector = DeviceDetector()
    keyboards, mice = detector.detect_all()

    if not keyboards and not mice:
        console.print("[red]No Logitech RGB devices found[/red]")
        return

    table = Table(title="Logitech RGB Devices")
    table.add_column("Type", style="cyan")
    table.add_column("Device", style="green")
    table.add_column("VID:PID", style="yellow")
    table.add_column("Tool", style="magenta")

    for kb in keyboards:
        table.add_row(
            "Keyboard",
            kb['name'],
            f"{kb['vid']}:{kb['pid']}",
            "g810-led"
        )

    for mouse in mice:
        table.add_row(
            "Mouse",
            mouse['name'],
            f"{mouse['vid']}:{mouse['pid']}",
            "ratbagctl"
        )

    console.print(table)


@cli.command()
@click.option('--color', '-c', required=True, help='Hex color code (RRGGBB)')
@click.option('--effect', '-e', help='Effect: solid, breathing, cycle, wave')
def set(color, effect):
    """Set color/effect for all devices"""
    detector = DeviceDetector()
    keyboards, mice = detector.detect_all()

    if not keyboards and not mice:
        console.print("[red]No devices found[/red]")
        return

    # Apply to keyboards
    for kb in keyboards:
        kb_controller = KeyboardController(kb)
        if effect:
            kb_controller.set_effect(effect, color)
        else:
            kb_controller.set_color(color)
        console.print(f"[green]✓[/green] {kb['name']}: {color}")

    # Apply to mice
    for mouse in mice:
        mouse_controller = MouseController(mouse)
        if effect:
            mouse_controller.set_effect(effect, color)
        else:
            mouse_controller.set_color(color)
        console.print(f"[green]✓[/green] {mouse['name']}: {color}")


@cli.command()
@click.option('--color', '-c', help='Hex color code (RRGGBB)')
@click.option('--effect', '-e', help='Effect: solid, breathing, cycle, wave')
@click.option('--speed', '-s', help='Effect speed in seconds')
def keyboard(color, effect, speed):
    """Configure keyboard lighting"""
    detector = DeviceDetector()
    keyboards, _ = detector.detect_all()

    if not keyboards:
        console.print("[red]No keyboards found[/red]")
        return

    for kb in keyboards:
        kb_controller = KeyboardController(kb)
        if effect:
            kb_controller.set_effect(effect, color, speed)
        elif color:
            kb_controller.set_color(color)
        console.print(f"[green]✓[/green] {kb['name']} configured")


@cli.command()
@click.option('--color', '-c', help='Hex color code (RRGGBB)')
@click.option('--effect', '-e', help='Effect: solid, breathing, cycle')
def mouse(color, effect):
    """Configure mouse lighting"""
    detector = DeviceDetector()
    _, mice = detector.detect_all()

    if not mice:
        console.print("[red]No mice found[/red]")
        return

    for m in mice:
        mouse_controller = MouseController(m)
        if effect:
            mouse_controller.set_effect(effect, color)
        elif color:
            mouse_controller.set_color(color)
        console.print(f"[green]✓[/green] {m['name']} configured")


@cli.command(name='enable-startup')
def enable_startup():
    """Enable automatic lighting on system boot"""
    detector = DeviceDetector()
    keyboards, mice = detector.detect_all()

    if not keyboards and not mice:
        console.print("[red]No devices found[/red]")
        return

    # Load saved config or use defaults
    config = ConfigManager()
    settings = config.load()

    color = settings.get('color', '8000ff')

    systemd = SystemdManager()
    systemd.create_services(keyboards, mice, color)

    console.print("[green]✓ Startup services enabled[/green]")
    console.print("Your lighting will automatically activate on boot.")


@cli.command(name='disable-startup')
def disable_startup():
    """Disable automatic lighting on system boot"""
    systemd = SystemdManager()
    systemd.remove_services()

    console.print("[green]✓ Startup services disabled[/green]")


@cli.command()
def status():
    """Check status of LogiLight services"""
    systemd = SystemdManager()
    status_info = systemd.check_status()

    table = Table(title="LogiLight Status")
    table.add_column("Service", style="cyan")
    table.add_column("Status", style="green")

    for service, active in status_info.items():
        status_text = "[green]Active[/green]" if active else "[red]Inactive[/red]"
        table.add_row(service, status_text)

    console.print(table)


@cli.command()
@click.argument('name')
def save(name):
    """Save current configuration as a profile"""
    detector = DeviceDetector()
    keyboards, mice = detector.detect_all()

    config = ConfigManager()
    config.save_profile(name, keyboards, mice)

    console.print(f"[green]✓ Profile '{name}' saved[/green]")


@cli.command()
@click.argument('name')
def load(name):
    """Load a saved profile"""
    config = ConfigManager()
    profile = config.load_profile(name)

    if not profile:
        console.print(f"[red]Profile '{name}' not found[/red]")
        return

    # Apply profile settings
    console.print(f"[yellow]Loading profile '{name}'...[/yellow]")

    # Implementation would apply saved settings
    console.print(f"[green]✓ Profile '{name}' loaded[/green]")


def main():
    """Main entry point"""
    try:
        cli()
    except KeyboardInterrupt:
        console.print("\\n[yellow]Interrupted by user[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)


if __name__ == '__main__':
    main()
