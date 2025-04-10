from src.datascience.config.configuration import ValidationConfigurationManager
from src.datascience.components.data_validation import DataValiadtion
from src.datascience import logger


STAGE_NAME="Data Validation Stage"



class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config=ValidationConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()

        
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<< \n\nx==========x")
        obj=DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        