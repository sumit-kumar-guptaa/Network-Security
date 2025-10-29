from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME

import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor=preprocessor
            self.model=model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def predict(self,X):
        try:
            X_transform=self.preprocessor.transform(X)
            y_hat=self.model.predict(X_transform)
            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e,sys)    