from SummarAIze.pipeline.data_ingestion_pipline import DataIngestionPipeline
from SummarAIze.logging import logger

STAGE = "Data Ingestion"
try:
    logger.info(f"////////////////////{STAGE} started////////////////////")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.start()
    logger.info(f"///////////////////{STAGE} completed///////////////////")
except Exception as e:
    logger.exception(e)
    raise e