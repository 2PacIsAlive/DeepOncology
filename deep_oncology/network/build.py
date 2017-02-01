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
    """
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    def __init__(self, shape):
        """
        
        Args: 
            shape (list): Shape of the input data.
        """
        self.network = input_data(shape=shape)

    def add_conv_3d_layers(self, num_filters, filter_size, activation, num_layers=1):
        """
    
        Args:
            num_filters (int): Number of convolutional filters to use.
            filter_size (int): Size of each filter.
            activation (str): Activation function to use.
            num_layers (int): The number of 3d convolutional layers to add.
        """
        for i in range(num_layers):
            self.network = conv_3d(self.network, num_filters, filter_size, 
                                    activation=activation)

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

    def build(self, checkpoint_path, max_checkpoints, tensorboard_verbose):
        """
        
        Args:
            checkpoint_path (str):
            max_checkpoints (int):
            tensorboard_verbose (int):

        Returns
            tflearn.DNN: A tflearn DNN object that can be used as an estimator. 
        """
        return DNN(self.network, checkpoint_path=checkpoint_path,
                    max_checkpoints=max_checkpoints, 
                    tensorboard_verbose=tensorboard_verbose)

