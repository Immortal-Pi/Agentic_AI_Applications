import os 
from box.exceptions import BoxValueError
import yaml 
from src.textSummerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any 


@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f'Yaml file {path_to_yaml} loaded successfully')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        print(e)


@ensure_annotations
def create_directory(path_to_dir:list, verbose=True):
    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f'created directory at: {path}')


    