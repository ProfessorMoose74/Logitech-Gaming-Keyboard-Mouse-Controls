# LogiLight 🌈

**Easy RGB lighting control for Logitech gaming peripherals on Linux**

LogiLight is a user-friendly command-line tool that makes it simple to configure and control RGB lighting on Logitech gaming keyboards and mice under Linux. No more complicated commands or manual systemd service creation!

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org)
[![Platform](https://img.shields.io/badge/platform-linux-lightgrey)](https://www.kernel.org)
[![GitHub stars](https://img.shields.io/github/stars/ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls?style=social)](https://github.com/ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls)](https://github.com/ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls/issues)

## ✨ Features

- 🎨 **Interactive color picker** - Easy-to-use interface for selecting colors
- 🔍 **Auto-detection** - Automatically finds your Logitech RGB devices
- ⚡ **Quick presets** - One-command setup for popular colors and effects
- 🚀 **Startup configuration** - Automatically apply settings on boot
- 🖱️ **Keyboard & Mouse support** - Works with G-series keyboards and LIGHTSYNC mice
- 💾 **Save profiles** - Create and switch between lighting profiles
- 🔧 **No manual setup** - Handles systemd services, udev rules, and dependencies
- 🐧 **Multi-distro** - Works on Ubuntu, Fedora, Arch, openSUSE, and more

## 🎮 Supported Devices

### Keyboards (via g810-led)
- Logitech G213 Prodigy
- Logitech G410, G413, G512, G513, G610
- Logitech G810, G910
- Logitech G Pro

### Mice (via libratbag)
- Logitech G102, G203 LIGHTSYNC
- Logitech G305, G403, G502, G604, G703
- Logitech G Pro Wireless
- And many more supported by libratbag

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls.git
cd Logitech-Gaming-Keyboard-Mouse-Controls

# Run the installer
sudo ./scripts/install.sh

# Or install manually
pip install -r requirements.txt
sudo python3 setup.py install
```

### Basic Usage

```bash
# Interactive mode - guided setup
logilight

# Set all devices to purple
logilight set --color 8000ff

# Set keyboard to rainbow cycle effect
logilight keyboard --effect cycle

# Set mouse to breathing red
logilight mouse --color ff0000 --effect breathing

# List detected devices
logilight list

# Save current setup as a profile
logilight save purple-setup

# Load a saved profile
logilight load purple-setup
```

## 📖 Documentation

- [Installation Guide](docs/INSTALLATION.md) - Detailed installation instructions
- [Usage Guide](docs/USAGE.md) - Complete command reference
- [Supported Devices](docs/SUPPORTED_DEVICES.md) - Full device compatibility list
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common issues and solutions

## 🎨 Examples

### Solid Colors

```bash
# Red
logilight set --color ff0000

# Green
logilight set --color 00ff00

# Blue
logilight set --color 0000ff

# Purple
logilight set --color 8000ff

# Cyan
logilight set --color 00a8ff
```

### Effects

```bash
# Rainbow cycle (keyboard)
logilight keyboard --effect cycle --speed 10

# Breathing effect (all devices)
logilight set --color ff0000 --effect breathing --speed 5

# Wave effect (keyboard)
logilight keyboard --effect wave --speed 5
```

### Startup Configuration

```bash
# Enable automatic lighting on boot
logilight enable-startup

# Disable automatic lighting
logilight disable-startup

# Check startup status
logilight status
```

## 🛠️ How It Works

LogiLight is a wrapper around proven Linux RGB tools:
- **g810-led** for Logitech keyboards
- **libratbag/ratbagctl** for Logitech mice

It simplifies configuration by:
1. Auto-detecting your Logitech devices
2. Managing systemd services for persistence
3. Creating udev rules for automatic activation
4. Providing a user-friendly interface
5. Handling group permissions automatically

## 🔧 Requirements

### System Dependencies

**Arch Linux / Manjaro:**
```bash
sudo pacman -S g810-led libratbag
```

**Ubuntu / Debian:**
```bash
sudo apt install g810-led ratbagd libratbag-tools
```

**Fedora:**
```bash
sudo dnf install g810-led ratbagd libratbag-ratbagd
```

**openSUSE:**
```bash
sudo zypper install g810-led libratbag-tools ratbagd
```

### Python Dependencies
- Python 3.8+
- click (CLI framework)
- rich (terminal formatting)
- pyyaml (config files)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Report bugs** - Open an issue with details
2. **Request features** - Tell us what you'd like to see
3. **Add device support** - Test and document new devices
4. **Improve docs** - Help make the documentation better
5. **Submit PRs** - Code contributions are appreciated!

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- **g810-led** - [MatMoul/g810-led](https://github.com/MatMoul/g810-led)
- **libratbag** - [libratbag/libratbag](https://github.com/libratbag/libratbag)
- **Piper** - GUI for libratbag

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls/discussions)
- **Project Origin**: Built as part of the [Helyxium VR Platform](https://github.com/ProfessorMoose74/Helyxium) project

## 🗺️ Roadmap

- [ ] GUI application (PyQt/GTK)
- [ ] Per-key RGB support (advanced keyboards)
- [ ] Sync lighting across devices
- [ ] Integration with desktop environments
- [ ] Animated lighting patterns
- [ ] Community lighting profiles repository
- [ ] Support for more RGB protocols (OpenRGB integration)

---

**Made with ❤️ for the Linux gaming community**

If LogiLight helps you, please ⭐ star the repo!
