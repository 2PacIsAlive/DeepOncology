import logging
from tflearn import DNN
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_3d, max_pool_3d
from tflearn.layers.estimator import regression


class NetworkBuilder(object):
    """

    Attributes: 
        log (logging.Logger): The logger for this module.
        network (tflearn.Network): #TODO fixme
        funcmap (dict): A mapping from config strings to NetworkBuilder functions.
    """
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    def __init__(self, shape):
        """
        
        Args: 
            shape (list): Shape of the input data.
        """
        self.funcmap = {
            "fully_connected": self.add_fully_connected_layer,
            "dropout": self.add_dropout_layer,
            "convolution_3d": self.add_conv_3d_layer,
            "max_pooling_3d": self.add_max_pool_3d_layer,
            "regression": self.add_regression_estimator
        }

        self.network = input_data(shape=shape)

    def add_conv_3d_layer(self, options):
        """
    
        Args:
            options (deep_networks.network.config.Conv3DOptions): The parameters for this layer.
            num_filters (int): Number of convolutional filters to use.
            filter_size (int): Size of each filter.
            activation (str): Activation function to use.
        """
        self.network = conv_3d(self.network, options.num_filters, options.filter_size,
                                activation=options.activation)

    def add_max_pool_3d_layer(self, kernel_size, strides): 
        """

        Args: 
            kernel_size (int):
            strides (int):
        """
        self.network = max_pool_3d(self.network, kernel_size, 
                                    strides=strides)
    
    def add_fully_connected_layer(self, num_units):
        """

        Args:
            num_units (int):
            activation (str): 
        """
        self.network = fully_connected(self.network, num_units, 
                                        activation=activation)
        
    def add_dropout_layer(self, keep_prob): 
        """

        Args:
            keep_prob (float): 
        """
        self.network = dropout(self.network, keep_prob)

    def add_regression_estimator(self, optimizer, loss_fcn, learning_rate):
        """

        Args:
            optimizer (str):
            loss_fcn (str):
            learning_rate (float):
        """
        self.network = regression(self.network, optimizer=optimizer,
                                    loss_fcn=loss_fcn, learning_rate=learning_rate)

    def build_from_config(self, config):
        """Construct a network from a config object.

        Args:
            config (deep_networks.network.config): A config object.
        """
        for layer in config:
            self.funcmap[layer.type]](layer.options)

    def build(self, checkpoint_path, max_checkpoints, tensorboard_verbose):
        """
        
        Args:
            checkpoint_path (str):
            max_checkpoints (int):
            tensorboard_verbose (int):

        Returns:
            tflearn.DNN: A tflearn DNN object that can be used as an estimator. 
        """
        return DNN(self.network, checkpoint_path=checkpoint_path,
                    max_checkpoints=max_checkpoints, 
                    tensorboard_verbose=tensorboard_verbose)

