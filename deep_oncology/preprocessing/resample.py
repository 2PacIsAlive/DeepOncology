import logging
import numpy as np
import scipy.ndimage


class Resampler(object):
    """Remove invariance in scans.

    Since different scans may have different pixel spacings, it is 
    beneficial to resample the entire dataset such that downstream
    algorithms do not have to learn this invariance.

    Attributes:
        log (logging.Logger): The logger for this module.
    """
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    def resample(self, image, scan, new_spacing=[1,1,1]):
        """Resample all data in a scan to a new isotropic resolution.

        Adapted from:
        https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial
        
        Args:
            image: 
            scan:
            new_spacing:

        Returns:
            tuple of :
        """
        self.log.info("resampling {}".format(scan[0].PatientName)) 
        # Determine current pixel spacing
        spacing = map(float, ([scan[0].SliceThickness] + scan[0].PixelSpacing))
        spacing = np.array(list(spacing))
        resize_factor = spacing / new_spacing
        new_real_shape = image.shape * resize_factor
        new_shape = np.round(new_real_shape)
        real_resize_factor = new_shape / image.shape
        new_spacing = spacing / real_resize_factor
        image = scipy.ndimage.interpolation.zoom(image, real_resize_factor, mode='nearest')
        return image, new_spacing 
