#!/usr/bin/python
# Classification (U)

"""Program:  list_queues.py

    Description:  Unit testing of list_queues in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/list_queues.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party
import json
import mock

# Local
sys.path.append(os.getcwd())
import rmq_admin
import lib.gen_libs as gen_libs
import rabbit_lib.rabbitmq_class as rabbitmq_class
import version

__version__ = version.__version__


class ArgParser(object):

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "rabbitmq", "-d": "config"}


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.user = "username"
        self.japd = None
        self.host = "hostname"
        self.m_port = 15672
        self.scheme = "https"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_default

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """


        self.args = ArgParser()
        self.cfg = CfgTest()
        self.rmq = rabbitmq_class.RabbitMQAdmin(self.cfg.user, self.cfg.japd)
        self.data = {}

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_queues")
    def test_default(self, mock_rmq):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_rmq.return_value = self.data

        self.assertFalse(rmq_admin.list_queues(self.rmq, self.args))


if __name__ == "__main__":
    unittest.main()
