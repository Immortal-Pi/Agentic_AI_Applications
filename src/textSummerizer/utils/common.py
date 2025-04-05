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
    except Exception as e:
        print(e)