import os


def parse_yaml_file(filename: str):
    """Parse data from .yml files"""
    if not os.path.exists(filename):
        raise FileNotFoundError
    return {}
