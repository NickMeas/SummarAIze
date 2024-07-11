from SummarAIze.config.configuration import ConfigurationManager
from SummarAIze.components.data_ingestion import DataIngestion
from SummarAIze.logging import logger

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def start(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download()
        data_ingestion.extract_file()