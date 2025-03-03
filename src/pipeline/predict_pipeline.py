import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            print("Model and preprocessor path defined")
            model = load_object(file_path = model_path)
            print("Model Loaded")
            preprocessor = load_object(file_path = preprocessor_path)
            print("Preprocessor Loaded")
            data_scaled = preprocessor.transform(features)
            print("Input data scaled using preprocessor")
            preds = model.predict(data_scaled)
            print("Model prediction done!")
            return preds
        except Exception as e:
            print(CustomException(e,sys))
            raise CustomException(e,sys)


class CustomData:
    def __init__(self,
        gender:str,
        race_ethnicity:str,
        parental_level_of_education:str,
        lunch:str,
        test_preparation_course:str,
        writing_score:int,
        reading_score:int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.writing_score = writing_score

        self.reading_score = reading_score

    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender" : [self.gender[0]],
                "race_ethnicity" : [self.race_ethnicity[0]],
                "parental_level_of_education" : [self.parental_level_of_education[0]],
                "lunch" : [self.lunch[0]],
                "test_preparation_course" : [self.test_preparation_course[0]],
                "writing_score" : [self.writing_score[0]],
                "reading_score" : [self.reading_score]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e,sys)
        