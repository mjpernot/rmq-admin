#!/usr/bin/python
# Classification (U)

"""Program:  print_list.py

    Description:  Unit testing of print_list in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/print_list.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_mode_a_passed -> Test with file mode of append passing mode.
        test_mode_w_default -> Test file mode overwrite using default setting.
        test_write_file2 -> Test with writing multiple lines to file.
        test_write_file -> Test with writing to file.
        test_std_out2 -> Test with printing multiple lines to standard out.
        test_std_out -> Test with printing to standard out.
        tearDown -> Cleanup of testing environment.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.file = "test/unit/rmq_admin/tmp/outfile.txt"
        self.mode = "a"
        self.mode2 = "w"
        self.data = ["First line of data"]
        self.data2 = ["First line of data", "Second line of data"]

    def test_mode_a_passed(self):

        """Function:  test_mode_a_passed

        Description:  Test with file mode of append passing mode.

        Arguments:

        """

        rmq_admin.print_list(self.data2, ofile=self.file, mode=self.mode)
        rmq_admin.print_list(self.data2, ofile=self.file, mode=self.mode)

        self.assertEqual(sum(1 for line in open(self.file)), 4)

    def test_mode_w_passed(self):

        """Function:  test_mode_w_passed

        Description:  Test with file mode of overwrite passing mode.

        Arguments:

        """

        rmq_admin.print_list(self.data2, ofile=self.file, mode=self.mode2)
        rmq_admin.print_list(self.data2, ofile=self.file, mode=self.mode2)

        self.assertEqual(sum(1 for line in open(self.file)), 2)

    def test_mode_w_default(self):

        """Function:  test_mode_w_default

        Description:  Test with file mode of overwrite using default setting.

        Arguments:

        """

        rmq_admin.print_list(self.data2, ofile=self.file)
        rmq_admin.print_list(self.data2, ofile=self.file)

        self.assertEqual(sum(1 for line in open(self.file)), 2)

    def test_write_file2(self):

        """Function:  test_write_file2

        Description:  Test with writing multiple lines to file.

        Arguments:

        """

        rmq_admin.print_list(self.data2, ofile=self.file)

        self.assertEqual(sum(1 for line in open(self.file)), 2)

    def test_write_file(self):

        """Function:  test_write_file

        Description:  Test with writing to file.

        Arguments:

        """

        rmq_admin.print_list(self.data, ofile=self.file)

        self.assertTrue(os.path.isfile(self.file))

    def test_std_out2(self):

        """Function:  test_std_out2

        Description:  Test with printing multiple lines to standard out.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.print_list(self.data2))

    def test_std_out(self):

        """Function:  test_std_out

        Description:  Test with printing to standard out.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.print_list(self.data))

    def tearDown(self):

        """Function:  tearDown

        Description:  Cleanup of unit testing.

        Arguments:

        """

        if os.path.isfile(self.file):
            os.remove(self.file)


if __name__ == "__main__":
    unittest.main()
