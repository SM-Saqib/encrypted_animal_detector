from .architecture import Animal_detector
import os

import tensorflow as tf
# from tensorflow import keras






class Predictor:
    """
    Main class that provides the funtionality of running the Animal_detection model
    """
    def __init__(self):
        """
        Initialization Method

        Arguments:
        ----------
        """

        model_path="modelo.h5"
        self.output=[]
        self.model=Animal_detector()
        latest = tf.train.latest_checkpoint(model_path)

        self.model.load_weights(model_path)

    def run(self,image):
        ''' runs inference on an image and returns the predicted class of the animal'''
        predicted=self.model.predict_step(image)
        return predicted["predicted"]


