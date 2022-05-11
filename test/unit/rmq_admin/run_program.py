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
import version

__version__ = version.__version__


def node_health(base_url, cfg, args_array):

    """Function:  node_health

    Description:  node_health function.

    Arguments:

    """

    status = True

    if base_url and cfg and args_array:
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
        test_func_call
        test_no_func

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.cfg = CfgTest()
        self.func_dict = {"-N": node_health}
        self.rmq = "RMQ_Class_Instance"

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin")
    @mock.patch("rmq_admin.gen_libs.load_module")
    def test_func_call(self, mock_cfg, mock_rmq):

        """Function:  test_func_call

        Description:  Test with function called.

        Arguments:

        """

        self.args.args_array["-N"] = True

        mock_cfg.return_value = self.cfg
        mock_rmq.return_value = self.rmq

        self.assertFalse(rmq_admin.run_program(self.args, self.func_dict))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin")
    @mock.patch("rmq_admin.gen_libs.load_module")
    def test_no_func(self, mock_cfg, mock_rmq):

        """Function:  test_no_func

        Description:  Test with no functions selected.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        mock_rmq.return_value = self.rmq

        self.assertFalse(rmq_admin.run_program(self.args, self.func_dict))


if __name__ == "__main__":
    unittest.main()
