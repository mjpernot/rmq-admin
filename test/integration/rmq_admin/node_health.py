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
import mock

# Local
sys.path.append(os.getcwd())
import rmq_admin
import lib.gen_libs as gen_libs
import version

__version__ = version.__version__


def linecnt(fname):

    """Function:  linecnt

    Description:  Count number of lines in a file.

    Arguments:

    """

    return sum(1 for _ in open(fname))


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_verb_std_file_mail
        test_verb_std_file
        test_verb_mail_file
        test_verb_std_mail
        test_no_err_verb_mail
        test_no_err_mail
        test_append_verb_file
        test_no_err_verb_file
        test_no_err_file
        test_no_err_verb_suppr
        test_no_errors_verbose
        test_no_errors
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.http = "http"
        self.mod = "rabbitmq"
        self.dir = "test/integration/rmq_admin/config"
        self.file = "test/unit/rmq_admin/tmp/outfile.txt"
        self.cfg2 = gen_libs.load_module(self.mod, self.dir)
        self.base_url2 = \
            self.http + "://" + self.cfg2.host + ":" + \
            str(self.cfg2.m_port) + "/api/"
        self.args_array = {}
        self.args_array2 = {"-t": "toaddr", "-w": True}
        self.args_array3 = {"-w": True}
        self.args_array4 = {"-w": True, "-z": True}
        self.args_array5 = {"-o": self.file, "-z": True}
        self.args_array6 = {"-o": self.file, "-w": True, "-z": True}
        self.args_array7 = {"-o": self.file, "-t": "toaddr", "-w": True,
                            "-z": True}
        self.args_array8 = {"-o": self.file, "-a": True, "-w": True,
                            "-z": True}
        self.args_array9 = {"-t": "toaddr", "-z": True}
        self.args_array10 = {"-t": "toaddr", "-w": True, "-z": True}
        self.args_array11 = {"-o": self.file, "-w": True}
        self.args_array12 = {"-t": "toaddr", "-o": self.file, "-w": True}

    @mock.patch("rmq_admin.gen_class.Mail.send_mail",
                mock.Mock(return_value=True))
    @mock.patch("rmq_admin.print_list", mock.Mock(return_value=True))
    def test_verb_std_file_mail(self):

        """Function:  test_verb_std_file_mail

        Description:  Test with std out, file and mail - verbose.

        Arguments:

        """

        self.assertFalse(rmq_admin.node_health(self.base_url2, self.cfg2,
                                               self.args_array12))

    @mock.patch("rmq_admin.print_list", mock.Mock(return_value=True))
    def test_verb_std_file(self):

        """Function:  test_verb_std_file

        Description:  Test with strandard out and file - verbose.

        Arguments:

        """

        self.assertFalse(rmq_admin.node_health(self.base_url2, self.cfg2,
                                               self.args_array11))

    @mock.patch("rmq_admin.gen_class.Mail.send_mail",
                mock.Mock(return_value=True))
    def test_verb_mail_file(self):

        """Function:  test_verb_mail_file

        Description:  Test with no error for mail - verbose.

        Arguments:

        """

        self.assertFalse(rmq_admin.node_health(self.base_url2, self.cfg2,
                                               self.args_array7))

    @mock.patch("rmq_admin.gen_class.Mail.send_mail",
                mock.Mock(return_value=True))
    @mock.patch("rmq_admin.print_list", mock.Mock(return_value=True))
    def test_verb_std_mail(self):

        """Function:  test_verb_std_mail

        Description:  Test with standard out and mail - verbose.

        Arguments:

        """

        self.assertFalse(rmq_admin.node_health(self.base_url2, self.cfg2,
                                               self.args_array2))

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

        self.assertEqual(linecnt(self.file), 6)

    def test_no_err_verb_file(self):

        """Function:  test_no_err_verb_file

        Description:  Test with no errors detected - write file - verbose.

        Arguments:

        """

        rmq_admin.node_health(self.base_url2, self.cfg2, self.args_array6)

        self.assertEqual(linecnt(self.file), 3)

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
