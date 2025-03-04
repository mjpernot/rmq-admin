# Classification (U)

"""Program:  generic_call.py

    Description:  Unit testing of generic_call in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/generic_call.py

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


class ArgParser():                                      # pylint:disable=R0903

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
        test_email_subject
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
        self.data = {}

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_nodes")
    def test_email_subject(self, mock_rmq):

        """Function:  test_email_subject

        Description:  Test with email subject.

        Arguments:

        """

        mock_rmq.return_value = self.data

        self.assertFalse(
            rmq_admin.generic_call(
                self.args, rmq=self.rmq, method=self.rmq.list_nodes,
                subj="Email_Subject_Line"))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_nodes")
    def test_default(self, mock_rmq):

        """Function:  test_default

        Description:  Test with default settings.

        Arguments:

        """

        mock_rmq.return_value = self.data

        self.assertFalse(
            rmq_admin.generic_call(
                self.args, rmq=self.rmq, method=self.rmq.list_nodes))


if __name__ == "__main__":
    unittest.main()
