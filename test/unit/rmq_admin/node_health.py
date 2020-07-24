#!/usr/bin/python
# Classification (U)

"""Program:  node_health.py

    Description:  Unit testing of node_health in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/node_health.py

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


class MailTest(object):

    """Class:  MailTest

    Description:  Class which is a representation of an email.

    Methods:
        __init__ -> Class instance initilization.
        add_2_msg -> Add text to text string if data is present.
        send_mail -> Send email.

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

    def send_mail(self, txt_ln=None):

        """Method:  send_mail

        Description:  Send email.

        Arguments:

        """

        pass


class GetTest(object):

    """Class:  GetTest

    Description:  Class which is a representation of a request call.

    Methods:
        __init__ -> Class instance initilization.
        json -> Return status of request call.

    """

    def __init__(self, data):

        """Method:  __init__

        Description:  Initialization of an instance class.

        Arguments:
            (input) data -> Results of requests.

        """

        self.data = data

    def json(self):

        """Method:  json

        Description:  Return status of request call.

        Arguments:

        """

        return self.data


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_no_err_verb_all -> Test with no errors detected - all - verbose.
        test_no_err_all -> Test with no errors detected - all outputs.
        test_no_err_verb_std_file -> Test no erro to std out & file - verbose.
        test_no_err_std_file -> Test with no errors to standard out and file.
        test_no_err_verb_file_mail -> Test no errors: file & mail: verbose.
        test_no_err_file_mail -> Test with no errors detected - file and mail.
        test_no_err_verb_std_mail -> Test no erro to std out & mail - verbose.
        test_no_err_std_mail -> Test with no errors to standard out and mail.
        test_err_verb_mail -> Test with error for mail - verbose.
        test_err_mail -> Test with error for mail.
        test_no_err_verb_mail -> Test with no error for mail - verbose.
        test_no_err_mail -> Test with no error for mail.
        test_append_verb_file -> Test with append file and verbose.
        test_append_file -> Test with errors detected - append file.
        test_err_verb_file -> Test with errors detected - write file - verbose.
        test_err_file -> Test with errors detected - write file.
        test_no_err_verb_file -> Test no errors detected: write file, verbose.
        test_no_err_file -> Test with no errors detected - write file.
        test_errors_suppr -> Test with errors detected - suppressed.
        test_no_err_verb_suppr -> Test no errors detected: verbose, suppressed.
        test_errors_verbose -> Test with errors detected - verbose mode.
        test_errors -> Test with errors detected.
        test_no_errors_verbose -> Test with no errors detected - verbose mode.
        test_no_errors -> Test with no errors detected.
        tearDown -> Cleanup of testing environment.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.mail = MailTest("toaddr")
        self.cfg = CfgTest()
        self.base_url = "http://localhost:15672/api/"
        self.data = {'status': 'ok'}
        self.data2 = {'status': 'failed', 'reason': 'reason for failure'}
        self.get = GetTest(self.data)
        self.get2 = GetTest(self.data2)
        self.file = "test/unit/rmq_admin/tmp/outfile.txt"
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
        self.date = "2020-07-24"
        self.time = "10:20:10"
        self.header = "Node Health Check"
        self.subhdr = "    AsOf: " + self.date + " " + self.time
        self.entry = "    Status: ok"
        self.entry2 = "    Error detected in node"
        self.entry3 = "    Status: failed"
        self.entry4 = "    Message: reason for failure"
        self.results = ""
        self.results2 = self.header + self.subhdr + self.entry
        self.results3 = \
            self.header + self.subhdr + self.entry2 + self.entry3 + self.entry4

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.requests.get")
    def test_no_err_verb_all(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_verb_all

        Description:  Test with no errors detected - all - verbose.

        Arguments:

        """

        mock_get.return_value = self.get
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.node_health(self.base_url, self.cfg, self.args_array18)

        self.assertEqual(sum(1 for line in open(self.file)), 3)
        self.assertEqual(self.mail.msg, self.results2)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.requests.get")
    def test_no_err_all(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_all

        Description:  Test with no errors detected - all outputs.

        Arguments:

        """

        mock_get.return_value = self.get
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array17)

        self.assertFalse(os.path.isfile(self.file))
        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.requests.get")
    def test_no_err_verb_std_file(self, mock_get):

        """Function:  test_no_err_verb_std_file

        Description:  Test no erro to std out & file - verbose.

        Arguments:

        """

        mock_get.return_value = self.get

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
                                                   self.args_array16))

        self.assertEqual(sum(1 for line in open(self.file)), 3)

    @mock.patch("rmq_admin.requests.get")
    def test_no_err_std_file(self, mock_get):

        """Function:  test_no_err_std_file

        Description:  Test with no errors to standard out and file.

        Arguments:

        """

        mock_get.return_value = self.get

        self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
                                               self.args_array15))
        self.assertFalse(os.path.isfile(self.file))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.requests.get")
    def test_no_err_verb_file_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_verb_file_mail

        Description:  Test with no errors detected - file and mail - verbose.

        Arguments:

        """

        mock_get.return_value = self.get
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array14)

        self.assertEqual(sum(1 for line in open(self.file)), 3)
        self.assertEqual(self.mail.msg, self.results2)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.requests.get")
    def test_no_err_file_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_file_mail

        Description:  Test with no errors detected - file and mail.

        Arguments:

        """

        mock_get.return_value = self.get
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array13)

        self.assertFalse(os.path.isfile(self.file))
        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.requests.get")
    def test_no_err_verb_std_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_errors_verbose

        Description:  Test no erro to std out & mail - verbose.

        Arguments:

        """

        mock_get.return_value = self.get
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
                                                   self.args_array12))

        self.assertEqual(self.mail.msg, self.results2)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.requests.get")
    def test_no_err_std_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_std_mail

        Description:  Test with no errors to standard out and mail.

        Arguments:

        """

        mock_get.return_value = self.get
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
                                               self.args_array11))
        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.requests.get")
    def test_err_verb_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_err_verb_mail

        Description:  Test with error for mail - verbose.

        Arguments:

        """

        mock_get.return_value = self.get2
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array10)

        self.assertEqual(self.mail.msg, self.results3)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.requests.get")
    def test_err_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_err_mail

        Description:  Test with error for mail.

        Arguments:

        """

        mock_get.return_value = self.get2
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array9)

        self.assertEqual(self.mail.msg, self.results3)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.requests.get")
    def test_no_err_verb_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_verb_mail

        Description:  Test with no error for mail - verbose.

        Arguments:

        """

        mock_get.return_value = self.get
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array10)

        self.assertEqual(self.mail.msg, self.results2)

    @mock.patch("rmq_admin.requests.get")
    def test_no_err_mail(self, mock_get):

        """Function:  test_no_err_mail

        Description:  Test with no error for mail.

        Arguments:

        """

        mock_get.return_value = self.get

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array9)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.requests.get")
    def test_append_verb_file(self, mock_get):

        """Function:  test_append_verb_file

        Description:  Test with append file and verbose.

        Arguments:

        """

        mock_get.return_value = self.get

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array8)
        rmq_admin.node_health(self.base_url, self.cfg, self.args_array8)

        self.assertEqual(sum(1 for line in open(self.file)), 6)

    @mock.patch("rmq_admin.requests.get")
    def test_append_file(self, mock_get):

        """Function:  test_append_file

        Description:  Test with errors detected - append file.

        Arguments:

        """

        mock_get.return_value = self.get2

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array7)
        rmq_admin.node_health(self.base_url, self.cfg, self.args_array7)

        self.assertEqual(sum(1 for line in open(self.file)), 10)

    @mock.patch("rmq_admin.requests.get")
    def test_err_verb_file(self, mock_get):

        """Function:  test_err_verb_file

        Description:  Test with errors detected - write file - verbose.

        Arguments:

        """

        mock_get.return_value = self.get2

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array6)

        self.assertEqual(sum(1 for line in open(self.file)), 5)

    @mock.patch("rmq_admin.requests.get")
    def test_err_file(self, mock_get):

        """Function:  test_err_file

        Description:  Test with errors detected - write file.

        Arguments:

        """

        mock_get.return_value = self.get2

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array5)

        self.assertEqual(sum(1 for line in open(self.file)), 5)

    @mock.patch("rmq_admin.requests.get")
    def test_no_err_verb_file(self, mock_get):

        """Function:  test_no_err_verb_file

        Description:  Test with no errors detected - write file - verbose.

        Arguments:

        """

        mock_get.return_value = self.get

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array6)

        self.assertEqual(sum(1 for line in open(self.file)), 3)

    @mock.patch("rmq_admin.requests.get")
    def test_no_err_file(self, mock_get):

        """Function:  test_no_err_file

        Description:  Test with no errors detected - write file.

        Arguments:

        """

        mock_get.return_value = self.get

        rmq_admin.node_health(self.base_url, self.cfg, self.args_array5)

        self.assertFalse(os.path.isfile(self.file))

    @mock.patch("rmq_admin.requests.get")
    def test_errors_suppr(self, mock_get):

        """Function:  test_errors_suppr

        Description:  Test with errors detected - suppressed.

        Arguments:

        """

        mock_get.return_value = self.get2

        self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
                                               self.args_array2))

    @mock.patch("rmq_admin.requests.get")
    def test_no_err_verb_suppr(self, mock_get):

        """Function:  test_no_err_verb_suppr

        Description:  Test with no errors detected - verbose mode - suppressed.

        Arguments:

        """

        mock_get.return_value = self.get

        self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
                                               self.args_array4))

    @mock.patch("rmq_admin.requests.get")
    def test_errors_verbose(self, mock_get):

        """Function:  test_errors_verbose

        Description:  Test with errors detected - verbose mode.

        Arguments:

        """

        mock_get.return_value = self.get2

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
                                                   self.args_array3))

    @mock.patch("rmq_admin.requests.get")
    def test_errors(self, mock_get):

        """Function:  test_errors

        Description:  Test with errors detected.

        Arguments:

        """

        mock_get.return_value = self.get2

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
                                                   self.args_array))

    @mock.patch("rmq_admin.requests.get")
    def test_no_errors_verbose(self, mock_get):

        """Function:  test_no_errors_verbose

        Description:  Test with no errors detected - verbose mode.

        Arguments:

        """

        mock_get.return_value = self.get

        with gen_libs.no_std_out():
            self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
                                                   self.args_array3))

    @mock.patch("rmq_admin.requests.get")
    def test_no_errors(self, mock_get):

        """Function:  test_no_errors

        Description:  Test with no errors detected.

        Arguments:

        """

        mock_get.return_value = self.get

        self.assertFalse(rmq_admin.node_health(self.base_url, self.cfg,
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
