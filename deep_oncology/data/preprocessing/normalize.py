import logging
import numpy as np


class Normalizer(object):
    """General normalization of data.

    Responsible for computing/adding missing attributes.

    Attributes:
        log (logging.Logger): The logger for this module.
        min_bound (float):
        max_bound (float):
        pixel_mean (float):
    """
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    min_bound = -1000.0
    max_bound = 400.0
    pixel_mean = 0.25   
    
    def normalize(self, image):
        image = (image - self.min_bound) / (self.max_bound - self.min_bound)
        image[image>1] = 1.
        image[image<0] = 0.
        return image

    def zero_center(self, image):
        """
        """
        return image - self.pixel_mean

    def pad_3d_array(self, image, size):
        """
        """
        def _shift(dim, size):
            """
            """
            shift_before = (size - dim) / 2
            if shift_before is float:
                shift_before = int(shift_before)
                shift_after = shift_before + 1
            else:
                shift_after = shift_before
            return (shift_before, shift_after)
        
        npad=(_shift(image.shape[0], size[0]), 
              _shift(image.shape[1], size[1]), 
              _shift(image.shape[2], size[2]))   
        self.log.info('calculated padding {}'.format(npad))
        return np.pad(image, pad_width=npad, 
                        mode='constant', constant_values=0)

    def add_slice_thickness(self, scan):
        """Add slice thickness to each dataset in a list of slices.

        Adapted from:
        https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial

        Args:
            scan (list): A list of datasets from a folder of .dcm dicom files.

        Returns:
            list: A list of slices with slice thickness computed.
        """
        try:
            slice_thickness = np.abs(scan[0].ImagePositionPatient[2] - scan[1].ImagePositionPatient[2])
        except:
            slice_thickness = np.abs(scan[0].SliceLocation - scan[1].SliceLocation)
        self.log.debug("slice thickness {} for patient {}".format(slice_thickness, scan[0].PatientName))
        for dataset in scan:
            dataset.SliceThickness = slice_thickness
        return scan
 
