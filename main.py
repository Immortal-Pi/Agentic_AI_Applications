from src.textSummerizer.logging import logger 
from src.textSummerizer.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from src.textSummerizer.pipeline.stage2_data_transformation import DataTransformationTrainingPipeline
from src.textSummerizer.pipeline.stage3_model_trainer import ModelTrainerPipeline
STAGE_NAME='DATA INGESTION STAGE'

try:
    logger.info(f'stage {STAGE_NAME} initiated')
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f'Stage {STAGE_NAME} Completed')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME='DATA TRANSFORMATION STAGE'

try:
    logger.info(f'stage {STAGE_NAME} initiated')
    data_transformation_pipeline=DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f'Stage {STAGE_NAME} Completed')
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME='MODEL TRAINER STAGE'

try:
    logger.info(f'stage {STAGE_NAME} initiated')
    model_trainer_pipeline=ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f'Stage {STAGE_NAME} Completed')
except Exception as e:
    logger.exception(e)
    raise e 