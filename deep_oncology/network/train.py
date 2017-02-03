import logging


class Trainer(object):
    """Trainer for u

    Attributes: 
        log (logging.Logger): The logger for this module.
        network (tflearn.DNN): The network to train.
    """
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    def __init__(self, network):
        """Initialize trainer with a network

        Args:
            network (tflearn.DNN): The network to train.
        """
        self.network = network

    def train(x, y, num_epoch, run_id):
        """Train that b 

        Args:
            x (np.ndarray): 
            y (np.ndarray):
            num_epoch (int): The number of epochs to train for.

        """
        self.network.fit(X, Y, n_epoch=num_epoch, shuffle=True,
                    show_metric=True, batch_size=32, 
                    snapshot_step=num_epoch, snapshot_epoch=False, 
                    run_id=run_id)
