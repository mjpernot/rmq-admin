# Classification (U)

"""Program:  node_health.py

    Description:  Unit testing of node_health in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/node_health.py

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


def linecnt(fname):

    """Function:  linecnt

    Description:  Count number of lines in a file.

    Arguments:

    """

    with open(fname, mode="r", encoding="UTF-8") as f_hldr:
        data = sum(1 for _ in f_hldr)

    return data


class ArgParser():

    """Class:  ArgParser

    Description:  Class stub holder for gen_class.ArgParser class.

    Methods:
        __init__
        get_val
        arg_exist

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
        test_errors_suppr
        test_no_err_verb_suppr
        test_errors_verbose
        test_errors
        test_no_errors_verbose
        test_no_errors

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.cfg = CfgTest()
        self.rmq = rmqcls.RabbitMQAdmin(self.cfg.user, self.cfg.japd)

        self.data = {'status': 'ok'}
        self.data2 = {'status': 'failed', 'reason': 'reason for failure'}
        self.args_array = {}
        self.args_array2 = {"-z": True}
        self.args_array3 = {"-w": True}
        self.args_array4 = {"-w": True, "-z": True}

        self.date = "2020-07-24"
        self.time = "10:20:10"

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_errors_suppr(self, mock_get):

        """Function:  test_errors_suppr

        Description:  Test with errors detected - suppressed.

        Arguments:

        """

        self.args.args_array = self.args_array2

        mock_get.return_value = self.data2

        self.assertFalse(rmq_admin.node_health(self.args, rmq=self.rmq))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_suppr(self, mock_get):

        """Function:  test_no_err_verb_suppr

        Description:  Test with no errors detected - verbose mode - suppressed.

        Arguments:

        """

        self.args.args_array = self.args_array4

        mock_get.return_value = self.data

        self.assertFalse(rmq_admin.node_health(self.args, rmq=self.rmq))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_errors_verbose(self, mock_get):

        """Function:  test_errors_verbose

        Description:  Test with errors detected - verbose mode.

        Arguments:

        """

        self.args.args_array = self.args_array3

        mock_get.return_value = self.data2

        self.assertFalse(rmq_admin.node_health(self.args, rmq=self.rmq))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_errors(self, mock_get):

        """Function:  test_errors

        Description:  Test with errors detected.

        Arguments:

        """

        self.args.args_array = self.args_array

        mock_get.return_value = self.data2

        self.assertFalse(rmq_admin.node_health(self.args, rmq=self.rmq))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_errors_verbose(self, mock_get):

        """Function:  test_no_errors_verbose

        Description:  Test with no errors detected - verbose mode.

        Arguments:

        """

        self.args.args_array = self.args_array3

        mock_get.return_value = self.data

        self.assertFalse(rmq_admin.node_health(self.args, rmq=self.rmq))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_errors(self, mock_get):

        """Function:  test_no_errors

        Description:  Test with no errors detected.

        Arguments:

        """

        self.args.args_array = self.args_array

        mock_get.return_value = self.data

        self.assertFalse(rmq_admin.node_health(self.args, rmq=self.rmq))


if __name__ == "__main__":
    unittest.main()
