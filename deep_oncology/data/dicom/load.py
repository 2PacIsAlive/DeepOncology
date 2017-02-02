import logging 
import dicom
import numpy as np
from glob import glob


class Loader(object):
    """Responsible for loading dicom resources.

    This class handles basic loading of patient scans and also performs some basic
    routines to put the data into a standard format to work with.

    Attributes:
        log (logging.Logger): The logger for this module.
    """
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    def load_scan(self, folder):
        """Load the dicom chest scans of one patient.
        
        Each folder in the DSB dataset corresponds to the scan of one patient.
        This function loads all the files in a patient's directory.
        
        Adapted from:
        https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial

        Args:
            folder (str): A local folder containing .dcm dicom files. 

        Returns:
            list: A sorted list of slices.    
        """
        self.log.info("loading scan from {}".format(folder))
        scan = [dicom.read_file(dicom_file) for dicom_file in glob("{}/*.dcm".format(folder))]
        self.log.debug("loaded {} files".format(len(scan)))
        scan.sort(key = lambda x: int(x.ImagePositionPatient[2]))
        return scan

