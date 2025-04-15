from src.datascience import logger
from src.datascience.pipeline.evaluate_pipeline import ModelEvalPipeline



STAGE_NAME="Evaluation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<< \n\nx==========x")
    obj=ModelEvalPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    




