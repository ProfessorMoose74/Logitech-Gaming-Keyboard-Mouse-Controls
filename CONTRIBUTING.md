# Contributing to LogiLight

First off, thank you for considering contributing to LogiLight! It's people like you that make LogiLight such a great tool for the Linux gaming community.

## Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. Please be kind and constructive.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include system information** (distro, kernel version, device model)
- **Include logs** if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List some examples of how it would be used**

### Adding Device Support

Know a Logitech device that should work but isn't detected? You can help add it!

1. Find the device's Product ID with `lsusb | grep Logitech`
2. Add the PID and name to `logilight/devices/detector.py`
3. Test the device
4. Submit a pull request with your findings

### Pull Requests

1. Fork the repo and create your branch from `main`
2. Make your changes
3. Test your changes thoroughly
4. Update documentation if needed
5. Submit a pull request with a clear description of the changes

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/LogiLight.git
cd LogiLight

# Install in development mode
pip3 install -e .

# Install dev dependencies
pip3 install black flake8 pytest

# Test your changes
python3 -m logilight.cli --help
```

## Style Guide

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Write clear commit messages

## Testing

Before submitting a PR:

1. Test on your system
2. Ensure no errors or warnings
3. Verify existing functionality still works
4. Test with different device combinations if possible

## Documentation

- Update README.md for user-facing changes
- Update docstrings for code changes
- Add examples for new features

## Questions?

Feel free to open an issue labeled "question" if you need help!

Thank you for contributing! 🎉
