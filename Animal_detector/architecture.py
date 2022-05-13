from tensorflow.keras.applications.efficientnet import EfficientNetB7
from tensorflow.keras.layers import Flatten, Dense #, Dropout
from tensorflow.keras.models import Sequential, load_model
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam, SGD



class Animal_detector():
    ''' architecture for the model used for detecting the animal'''
    def __init__(self,
        w = 224,
        h = 224,
        model="modelo.h5"):

        '''loading the animal_detector model'''

        # super().__init__()
        # BATCH_SIZE = 64
        
        self.class_no=10,
        self.index_animal_mapping={
            'cane': 0,
            'cavallo': 1,
            'elefante': 2,
            'farfalla': 3,
            'gallina': 4,
            'gatto': 5,
            'mucca': 6,
            'pecora': 7,
            'ragno': 8,
            'scoiattolo': 9
            }
        


        

     
        vgg16 = EfficientNetB7(include_top = False,
                    input_shape = (w, h, 3),
                    weights = "imagenet")

        for layer in vgg16.layers:
            layer.trainable = False

        self.model = Sequential()

        self.model.add(vgg16)
        self.model.add(Flatten())
        self.model.add(Dense(self.class_no, activation = "softmax"))
        
        # otimizador = SGD(learning_rate = 3e-3, momentum = 0.6)

        # self.model.compile(loss="categorical_crossentropy",
        #             optimizer = otimizador,
        #             metrics = ["accuracy"])