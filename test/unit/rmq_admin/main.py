#!/usr/bin/python
# Classification (U)

"""Program:  main.py

    Description:  Unit testing of main in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/main.py

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


class ProgramLock(object):

    """Class:  ProgramLock

    Description:  Class stub holder for gen_class.ProgramLock class.

    Methods:
        __init__

    """

    def __init__(self, cmdline, flavor):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmdline = cmdline
        self.flavor = flavor


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_help_true
        test_help_false
        test_arg_req_true
        test_arg_req_false
        test_arg_dir_true
        test_arg_dir_false
        test_arg_file_true
        test_arg_file_false
        test_arg_cond_req_false
        test_arg_cond_req_true
        test_run_program
        test_programlock_true
        test_programlock_false
        test_programlock_id

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args_array = {"-c": "rabbit", "-d": "config", "-N": True}
        self.args_array2 = {"-c": "rabbit", "-d": "config", "-N": True,
                            "-y": "Flavor"}
        self.proglock = ProgramLock(["cmdline"], "FlavorID")

    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_help_true(self, mock_arg, mock_help):

        """Function:  test_help_true

        Description:  Test help if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = True

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_help_false(self, mock_arg, mock_help):

        """Function:  test_help_false

        Description:  Test help if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_arg_req_true(self, mock_arg, mock_help):

        """Function:  test_arg_req_true

        Description:  Test arg_require if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = True

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_arg_req_false(self, mock_arg, mock_help):

        """Function:  test_arg_req_false

        Description:  Test arg_require if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_arg_dir_true(self, mock_arg, mock_help):

        """Function:  test_arg_dir_true

        Description:  Test arg_dir_chk_crt if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = True

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_arg_dir_false(self, mock_arg, mock_help):

        """Function:  test_arg_dir_false

        Description:  Test arg_dir_chk_crt if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_arg_file_true(self, mock_arg, mock_help):

        """Function:  test_arg_file_true

        Description:  Test arg_file_chk if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = True

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.run_program", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.gen_class.ProgramLock")
    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_arg_file_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_file_false

        Description:  Test arg_file_chk if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_cond_req.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.run_program", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.gen_class.ProgramLock")
    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_arg_cond_req_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_cond_req_false

        Description:  Test arg_cond_req if returns false.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_cond_req.return_value = False
        mock_lock.return_value = self.proglock

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.run_program", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.gen_class.ProgramLock")
    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_arg_cond_req_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_arg_cond_req_true

        Description:  Test arg_cond_req if returns true.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.run_program", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.gen_class.ProgramLock")
    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_run_program(self, mock_arg, mock_help, mock_lock):

        """Function:  test_run_program

        Description:  Test with run_program.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.run_program", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.gen_class.ProgramLock")
    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_programlock_true(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_true

        Description:  Test with ProgramLock returns True.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.run_program", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.gen_class.ProgramLock")
    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_programlock_false(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_false

        Description:  Test with ProgramLock returns False.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_lock.side_effect = \
            rmq_admin.gen_class.SingleInstanceException

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.main())

    @mock.patch("rmq_admin.run_program", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.gen_class.ProgramLock")
    @mock.patch("rmq_admin.gen_libs.help_func")
    @mock.patch("rmq_admin.arg_parser")
    def test_programlock_id(self, mock_arg, mock_help, mock_lock):

        """Function:  test_programlock_id

        Description:  Test ProgramLock with flavor ID.

        Arguments:

        """

        mock_arg.arg_parse2.return_value = self.args_array2
        mock_help.return_value = False
        mock_arg.arg_require.return_value = False
        mock_arg.arg_dir_chk_crt.return_value = False
        mock_arg.arg_file_chk.return_value = False
        mock_arg.arg_cond_req.return_value = True
        mock_lock.return_value = self.proglock

        self.assertFalse(rmq_admin.main())


if __name__ == "__main__":
    unittest.main()
