import os
import yaml

# disable errors
yaml.warnings({'YAMLLoadWarning': False})

# main function
def parse_yaml_file(filename: str):
    """Parse data from .yml files"""
    if not os.path.exists(filename):
        raise FileNotFoundError

    with open(filename) as f:
        return yaml.load(f)
