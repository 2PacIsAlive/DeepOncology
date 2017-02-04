import logging
import pandas as pd


class Parser(object):
    """Parse that b

    Attributes:
        log (logging.Logger): The logger for this module.
    """
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    def parse(self, csvfile):
        """

        Generates:
            list of tuples: First item is index, second item is pandas.dataframe.
        """
        return pd.read_csv(csvfile).iterrows()

