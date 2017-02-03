import logging
import pandas as pd

class Parser(object):
    """Parse that b

    Attributes:
        log (logging.Logger): The logger for this module.
        csvfile (str): The csv file to parse.
    """
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    def __init__(self, csvfile):
        """Initialize a parser b

        Args: 
            csvfile (str): The csv file to parse.
        """
        self.csvfile = csvfile

    def parse(self):
        """

        """
        return pd.read_csv(self.csvfile)
