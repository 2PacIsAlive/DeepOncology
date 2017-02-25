import logging
import numpy as np


class Saver(object):
    """Save that b

    Attributes:
        log (logging.Logger): The logger for this module.
    """
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)
    
    def save(self, filename, image):
        """

        Args: 
            filename (str): The path/name of the file being saved.
            image (numpy.ndarray): The image to save.
        """
        np.save(filename, image)


class Loader(object):
    """Load that b

    Attributes:
        log (logging.Logger): The logger for this module.
    """
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)
    
    def load(self, filename):
        """

        Args: 
            filename (str): The path/name of the file to load.

        Returns: 
            numpy.ndarray: The numpy array from the specified file.
        """
        return np.load(filename)

