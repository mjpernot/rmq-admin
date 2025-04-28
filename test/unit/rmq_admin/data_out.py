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
import rmq_admin                                # pylint:disable=E0401,C0413
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


def linecnt(fname):

    """Function:  linecnt

    Description:  Count number of lines in a file.

    Arguments:

    """

    with open(fname, mode="r", encoding="UTF-8") as f_hldr:
        data = sum(1 for _ in f_hldr)

    return data


class Mail():

    """Class:  Mail

    Description:  Class which is a representation of the gen_class.Mail class.

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


class Mail2():

    """Class:  Mail2

    Description:  Class which is a representation of the gen_class.Mail2 class.

    Methods:
        __init__
        add_attachment
        send_mail

    """

    def __init__(self, subject, toaddrs, fromaddr=None):

        """Method:  __init__

        Description:  Initialization of an instance of the Mail2 class.

        Arguments:

        """

        self.msg = {}
        # Dictionary of file types/extensions and their associated MIME types
        self.ftypes = {
            "plain": "plain", "text": "plain", "sh": "x-sh", "x-sh": "x-sh",
            "tar": "x-tar", "x-tar": "x-tar", "pdf": "pdf", "json": "json",
            "gz": "gzip", "gzip": "gzip"}
        self.subj = " ".join(subject) if isinstance(subject, list) else subject
        self.toaddrs = ",".join(
            toaddrs) if isinstance(toaddrs, list) else toaddrs
        self.fromaddr = fromaddr if fromaddr else "username@hostname"
        self.msg["From"] = self.fromaddr
        self.msg["To"] = self.toaddrs
        self.msg["Subject"] = self.subj
        self.fname = None
        self.data = None
        self.host = None

    def add_attachment(self, fname, ftype, data):

        """Method:  add_attachment

        Description:  Converts the file data into base64 format and attaches
            the data and filename to the email.

        Arguments:

        """

        ftype = self.ftypes[ftype] if ftype in self.ftypes else None
        self.fname = fname
        self.data = data

    def send_mail(self, host="localhost"):

        """Method:  send_mail

        Description:  Send email.

        Arguments:

        """

        self.host = host


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

        self.mail = Mail("toaddr")
        self.mail2 = Mail2("subject", "toaddr")

        self.data = {"Status": "ok"}
        self.file = "test/unit/rmq_admin/tmp/data_out_file.txt"
        base_data_config = {
            "indent": None, "to_addr": None, "attach": None, "outfile": None,
            "use_pprint": None, "suppress": None, "use_pprint": None}
        self.data_config = dict(base_data_config)
        self.data_config2 = dict(base_data_config)
        self.data_config2["suppress"] = True
        self.data_config3 = dict(base_data_config)
        self.data_config3["report"] = True
        self.data_config4 = dict(base_data_config)
        self.data_config4["report"] = True
        self.data_config4["suppress"] = True
        self.data_config5 = dict(base_data_config)
        self.data_config5["outfile"] = self.file
        self.data_config5["suppress"] = True
        self.data_config6 = dict(base_data_config)
        self.data_config6["outfile"] = self.file
        self.data_config6["report"] = True
        self.data_config6["suppress"] = True
        self.data_config7 = dict(base_data_config)
        self.data_config7["outfile"] = self.file
        self.data_config7["mode"] = "a"
        self.data_config7["suppress"] = True
        self.data_config8 = dict(base_data_config)
        self.data_config8["outfile"] = self.file
        self.data_config8["mode"] = "a"
        self.data_config8["report"] = True
        self.data_config8["suppress"] = True
        self.data_config9 = dict(base_data_config)
        self.data_config9["to_addr"] = "toaddr"
        self.data_config9["suppress"] = True
        self.data_config10 = dict(base_data_config)
        self.data_config10["to_addr"] = "toaddr"
        self.data_config10["report"] = True
        self.data_config10["suppress"] = True
        self.data_config11 = dict(base_data_config)
        self.data_config11["to_addr"] = "toaddr"
        self.data_config12 = dict(base_data_config)
        self.data_config12["to_addr"] = "toaddr"
        self.data_config12["report"] = True
        self.data_config13 = dict(base_data_config)
        self.data_config13["to_addr"] = "toaddr"
        self.data_config13["outfile"] = self.file
        self.data_config13["suppress"] = True
        self.data_config14 = dict(base_data_config)
        self.data_config14["to_addr"] = "toaddr"
        self.data_config14["outfile"] = self.file
        self.data_config14["report"] = True
        self.data_config14["suppress"] = True
        self.data_config15 = dict(base_data_config)
        self.data_config15["outfile"] = self.file
        self.data_config16 = dict(base_data_config)
        self.data_config16["outfile"] = self.file
        self.data_config16["report"] = True
        self.data_config17 = dict(base_data_config)
        self.data_config17["to_addr"] = "toaddr"
        self.data_config17["outfile"] = self.file
        self.data_config18 = dict(base_data_config)
        self.data_config18["to_addr"] = "toaddr"
        self.data_config18["outfile"] = self.file
        self.data_config18["report"] = True

        self.results = '{"Status": "ok"}'
        self.results2 = ""

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_all2(self, mock_mail):

        """Function:  test_no_err_verb_all2

        Description:  Test with no errors detected - all - verbose.

        Arguments:

        """

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, **self.data_config18)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_all(self, mock_mail):

        """Function:  test_no_err_verb_all

        Description:  Test with no errors detected - all - verbose.

        Arguments:

        """

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, **self.data_config18)

        self.assertEqual(linecnt(self.file), 1)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_all2(self, mock_mail):

        """Function:  test_no_err_all2

        Description:  Test with no errors detected - all outputs.

        Arguments:

        """

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, **self.data_config17)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_all(self, mock_mail):

        """Function:  test_no_err_all

        Description:  Test with no errors detected - all outputs.

        Arguments:

        """

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, **self.data_config17)

        self.assertTrue(os.path.isfile(self.file))

    def test_no_err_verb_std_file(self):

        """Function:  test_no_err_verb_std_file

        Description:  Test no erro to std out & file - verbose.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.data_out(self.data, **self.data_config16))

        self.assertEqual(linecnt(self.file), 1)

    def test_no_err_std_file2(self):

        """Function:  test_no_err_std_file2

        Description:  Test with no errors to standard out and file.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.data_out(self.data, **self.data_config15))

    def test_no_err_std_file(self):

        """Function:  test_no_err_std_file

        Description:  Test with no errors to standard out and file.

        Arguments:

        """

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, **self.data_config15)

        self.assertTrue(os.path.isfile(self.file))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_file_mail2(self, mock_mail):

        """Function:  test_no_err_verb_file_mail2

        Description:  Test with no errors detected - file and mail - verbose.

        Arguments:

        """

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, **self.data_config14)

        self.assertEqual(linecnt(self.file), 1)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_file_mail(self, mock_mail):

        """Function:  test_no_err_verb_file_mail

        Description:  Test with no errors detected - file and mail - verbose.

        Arguments:

        """

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, **self.data_config14)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_file_mail2(self, mock_mail):

        """Function:  test_no_err_file_mail2

        Description:  Test with no errors detected - file and mail.

        Arguments:

        """

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, **self.data_config13)

        self.assertTrue(os.path.isfile(self.file))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_file_mail(self, mock_mail):

        """Function:  test_no_err_file_mail

        Description:  Test with no errors detected - file and mail.

        Arguments:

        """

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, **self.data_config13)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_std_mail2(self, mock_mail):

        """Function:  test_no_err_verb_std_mail2

        Description:  Test no erro to std out & mail - verbose.

        Arguments:

        """

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.data_out(self.data, **self.data_config12))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_std_mail(self, mock_mail):

        """Function:  test_no_err_verb_std_mail

        Description:  Test no erro to std out & mail - verbose.

        Arguments:

        """

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, **self.data_config12)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_std_mail2(self, mock_mail):

        """Function:  test_no_err_std_mail2

        Description:  Test with no errors to standard out and mail.

        Arguments:

        """

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.data_out(self.data, **self.data_config11)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_std_mail(self, mock_mail):

        """Function:  test_no_err_std_mail

        Description:  Test with no errors to standard out and mail.

        Arguments:

        """

        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.data_out(self.data, **self.data_config11))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_err_verb_mail(self, mock_mail):

        """Function:  test_err_verb_mail

        Description:  Test with error for mail - verbose.

        Arguments:

        """

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, **self.data_config10)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_err_mail(self, mock_mail):

        """Function:  test_err_mail

        Description:  Test with error for mail.

        Arguments:

        """

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, **self.data_config9)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_verb_mail(self, mock_mail):

        """Function:  test_no_err_verb_mail

        Description:  Test with no error for mail - verbose.

        Arguments:

        """

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, **self.data_config10)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    def test_no_err_mail(self, mock_mail):

        """Function:  test_no_err_mail

        Description:  Test with no error for mail.

        Arguments:

        """

        mock_mail.return_value = self.mail

        rmq_admin.data_out(self.data, **self.data_config9)

        self.assertEqual(self.mail.msg, self.results)

    def test_append_verb_file(self):

        """Function:  test_append_verb_file

        Description:  Test with append file and verbose.

        Arguments:

        """

        rmq_admin.data_out(self.data, **self.data_config8)
        rmq_admin.data_out(self.data, **self.data_config8)

        self.assertEqual(linecnt(self.file), 2)

    def test_append_file(self):

        """Function:  test_append_file

        Description:  Test with errors detected - append file.

        Arguments:

        """

        rmq_admin.data_out(self.data, **self.data_config7)
        rmq_admin.data_out(self.data, **self.data_config7)

        self.assertEqual(linecnt(self.file), 2)

    def test_err_verb_file(self):

        """Function:  test_err_verb_file

        Description:  Test with errors detected - write file - verbose.

        Arguments:

        """

        rmq_admin.data_out(self.data, **self.data_config6)

        self.assertEqual(linecnt(self.file), 1)

    def test_err_file(self):

        """Function:  test_err_file

        Description:  Test with errors detected - write file.

        Arguments:

        """

        rmq_admin.data_out(self.data, **self.data_config5)

        self.assertEqual(linecnt(self.file), 1)

    def test_no_err_verb_file(self):

        """Function:  test_no_err_verb_file

        Description:  Test with no errors detected - write file - verbose.

        Arguments:

        """

        rmq_admin.data_out(self.data, **self.data_config6)

        self.assertEqual(linecnt(self.file), 1)

    def test_no_err_file(self):

        """Function:  test_no_err_file

        Description:  Test with no errors detected - write file.

        Arguments:

        """

        rmq_admin.data_out(self.data, **self.data_config5)

        self.assertTrue(os.path.isfile(self.file))

    def test_errors_suppr(self):

        """Function:  test_errors_suppr

        Description:  Test with errors detected - suppressed.

        Arguments:

        """

        self.assertFalse(rmq_admin.data_out(self.data, **self.data_config2))

    def test_no_err_verb_suppr(self):

        """Function:  test_no_err_verb_suppr

        Description:  Test with no errors detected - verbose mode - suppressed.

        Arguments:

        """

        self.assertFalse(rmq_admin.data_out(self.data, **self.data_config4))

    def test_errors_verbose(self):

        """Function:  test_errors_verbose

        Description:  Test with errors detected - verbose mode.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.data_out(self.data, **self.data_config3))

    def test_errors(self):

        """Function:  test_errors

        Description:  Test with errors detected.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, **self.data_config))

    def test_no_errors_verbose(self):

        """Function:  test_no_errors_verbose

        Description:  Test with no errors detected - verbose mode.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.data_out(self.data, **self.data_config3))

    def test_no_errors(self):

        """Function:  test_no_errors

        Description:  Test with no errors detected.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.data_out(self.data, **self.data_config))

    def tearDown(self):

        """Function:  tearDown

        Description:  Cleanup of unit testing.

        Arguments:

        """

        if os.path.isfile(self.file):
            os.remove(self.file)


if __name__ == "__main__":
    unittest.main()
