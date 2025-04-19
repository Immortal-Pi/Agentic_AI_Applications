from src.textSummerizer.config.configuration import ConfigurationManager
from src.textSummerizer.components.data_transformation import DataTransformation 
from src.textSummerizer.logging import logger
from src.textSummerizer.components.model_trainer import ModelTrainer 


class ModelTrainerPipeline:
    def __init__(self):
        pass 

    def initiate_model_trainer(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer_config=ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()


