from src.textSummerizer.config.configuration import ConfigurationManager
from src.textSummerizer.components.data_transformation import DataTransformation 
from src.textSummerizer.logging import logger
from src.textSummerizer.components.model_trainer import ModelTrainer 
from src.textSummerizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass 

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation=ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()

