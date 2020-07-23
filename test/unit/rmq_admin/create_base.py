#!/usr/bin/python
# Classification (U)

"""Program:  create_base.py

    Description:  Unit testing of create_base in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/create_base.py

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

# Local
sys.path.append(os.getcwd())
import rmq_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__ -> Initialize configuration environment.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.user = "username"
        self.passwd = None
        self.host = "hostname"
        self.m_port = 15672


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_port_str -> Test with port passed as a string.
        test_create_base -> Test with no arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = CfgTest()
        self.results = "http://hostname:15672/api/"

    def test_port_str(self):

        """Function:  test_port_str

        Description:  Test with port passed as a string.

        Arguments:

        """

        self.cfg.m_port = "15672"

        self.assertEqual(rmq_admin.create_base(self.cfg), self.results)

    def test_create_base(self):

        """Function:  test_create_base

        Description:  Test create_base function.

        Arguments:

        """

        self.assertEqual(rmq_admin.create_base(self.cfg), self.results)


if __name__ == "__main__":
    unittest.main()
