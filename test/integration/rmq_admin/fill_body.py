#!/usr/bin/python
# Classification (U)

"""Program:  fill_body.py

    Description:  Unit testing of fill_body in rmq_admin.py.

    Usage:
        test/integration/rmq_admin/fill_body.py

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
import lib.gen_class as gen_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_multiple_lines
        test_single_line

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = gen_class.setup_mail("toaddr")
        self.line = "First line of data"
        self.data = [self.line]
        self.data2 = [self.line, "Second line of data"]
        self.results = self.line
        self.results2 = "First line of dataSecond line of data"

    def test_multiple_lines(self):

        """Function:  test_multiple_lines

        Description:  Test with multiple lines from list.

        Arguments:

        """

        rmq_admin.fill_body(self.mail, self.data2)

        self.assertEqual(self.mail.msg, self.results2)

    def test_single_line(self):

        """Function:  test_single_line

        Description:  Test with single line from list.

        Arguments:

        """

        rmq_admin.fill_body(self.mail, self.data)

        self.assertEqual(self.mail.msg, self.results)


if __name__ == "__main__":
    unittest.main()
