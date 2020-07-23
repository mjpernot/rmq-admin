#!/usr/bin/python
# Classification (U)

"""Program:  fill_body.py

    Description:  Unit testing of fill_body in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/fill_body.py

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

# Local
sys.path.append(os.getcwd())
import rmq_admin
import version

__version__ = version.__version__


class MailTest(object):

    """Class:  MailTest

    Description:  Class which is a representation of an email.

    Methods:
        __init__ -> Class instance initilization.
        add_2_msg -> Add text to text string if data is present.

    """

    def __init__(self, to, subj=None, frm=None, msg_type=None):

        """Method:  __init__

        Description:  Initialization of an instance of the Mail class.

        Arguments:
            (input) to -> To email address.
            (input) subj -> Subject line of mail.
            (input) msg_type -> Type of email being sent.
            (input) frm -> From email address.
            (input) host -> 'localhost' or IP.
            (input) host_name -> Host name of server.

        """

        if isinstance(subj, list):
            subj = list(subj)

        if isinstance(to, list):
            self.to = list(to)

        else:
            self.to = to

        self.subj = subj
        self.frm = frm
        self.msg_type = msg_type
        self.msg = ""

    def add_2_msg(self, txt_ln=None):

        """Method:  add_2_msg

        Description:  Add text to text string if data is present.

        Arguments:
            (input) txt_ln -> Line of text to add to message.

        """

        if txt_ln:

            if isinstance(txt_ln, str):
                self.msg = self.msg + txt_ln

            else:
                self.msg = self.msg + json.dumps(txt_ln)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_multiple_lines -> Test with multiple lines from list.
        test_single_line -> Test with single line from list.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = MailTest("toaddr")
        self.data = ["First line of data"]
        self.data2 = ["First line of data", "Second line of data"]
        self.results = "First line of data"
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
