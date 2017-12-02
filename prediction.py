import keras
import numpy as np
model = keras.models.load_model('trained_model.h5')

def test():
    """Tests to see if the model is working """
    X = [22.05,25.22,21.23,23.43]
    X = [X]
    X = np.asarray(X,dtype=np.float32)
    a = model.predict(X)
    print(a)

def predictDay(x):
    """Takes the data provided and makes a prediction for each day provided"""
    x = [x]
    x = np.asarray(x,dtype=np.float32)
    result = model.predict(x)
    return result
