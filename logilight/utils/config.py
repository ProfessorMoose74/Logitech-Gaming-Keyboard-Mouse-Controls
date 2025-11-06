"""Configuration management"""

import os
import yaml
import json
from pathlib import Path


class ConfigManager:
    """Manage LogiLight configuration and profiles"""

    def __init__(self):
        self.config_dir = Path.home() / '.config' / 'logilight'
        self.config_file = self.config_dir / 'config.yaml'
        self.profiles_dir = self.config_dir / 'profiles'

        # Create directories if they don't exist
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.profiles_dir.mkdir(parents=True, exist_ok=True)

    def load(self):
        """Load main configuration

        Returns:
            dict: Configuration settings
        """
        if not self.config_file.exists():
            return self._get_default_config()

        try:
            with open(self.config_file, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
            return self._get_default_config()

    def save(self, config):
        """Save main configuration

        Args:
            config (dict): Configuration settings
        """
        try:
            with open(self.config_file, 'w') as f:
                yaml.dump(config, f, default_flow_style=False)
        except Exception as e:
            print(f"Error saving config: {e}")

    def save_profile(self, name, keyboards, mice, color=None, effect=None):
        """Save a lighting profile

        Args:
            name (str): Profile name
            keyboards (list): List of keyboards
            mice (list): List of mice
            color (str): Hex color code (optional)
            effect (str): Effect name (optional)
        """
        profile = {
            'name': name,
            'color': color or '8000ff',
            'effect': effect,
            'keyboards': keyboards,
            'mice': mice
        }

        profile_file = self.profiles_dir / f'{name}.yaml'

        try:
            with open(profile_file, 'w') as f:
                yaml.dump(profile, f, default_flow_style=False)
        except Exception as e:
            print(f"Error saving profile: {e}")

    def load_profile(self, name):
        """Load a saved profile

        Args:
            name (str): Profile name

        Returns:
            dict: Profile settings or None if not found
        """
        profile_file = self.profiles_dir / f'{name}.yaml'

        if not profile_file.exists():
            return None

        try:
            with open(profile_file, 'r') as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"Error loading profile: {e}")
            return None

    def list_profiles(self):
        """List all saved profiles

        Returns:
            list: Profile names
        """
        profiles = []

        for file in self.profiles_dir.glob('*.yaml'):
            profiles.append(file.stem)

        return profiles

    def _get_default_config(self):
        """Get default configuration

        Returns:
            dict: Default config
        """
        return {
            'color': '8000ff',
            'effect': None,
            'startup_enabled': False
        }
