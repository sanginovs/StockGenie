import keras
import numpy as np
model = keras.models.load_model('trained_model.h5')

X = [[22.05,25.22,21.23,23.43]]
X = np.asarray(X,dtype=np.float32)
a = model.predict(X)
print(a)
