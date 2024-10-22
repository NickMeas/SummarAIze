from dataclasses import dataclass
from pathlib import Path
from pickletools import string1

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
    
@dataclass(frozen = True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    REQUIRED_FILES: list
    
    

