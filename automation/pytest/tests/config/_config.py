import os
import json

from attrdict import AttrDict

ENVIRONMENT = os.getenv('ENV')
TEAM = os.getenv('TEAM')
supported_keys = ['ENV', 'TEAM']
_vault = AttrDict()


def parse_env_variables():
    """ Function for loading, parsing, and storing environment variables """
    for keys, values in os.environ.items():
        if keys in supported_keys:
            _vault[keys] = values


def parse_json_variables():
    """ Function for loading, parsing, and storing json config variables """
    with open(f'tests/config/{ENVIRONMENT}.json') as json_file:
        for keys, values in json.load(json_file).items():
            _vault[keys] = values
