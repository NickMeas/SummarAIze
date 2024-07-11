import os
import urllib.request as request
import zipfile
from SummarAIze.logging import logger
from SummarAIze.utils.common import get_size
from pathlib import Path
from SummarAIze.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
        
    def download(self):
        """
        The `download` function checks if a local data file exists, and if not, downloads it from a
        specified URL and logs the download information.
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
                )
            logger.info(f"{filename} downloaded with the following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
            
            
    def extract_file(self):
        """
        The function `extract_file` extracts the contents of a zip file to a specified directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        