from SummarAIze.pipeline.data_ingestion_pipline import DataIngestionPipeline
from SummarAIze.pipeline.data_validation_pipeline import DataValidationPipeline
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


STAGE = "Data Validation"
try:
    logger.info(f"////////////////////{STAGE} started////////////////////")
    data_validation = DataValidationPipeline()
    data_validation.start()
    logger.info(f"///////////////////{STAGE} completed///////////////////")
except Exception as e:
    logger.exception(e)
    raise e