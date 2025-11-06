# Changelog

All notable changes to LogiLight will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-06

### Added
- Initial release of LogiLight
- Interactive CLI mode with color picker
- Auto-detection of Logitech RGB keyboards and mice
- Support for g810-led (keyboards) and libratbag (mice)
- Systemd service management for startup persistence
- Profile save/load functionality
- Multiple effects: solid, breathing, rainbow cycle, wave
- Multi-distribution support (Ubuntu, Fedora, Arch, openSUSE)
- One-command installation script
- Comprehensive documentation

### Supported Devices
- **Keyboards**: G213, G410, G413, G512, G513, G610, G810, G910, G Pro
- **Mice**: G102, G203, G305, G403, G502, G604, G703, G Pro Wireless

### Known Issues
- Mouse control requires user to be in `input` and `games` groups (requires logout/login)
- Some older Logitech devices may not be detected automatically

---

## Project Origin

LogiLight was created as part of the [Helyxium VR Platform](https://github.com/ProfessorMoose74/Helyxium) project to solve RGB lighting issues on Linux for gaming peripherals.
