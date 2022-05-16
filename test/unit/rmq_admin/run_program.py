#!/usr/bin/python
# Classification (U)

"""Program:  run_program.py

    Description:  Unit testing of run_program in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/run_program.py

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
import mock

# Local
sys.path.append(os.getcwd())
import rmq_admin
import rabbit_lib.rabbitmq_class as rabbitmq_class
import version

__version__ = version.__version__


def node_health(rmq, args):

    """Function:  node_health

    Description:  node_health function.

    Arguments:

    """

    status = True

    if rmq and args:
        status = True

    return status


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

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


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
        test_generic_call
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

    @mock.patch("rmq_admin.generic_call", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin")
    @mock.patch("rmq_admin.gen_libs.load_module")
    def test_generic_call(self, mock_cfg, mock_rmq):

        """Function:  test_generic_call

        Description:  Test with generic_call call.

        Arguments:

        """

        self.args.args_array["-M"] = True

        mock_cfg.return_value = self.cfg
        mock_rmq.return_value = self.rmq

        self.assertFalse(rmq_admin.run_program(self.args))

    @mock.patch("rmq_admin.node_health", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin")
    @mock.patch("rmq_admin.gen_libs.load_module")
    def test_default(self, mock_cfg, mock_rmq):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        self.args.args_array["-N"] = True

        mock_cfg.return_value = self.cfg
        mock_rmq.return_value = self.rmq

        self.assertFalse(rmq_admin.run_program(self.args))


if __name__ == "__main__":
    unittest.main()
