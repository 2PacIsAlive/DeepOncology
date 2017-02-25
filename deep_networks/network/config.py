import logging


class NetworkConfig(object):
    """

    Attributes:
        log (logging.Logger): The logger for this module.
    """
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    def __init__(self, config):
		pass
