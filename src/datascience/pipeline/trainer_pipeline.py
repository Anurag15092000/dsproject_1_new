
from src.datascience.config.configuration import TrainerConfigurationManager
from src.datascience.components.trainer import ModelTrainer



STAGE_NAME="Trainer Stage"



class TrainingPipeline:
    def __init__(self):
        pass

    def initiate_training(self):
        config=TrainerConfigurationManager()
        trainer_config=config.get_model_trainer_config()
        trainer=ModelTrainer(config=trainer_config)
        trainer.train()

        
if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<< \n\nx==========x")
        obj=TrainingPipeline()
        obj.initiate_training()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<< \n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        