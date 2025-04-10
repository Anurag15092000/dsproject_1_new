from src.datascience import logger
from src.datascience.pipeline.trainer_pipeline import TrainingPipeline



STAGE_NAME="Training Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<< \n\nx==========x")
    obj=TrainingPipeline()
    obj.initiate_training()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    



