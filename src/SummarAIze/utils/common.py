import os
from box.exceptions import BoxValueError
import yaml
from SummarAIze.logging import logger
from box import ConfigBox
from pathlib import Path
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox: 
    """
    The function reads a YAML file and returns its content as a ConfigBox object, logging success and
    handling exceptions.
    
    :param path_to_yaml: The `path_to_yaml` parameter is the file path to the YAML file that you want to
    read and load into a `ConfigBox` object
    :type path_to_yaml: Path
    :return: The function `read_yaml` is returning either a `ConfigBox` object containing the content of
    the YAML file if it is successfully loaded, or it is raising a `ValueError` with the message
    "Invalid yaml file" if there is an issue with the YAML file format. If an exception other than
    `BoxValueError` occurs during the process, the function returns the exception object.
    """
    try: 
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Invalid yaml file")
    except Exception as e:
        return e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    The function `create_directories` creates directories at specified paths and logs the action if
    verbose mode is enabled.
    
    :param path_to_directories: A list of paths where directories will be created
    :type path_to_directories: list
    :param verbose: The `verbose` parameter in the `create_directories` function is a boolean parameter
    that determines whether additional information or logs should be displayed during the execution of
    the function. If `verbose` is set to `True`, the function will log a message indicating that a
    directory is being created at a specific, defaults to True (optional)
    """
    for p in path_to_directories:
        os.makedirs(p, exist_ok = True)
        if verbose:
            logger.info(f"created directory at: {p}")
            
            
@ensure_annotations
def get_size(path: Path) -> str:
    """
    The function `get_size` calculates the size of a file in kilobytes and returns it as a string.
    
    :param path: The `path` parameter in the `get_size` function is expected to be a `Path` object,
    which represents a file or directory path
    :type path: Path
    :return: The function `get_size` takes a file path as input and calculates the size of the file in
    kilobytes. It then returns a string that represents the size of the file in kilobytes with the
    format "~ {size_in_kb} KB".
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"