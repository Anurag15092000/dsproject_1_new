from src.datascience.config.configuration import TransformationConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger


STAGE_NAME="Data Transformation Stage"



class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config=TransformationConfigurationManager()
        data_transformation_config=config.get_data_transformation()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()
        
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<< \n\nx==========x")
        obj=DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        