import logging


class NetworkConfig(object):
    """A network configuration that can be used by a NetworkBuilder.

    Attributes:
        log (logging.Logger): The logger for this module.
        layers (list): A list of LayerConfig objects.

    Raises:
        ValueError: Invalid config, error message contained within.
    """
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    def __init__(self, config):
        try:
            self.layers = self.build_from_config(config)
        except ValueError as ve:
            raise ve

    class LayerConfig(object):
        """A single layer configuration.

        Attributes:
            layer_type (str): The layer type.
            options (deep_networks.network.*Options): Options for the layer.
        """
        def __init__(self, layer_type):
            self.layer_type = layer_type

        class Conv3DOptions(object):
            """Options for a 3d conv layer.

            Attributes:
                num_filters (int): Number of convolutional filters to use.
                filter_size (int): Size of each filter.
                activation (str): Activation function to use.
            """
            def __init__(self, num_filters, filter_size, activation):
                self.num_filters = num_filters
                self.filter_size = filter_size
                self.activation = activation

    class NetworkConfigValidator(object):
        """Validate a dict based config.

        Attributes:
            config (object): A config to validate.
            errors (list): A list of errors found, if any.
            messages (dict): All potentially thrown error messages.

        Raises:
            ValueError: The reason why the config is invalid.
        """
        errors = list()
        messages = {
            "not_list_of_layers": "Config should contain a list of layer definitions, but was a {}."
        }

        def __init__(self, config):
            """Call methods required for validation.

            Args:
            config (object): The object to validate

            """
            self.config = config
            if (self.has_layers() and
                    self.has_valid_options()):
                pass
            else:
                raise ValueError(', '.join(self.errors))

        def has_layers(self):
            """Check to see if a config is a list of layers.

            Returns bool: Whether or not the config has layers.
            """
            config_type = type(self.config)
            if config_type is list:
                return True
            else:
                self.errors.append(self.messages["not_list_of_layers"].format(config_type))
                return False

        def has_valid_options(self):
            """Check to see that each layer has the required options.

            TODO: move this to LayerConfig, then can just validate by trying/failing

            Returns bool: Whether or not all layer objects are valid.
            """
            # TODO!!!
            return True

    def build_from_config(self, config):
        """Construct with a NetworkConfig from a dict based config object.

        Constructs NetworkConfigValidator to perform validation before building.

        Args:
            config (list): A list of dicts containing a representation of a network (TODO how to define?)

        """
        try:
            self.NetworkConfigValidator(config)
        except ValueError as ve:
            raise ve


