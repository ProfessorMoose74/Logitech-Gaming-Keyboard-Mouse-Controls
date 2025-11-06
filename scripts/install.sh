#!/bin/bash
# LogiLight Installation Script

set -e

echo "======================================"
echo "  LogiLight Installation"
echo "======================================"
echo ""

# Check if running with sudo
if [ "$EUID" -ne 0 ]; then
    echo "Please run with sudo: sudo ./install.sh"
    exit 1
fi

# Detect distribution
if [ -f /etc/os-release ]; then
    . /etc/os-release
    DISTRO=$ID
else
    echo "Cannot detect Linux distribution"
    exit 1
fi

echo "Detected distribution: $DISTRO"
echo ""

# Install system dependencies based on distro
echo "Installing system dependencies..."

case "$DISTRO" in
    ubuntu|debian)
        apt update
        apt install -y g810-led ratbagd libratbag-tools python3 python3-pip
        ;;
    fedora)
        dnf install -y g810-led ratbagd libratbag-ratbagd python3 python3-pip
        ;;
    arch|manjaro)
        pacman -S --noconfirm g810-led libratbag python python-pip
        ;;
    opensuse*|sles)
        zypper install -y g810-led libratbag-tools ratbagd python3 python3-pip
        ;;
    *)
        echo "Unsupported distribution: $DISTRO"
        echo "Please install g810-led and libratbag manually"
        ;;
esac

echo ""
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo ""
echo "Installing LogiLight..."
python3 setup.py install

echo ""
echo "Setting up user groups..."
# Add current user to input and games groups
REAL_USER=${SUDO_USER:-$USER}
usermod -aG input,games $REAL_USER

echo ""
echo "Starting ratbagd service..."
systemctl start ratbagd
systemctl enable ratbagd

echo ""
echo "======================================"
echo "  Installation Complete!"
echo "======================================"
echo ""
echo "✓ LogiLight has been installed"
echo "✓ Dependencies are configured"
echo "✓ Services are running"
echo ""
echo "IMPORTANT: Please log out and back in for group"
echo "permissions to take effect."
echo ""
echo "Get started:"
echo "  logilight                 # Interactive mode"
echo "  logilight list            # List devices"
echo "  logilight set --color 8000ff  # Set purple"
echo ""
echo "For help:"
echo "  logilight --help"
echo ""
