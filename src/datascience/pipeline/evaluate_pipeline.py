from src.datascience.config.configuration import EvaluationConfigurationManager
from src.datascience.components.evaluation import ModelEvaluation
from src.datascience import logger


STAGE_NAME="Evaluation Stage"

class ModelEvalPipeline:
    def __init__(self):
        pass
    def initiate_model_evaluation(self):
        config = EvaluationConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()