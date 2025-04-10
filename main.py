from src.datascience import logger
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline



STAGE_NAME="Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<< \n\nx==========x")
    obj=DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
    



