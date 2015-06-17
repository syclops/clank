# Clank Configuration Manager
# Author: Steve Matsumoto
# This code is released under the GNU LGPL Version 3.

"""
:mod:`conf` --- Clank Configuration Manager
===========================================
"""

import configparser

class Config(object):
    """
    Representation of the Clank session configuration.

    :ivar config: the configuration parser.
    :type config: `configparser.ConfigParser`
    """

    def __init__(self, configFile=None):
        """
        Constructor.

        :param configFile: the name of the configuration file
        :type configFile: str
        """
        if configFile is not None:
            with open(configFile, 'r') as f:
                contents = f.read()
            self.config = configparser.ConfigParser()
            self.config.read_string(contents)
        else:
            self.config = None
