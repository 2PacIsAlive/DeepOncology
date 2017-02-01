import logging
import numpy as np
from skimage import measure


class LungSegmenter(object):
    """Extract the lungs from a scan.

    Attributes:
        log (logging.Logger): The logger for this module.
    """
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    def largest_label_volume(self, im, bg=-1):
        """
    
        Adapted from:
        https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial
  
        Args:
            im:
            bg:

        Returns:
            
        """
        vals, counts = np.unique(im, return_counts=True)

        counts = counts[vals != bg]
        vals = vals[vals != bg]

        if len(counts) > 0:
            return vals[np.argmax(counts)]
        else:
            return None

    def mask(self, image, fill_lungs=True):
        """

        Adapted from:
        https://www.kaggle.com/gzuidhof/data-science-bowl-2017/full-preprocessing-tutorial
        
        Args:
            image:
            fill_lungs:

        Returns:
        
        """
        # not actually binary, but 1 and 2. 
        # 0 is treated as background, which we do not want
        binary_image = np.array(image > -320, dtype=np.int8)+1
        labels = measure.label(binary_image)
        
        # Pick the pixel in the very corner to determine which label is air.
        #   Improvement: Pick multiple background labels from around the patient
        #   More resistant to "trays" on which the patient lays cutting the air 
        #   around the person in half
        background_label = labels[0,0,0]
        
        #Fill the air around the person
        binary_image[background_label == labels] = 2
        
        
        # Method of filling the lung structures (that is superior to something like 
        # morphological closing)
        if fill_lungs:
            # For every slice we determine the largest solid structure
            for i, axial_slice in enumerate(binary_image):
                axial_slice = axial_slice - 1
                labeling = measure.label(axial_slice)
                l_max = self.largest_label_volume(labeling, bg=0)
                
                if l_max is not None: #This slice contains some lung
                    binary_image[i][labeling != l_max] = 1

        
        binary_image -= 1 #Make the image actual binary
        binary_image = 1-binary_image # Invert it, lungs are now 1
        
        # Remove other air pockets insided body
        labels = measure.label(binary_image, background=0)
        l_max = self.largest_label_volume(labels, bg=0)
        if l_max is not None: # There are air pockets
            binary_image[labels != l_max] = 0
     
        return binary_image 
