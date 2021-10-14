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

        http = "http"
        self.cfg = CfgTest()
        self.func_dict = {"-N": node_health}
        self.args_array = {"-c": "rabbitmq", "-d": "config"}
        self.args_array2 = {"-c": "rabbitmq", "-d": "config", "-N": True}
        self.base_url = \
            http + "://" + self.cfg.host + ":" + str(self.cfg.m_port) + "/api/"

    @mock.patch("rmq_admin.create_base")
    @mock.patch("rmq_admin.gen_libs.load_module")
    def test_func_call(self, mock_cfg, mock_base):

        """Function:  test_func_call

        Description:  Test with function called.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        mock_base.return_value = self.base_url

        self.assertFalse(rmq_admin.run_program(self.args_array2,
                                               self.func_dict))

    @mock.patch("rmq_admin.create_base")
    @mock.patch("rmq_admin.gen_libs.load_module")
    def test_no_func(self, mock_cfg, mock_base):

        """Function:  test_no_func

        Description:  Test with no functions selected.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        mock_base.return_value = self.base_url

        self.assertFalse(rmq_admin.run_program(self.args_array,
                                               self.func_dict))


if __name__ == "__main__":
    unittest.main()
