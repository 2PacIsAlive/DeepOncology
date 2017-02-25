import logging
import numpy as np


class Converter(object):
    """Pixel conversions.

    Attributes:
        log (logging.Logger): The logger for this module.
    """
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    def pixels_to_hu(self, scan):
        """Convert all pixels in a list of datasets to Hounsfield Units.

        Adapted from:
        https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial

        Args:
            scan (list): A list of datasets from a folder of .dcm dicom files.
        
        Returns:
            numpy.ndarray: A scan converted to Hounsfield Units.  
        """
        self.log.debug("converting {} to hu".format(scan[0].PatientName))
        image = np.stack([dataset.pixel_array for dataset in scan]).astype(np.int16)
        # Set outside-of-scan pixels to 0
        # The intercept is usually -1024, so air is approximately 0
        image[image == -2000] = 0
    
        for slice_index in range(len(scan)):
            
            intercept = scan[slice_index].RescaleIntercept
            slope = scan[slice_index].RescaleSlope
            
            if slope != 1:
                image[slice_index] = slope * image[slice_index].astype(np.float64)
                image[slice_index] = image[slice_index].astype(np.int16)
                
            image[slice_index] += np.int16(intercept)
        
        return np.array(image, dtype=np.int16)

