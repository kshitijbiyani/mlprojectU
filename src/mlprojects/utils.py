import os
import sys
from src.mlprojects.exception import CustomException
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score


import os
import dill

def save_object(file_path, obj):
    """
    Serialize `obj` to `file_path` using dill.
    Ensures the containing directory exists.
    """
    # 1. Compute the directory, not including the file name
    dir_name = os.path.dirname(file_path)
    os.makedirs(dir_name, exist_ok=True)

    # 2. Open the file in binary-write and dump into the file object
    with open(file_path, "wb") as file_obj:
        dill.dump(obj, file_obj)


# def save_object(file_path, obj):
    
#     dir_path=os.path.join(file_path)
    
#     os.makedirs(dir_path,exist_ok=True)
    
#     with open(file_path, "wb") as file_obj:
#         dill.dump(obj,file_path)
        
def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            
            model.fit(X_train,y_train)
            
            y_train_pred=model.predict(X_train)
            
            y_test_pred=model.predict(X_test)
            
            train_model_score=r2_score(y_train,y_train_pred)
 
            test_model_score=r2_score(y_test,y_test_pred)
 
            report[list(models.keys())[i]]=test_model_score
 
        return report
 
    except Exception as e:
        raise CustomException(e,sys)