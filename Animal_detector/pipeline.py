from .inference import Predictor


class Pipeline:
    """
    animal_detector Class for constructing the pipeline composed of the run method provided by the module
    """
    def __init__(self, region, tokenizer, device="cpu"):
        """
        Initialization method for animal_detector is self composed given there are complete set of files and folders required by the pipeline
        """
        

        self.to(device)
        self.predictor=Predictor()

    # def to(self, device):
    #     self.predictor = Predictor(self.image)
    #     self.device = device

    def run(self, image):
        """
        Takes an img and runs inference on it. 
        The pipeline is there to facilitate addition of preprocessing and postprocessing etc if needed.

        Arguments:
        ----------
            image(PIL image object) : ia=mage of the animal
        Returns:
        --------
            animal_detected (string): 
        """
        animal_detected = self.predictor.run(image)
        return animal_detected