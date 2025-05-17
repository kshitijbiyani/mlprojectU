import os
import sys
from src.mlprojects.exception import CustomException
import numpy as np
import pandas as pd
import dill
def save_object(file_path, obj):
    dir_path=os.path.join(file_path)
    os.makedirs(dir_path,exist_ok=True)
    with open(file_path, "wb") as file_obj:
        dill.dump(obj,file_path)