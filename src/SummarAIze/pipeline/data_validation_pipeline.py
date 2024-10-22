from SummarAIze.config.configuration import ConfigurationManager
from SummarAIze.components.data_validation import DataValidation
from SummarAIze.logging import logger

class DataValidationPipeline:
    def __init__(self):
        pass
    
    def start(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files()