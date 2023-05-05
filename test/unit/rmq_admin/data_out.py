# Classification (U)

"""Program:  data_out.py

    Description:  Unit testing of data_out in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/data_out.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import json
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

    with open(fname) as f_hldr:
        data = sum(1 for _ in f_hldr)

    return data


class ArgParser(object):

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

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class MailTest(object):

    """Class:  MailTest

    Description:  Class which is a representation of an email.

    Methods:
        __init__
        add_2_msg
        send_mail

    """

    def __init__(self, toline, subj=None, frm=None, msg_type=None):

        """Method:  __init__

        Description:  Initialization of an instance of the Mail class.

        Arguments:

        """

        if isinstance(subj, list):
            subj = list(subj)

        if isinstance(toline, list):
            self.toline = list(toline)

        else:
            self.toline = toline

        self.subj = subj
        self.frm = frm
        self.msg_type = msg_type
        self.msg = ""

    def add_2_msg(self, txt_ln=None):

        """Method:  add_2_msg

        Description:  Add text to text string if data is present.

        Arguments:

        """

        if txt_ln:

            if isinstance(txt_ln, str):
                self.msg = self.msg + txt_ln

            else:
                self.msg = self.msg + json.dumps(txt_ln)

    def send_mail(self, txt_ln=None):

        """Method:  send_mail

        Description:  Send email.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_no_err_verb_all2
        test_no_err_verb_all
        test_no_err_all2
        test_no_err_all
        test_no_err_verb_std_file
        test_no_err_std_file2
        test_no_err_std_file
        test_no_err_verb_file_mail2
        test_no_err_verb_file_mail
        test_no_err_file_mail2
        test_no_err_file_mail
        test_no_err_verb_std_mail2
        test_no_err_verb_std_mail
        test_no_err_std_mail2
        test_no_err_std_mail
        test_err_verb_mail
        test_err_mail
        test_no_err_verb_mail
        test_no_err_mail
        test_append_verb_file
        test_append_file
        test_err_verb_file
        test_err_file
        test_no_err_verb_file
        test_no_err_file
        test_errors_suppr
        test_no_err_verb_suppr
        test_errors_verbose
        test_errors
        test_no_errors_verbose
        test_no_errors
        tearDown

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.mail = MailTest("toaddr")

        self.data = {"Status": "ok"}
        self.file = "test/unit/rmq_admin/tmp/data_out_file.txt"
        self.args_array = {}
        self.args_array2 = {"-z": True}
        self.args_array3 = {"-w": True}
        self.args_array4 = {"-w": True, "-z": True}
        self.args_array5 = {"-o": self.file, "-z": True}
        self.args_array6 = {"-o": self.file, "-w": True, "-z": True}
        self.args_array7 = {"-o": self.file, "-a": True, "-z": True}
        self.args_array8 = {"-o": self.file, "-a": True, "-w": True,
                            "-z": True}
        self.args_array9 = {"-t": "toaddr", "-z": True}
        self.args_array10 = {"-t": "toaddr", "-w": True, "-z": True}
        self.args_array11 = {"-t": "toaddr"}
        self.args_array12 = {"-t": "toaddr", "-w": True}
        self.args_array13 = {"-t": "toaddr", "-o": self.file, "-z": True}
        self.args_array14 = {"-t": "toaddr", "-o": self.file, "-w": True,
                             "-z": True}
        self.args_array15 = {"-o": self.file}
        self.args_array16 = {"-o": self.file, "-w": True}
        self.args_array17 = {"-t": "toaddr", "-o": self.file}
        self.args_array18 = {"-t": "toaddr", "-o": self.file, "-w": True}

        self.results = '{"Status": "ok"}'
        self.results2 = ""

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_all2(self, mock_mail):

        """Function:  test_no_err_verb_all2

        Description:  Test with no errors detected - all - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array18

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_all(self, mock_mail):

        """Function:  test_no_err_verb_all

        Description:  Test with no errors detected - all - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array18

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, self.args)

        self.assertEqual(linecnt(self.file), 3)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_all2(self, mock_mail):

        """Function:  test_no_err_all2

        Description:  Test with no errors detected - all outputs.

        Arguments:

        """

        self.args.args_array = self.args_array17

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_all(self, mock_mail):

        """Function:  test_no_err_all

        Description:  Test with no errors detected - all outputs.

        Arguments:

        """

        self.args.args_array = self.args_array17

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, self.args)

        self.assertTrue(os.path.isfile(self.file))

    def test_no_err_verb_std_file(self):

        """Function:  test_no_err_verb_std_file

        Description:  Test no erro to std out & file - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array16

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, self.args))

        self.assertEqual(linecnt(self.file), 3)

    def test_no_err_std_file2(self):

        """Function:  test_no_err_std_file2

        Description:  Test with no errors to standard out and file.

        Arguments:

        """

        self.args.args_array = self.args_array15

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, self.args))

    def test_no_err_std_file(self):

        """Function:  test_no_err_std_file

        Description:  Test with no errors to standard out and file.

        Arguments:

        """

        self.args.args_array = self.args_array15

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, self.args)

        self.assertTrue(os.path.isfile(self.file))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_file_mail2(self, mock_mail):

        """Function:  test_no_err_verb_file_mail2

        Description:  Test with no errors detected - file and mail - verbose.

        Arguments:

        """

        mock_mail.return_value = self.mail

        self.args.args_array = self.args_array14

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(linecnt(self.file), 3)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_file_mail(self, mock_mail):

        """Function:  test_no_err_verb_file_mail

        Description:  Test with no errors detected - file and mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array14

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_file_mail2(self, mock_mail):

        """Function:  test_no_err_file_mail2

        Description:  Test with no errors detected - file and mail.

        Arguments:

        """

        self.args.args_array = self.args_array13

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, self.args)

        self.assertTrue(os.path.isfile(self.file))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_file_mail(self, mock_mail):

        """Function:  test_no_err_file_mail

        Description:  Test with no errors detected - file and mail.

        Arguments:

        """

        self.args.args_array = self.args_array13

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_std_mail2(self, mock_mail):

        """Function:  test_no_err_verb_std_mail2

        Description:  Test no erro to std out & mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array12

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, self.args))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_std_mail(self, mock_mail):

        """Function:  test_no_err_verb_std_mail

        Description:  Test no erro to std out & mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array12

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_std_mail2(self, mock_mail):

        """Function:  test_no_err_std_mail2

        Description:  Test with no errors to standard out and mail.

        Arguments:

        """

        self.args.args_array = self.args_array11

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_std_mail(self, mock_mail):

        """Function:  test_no_err_std_mail

        Description:  Test with no errors to standard out and mail.

        Arguments:

        """

        self.args.args_array = self.args_array11

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, self.args))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_err_verb_mail(self, mock_mail):

        """Function:  test_err_verb_mail

        Description:  Test with error for mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array10

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_err_mail(self, mock_mail):

        """Function:  test_err_mail

        Description:  Test with error for mail.

        Arguments:

        """

        self.args.args_array = self.args_array9

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_mail(self, mock_mail):

        """Function:  test_no_err_verb_mail

        Description:  Test with no error for mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array10

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_mail(self, mock_mail):

        """Function:  test_no_err_mail

        Description:  Test with no error for mail.

        Arguments:

        """

        self.args.args_array = self.args_array9

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(self.mail.msg, self.results)

    def test_append_verb_file(self):

        """Function:  test_append_verb_file

        Description:  Test with append file and verbose.

        Arguments:

        """

        self.args.args_array = self.args_array8

        rmq_admin.data_out(self.data, self.args)
        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(linecnt(self.file), 6)

    def test_append_file(self):

        """Function:  test_append_file

        Description:  Test with errors detected - append file.

        Arguments:

        """

        self.args.args_array = self.args_array7

        rmq_admin.data_out(self.data, self.args)
        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(linecnt(self.file), 6)

    def test_err_verb_file(self):

        """Function:  test_err_verb_file

        Description:  Test with errors detected - write file - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array6

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(linecnt(self.file), 3)

    def test_err_file(self):

        """Function:  test_err_file

        Description:  Test with errors detected - write file.

        Arguments:

        """

        self.args.args_array = self.args_array5

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(linecnt(self.file), 3)

    def test_no_err_verb_file(self):

        """Function:  test_no_err_verb_file

        Description:  Test with no errors detected - write file - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array6

        rmq_admin.data_out(self.data, self.args)

        self.assertEqual(linecnt(self.file), 3)

    def test_no_err_file(self):

        """Function:  test_no_err_file

        Description:  Test with no errors detected - write file.

        Arguments:

        """

        self.args.args_array = self.args_array5

        rmq_admin.data_out(self.data, self.args)

        self.assertTrue(os.path.isfile(self.file))

    def test_errors_suppr(self):

        """Function:  test_errors_suppr

        Description:  Test with errors detected - suppressed.

        Arguments:

        """

        self.args.args_array = self.args_array2

        self.assertFalse(rmq_admin.data_out(self.data, self.args))

    def test_no_err_verb_suppr(self):

        """Function:  test_no_err_verb_suppr

        Description:  Test with no errors detected - verbose mode - suppressed.

        Arguments:

        """

        self.args.args_array = self.args_array4

        self.assertFalse(rmq_admin.data_out(self.data, self.args))

    def test_errors_verbose(self):

        """Function:  test_errors_verbose

        Description:  Test with errors detected - verbose mode.

        Arguments:

        """

        self.args.args_array = self.args_array3

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, self.args))

    def test_errors(self):

        """Function:  test_errors

        Description:  Test with errors detected.

        Arguments:

        """

        self.args.args_array = self.args_array

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, self.args))

    def test_no_errors_verbose(self):

        """Function:  test_no_errors_verbose

        Description:  Test with no errors detected - verbose mode.

        Arguments:

        """

        self.args.args_array = self.args_array3

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, self.args))

    def test_no_errors(self):

        """Function:  test_no_errors

        Description:  Test with no errors detected.

        Arguments:

        """

        self.args.args_array = self.args_array

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, self.args))

    def tearDown(self):

        """Function:  tearDown

        Description:  Cleanup of unit testing.

        Arguments:

        """

        if os.path.isfile(self.file):
            os.remove(self.file)


if __name__ == "__main__":
    unittest.main()
