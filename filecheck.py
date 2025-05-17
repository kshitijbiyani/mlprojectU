import pickle
import dill

with open("./artifacts/preprocessor.pkl", "rb") as f:
    obj = dill.load(f)
    print("Pickle file loaded successfully!")
