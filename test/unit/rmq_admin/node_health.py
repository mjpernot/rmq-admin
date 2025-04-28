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
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
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

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.cfg = CfgTest()
        self.rmq = rmqcls.RabbitMQAdmin(self.cfg.user, self.cfg.japd)
        self.data = {'status': 'ok'}
        self.data2 = {'status': 'failed', 'reason': 'reason for failure'}
        self.data_config = {"report": False}
        self.data_config2 = {"report": False, "suppress": True}
        self.data_config3 = {"report": True}
        self.data_config4 = {"report": True, "suppress": True}

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_errors_suppr(self, mock_get):

        """Function:  test_errors_suppr

        Description:  Test with errors detected - suppressed.

        Arguments:

        """

        mock_get.return_value = self.data2

        self.assertFalse(
            rmq_admin.node_health(self.data_config2, self.dtg, rmq=self.rmq))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_suppr(self, mock_get):

        """Function:  test_no_err_verb_suppr

        Description:  Test with no errors detected - verbose mode - suppressed.

        Arguments:

        """

        mock_get.return_value = self.data

        self.assertFalse(
            rmq_admin.node_health(self.data_config4, self.dtg, rmq=self.rmq))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_errors_verbose(self, mock_get):

        """Function:  test_errors_verbose

        Description:  Test with errors detected - verbose mode.

        Arguments:

        """

        mock_get.return_value = self.data2

        self.assertFalse(
            rmq_admin.node_health(self.data_config3, self.dtg, rmq=self.rmq))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_errors(self, mock_get):

        """Function:  test_errors

        Description:  Test with errors detected.

        Arguments:

        """

        mock_get.return_value = self.data2

        self.assertFalse(
            rmq_admin.node_health(self.data_config, self.dtg, rmq=self.rmq))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_errors_verbose(self, mock_get):

        """Function:  test_no_errors_verbose

        Description:  Test with no errors detected - verbose mode.

        Arguments:

        """

        mock_get.return_value = self.data

        self.assertFalse(
            rmq_admin.node_health(self.data_config3, self.dtg, rmq=self.rmq))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_errors(self, mock_get):

        """Function:  test_no_errors

        Description:  Test with no errors detected.

        Arguments:

        """

        mock_get.return_value = self.data

        self.assertFalse(
            rmq_admin.node_health(self.data_config, self.dtg, rmq=self.rmq))


if __name__ == "__main__":
    unittest.main()
