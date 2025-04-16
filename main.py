from src.textSummerizer.logging import logger 
from src.textSummerizer.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME='DATA INGESTION STAGE'

try:
    logger.info(f'stage {STAGE_NAME} initiated')
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f'Stage {STAGE_NAME} Completed')
except Exception as e:
    logger.exception(e)
    raise e 