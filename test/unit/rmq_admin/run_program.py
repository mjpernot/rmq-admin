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
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import rmq_admin                                # pylint:disable=E0401,C0413
import rabbit_lib.rabbitmq_class as rmqcls  # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

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


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_args_keys
        get_val
        arg_exist

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.args_array = {"-c": "rabbitmq", "-d": "config"}

    def get_args_keys(self):

        """Method:  get_args_keys

        Description:  Method stub holder for gen_class.ArgParser.get_args_keys.

        Arguments:

        """

        return list(self.args_array.keys())

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)

    def arg_exist(self, arg):

        """Method:  arg_exist

        Description:  Method stub holder for gen_class.ArgParser.arg_exist.

        Arguments:

        """

        return arg in self.args_array


class CfgTest():                                        # pylint:disable=R0903

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
        self.rmq = rmqcls.RabbitMQAdmin(self.cfg.user, self.cfg.japd)

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
