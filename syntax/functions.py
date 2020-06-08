import os
import yaml

# disable errors
from syntax import exceptions

yaml.warnings({'YAMLLoadWarning': False})


# main function
def parse_yaml_file(filename: str):
    """Parse data from .yml files"""
    data = None

    if not os.path.exists(filename):
        raise FileNotFoundError

    with open(filename) as f:
        data = yaml.load(f)

    if not (isinstance(data, dict) or isinstance(data, list)):
        raise exceptions.NotValidFileDataError

    return data
