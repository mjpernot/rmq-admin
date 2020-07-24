#!/usr/bin/python
# Classification (U)

"""Program:  node_health.py

    Description:  Unit testing of node_health in rmq_admin.py.

    Usage:
        test/integration/rmq_admin/node_health.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_no_err_verb_mail -> Test with no error for mail - verbose.
        test_no_err_mail -> Test with no error for mail.
        test_append_verb_file -> Test with append file and verbose.
        test_no_err_verb_file -> Test no errors detected: write file, verbose.
        test_no_err_file -> Test with no errors detected - write file.
        test_no_err_verb_suppr -> Test no errors detected: verbose, suppressed.
        test_no_errors_verbose -> Test with no errors detected - verbose mode.
        test_no_errors -> Test with no errors detected.
        tearDown -> Cleanup of testing environment.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mod = "rabbitmq"
        self.dir = "test/integration/rmq_admin/config"
        self.file = "test/unit/rmq_admin/tmp/outfile.txt"
        self.cfg2 = gen_libs.load_module(self.mod, self.dir)
        self.base_url2 = \
            "http://" + self.cfg2.host + ":" + str(self.cfg2.m_port) + "/api/"
        self.args_array = {}
        self.args_array3 = {"-w": True}
        self.args_array4 = {"-w": True, "-z": True}
        self.args_array5 = {"-o": self.file, "-z": True}
        self.args_array6 = {"-o": self.file, "-w": True, "-z": True}
        self.args_array8 = {"-o": self.file, "-a": True, "-w": True,
                            "-z": True}
        self.args_array9 = {"-t": "toaddr", "-z": True}
        self.args_array10 = {"-t": "toaddr", "-w": True, "-z": True}

    @mock.patch("rmq_admin.gen_class.Mail.send_mail",
                mock.Mock(return_value=True))
    def test_no_err_verb_mail(self):

        """Function:  test_no_err_verb_mail

        Description:  Test with no error for mail - verbose.

        Arguments:

        """

        self.assertFalse(rmq_admin.node_health(self.base_url2, self.cfg2,
                                               self.args_array10))

    def test_no_err_mail(self):

        """Function:  test_no_err_mail

        Description:  Test with no error for mail.

        Arguments:

        """

        self.assertFalse(rmq_admin.node_health(self.base_url2, self.cfg2,
                                               self.args_array9))

    def test_append_verb_file(self):

        """Function:  test_append_verb_file

        Description:  Test with append file and verbose.

        Arguments:

        """

        rmq_admin.node_health(self.base_url2, self.cfg2, self.args_array8)
        rmq_admin.node_health(self.base_url2, self.cfg2, self.args_array8)

        self.assertEqual(sum(1 for line in open(self.file)), 6)

    def test_no_err_verb_file(self):

        """Function:  test_no_err_verb_file

        Description:  Test with no errors detected - write file - verbose.

        Arguments:

        """

        rmq_admin.node_health(self.base_url2, self.cfg2, self.args_array6)

        self.assertEqual(sum(1 for line in open(self.file)), 3)

    def test_no_err_file(self):

        """Function:  test_no_err_file

        Description:  Test with no errors detected - write file.

        Arguments:

        """

        rmq_admin.node_health(self.base_url2, self.cfg2, self.args_array5)

        self.assertFalse(os.path.isfile(self.file))

    def test_no_err_verb_suppr(self):

        """Function:  test_no_err_verb_suppr

        Description:  Test with no errors detected - verbose mode - suppressed.

        Arguments:

        """

        self.assertFalse(rmq_admin.node_health(self.base_url2, self.cfg2,
                                               self.args_array4))

    @mock.patch("rmq_admin.print_list", mock.Mock(return_value=True))
    def test_no_errors_verbose(self):

        """Function:  test_no_errors_verbose

        Description:  Test with no errors detected - verbose mode.

        Arguments:

        """

        self.assertFalse(rmq_admin.node_health(self.base_url2, self.cfg2,
                                               self.args_array3))

    def test_no_errors(self):

        """Function:  test_no_errors

        Description:  Test with no errors detected.

        Arguments:

        """

        self.assertFalse(rmq_admin.node_health(self.base_url2, self.cfg2,
                                               self.args_array))

    def tearDown(self):

        """Function:  tearDown

        Description:  Cleanup of unit testing.

        Arguments:

        """

        if os.path.isfile(self.file):
            os.remove(self.file)


if __name__ == "__main__":
    unittest.main()
