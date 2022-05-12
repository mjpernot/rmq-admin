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
import rabbit_lib.rabbitmq_class as rabbitmq_class
import version

__version__ = version.__version__


def linecnt(fname):

    """Function:  linecnt

    Description:  Count number of lines in a file.

    Arguments:

    """

    return sum(1 for _ in open(fname))


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


class CfgTest(object):

    """Class:  CfgTest

    Description:  Class which is a representation of a cfg module.

    Methods:
        __init__

    """

    def __init__(self):

        """Method:  __init__

        Description:  Initialization instance of the CfgTest class.

        Arguments:

        """

        self.user = "username"
        self.japd = None
        self.host = "hostname"
        self.m_port = 15672
        self.scheme = "https"


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
        self.cfg = CfgTest()

        self.rmq = rabbitmq_class.RabbitMQAdmin(self.cfg.user, self.cfg.japd)

        self.data = {'status': 'ok'}
        self.data2 = {'status': 'failed', 'reason': 'reason for failure'}
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
        self.results = ""
        self.results2 = '{"Status": "ok", "Type": "Node Health Check", \
"AsOf": "2020-07-24 10:20:10"}'
        self.results3 = '{"Status": "failed", "Message": \
"reason for failure", "Type": "Node Health Check", \
"AsOf": "2020-07-24 10:20:10"}'

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs.get_date")
    @mock.patch("rmq_admin.gen_libs.get_time")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_all2(self, mock_get, mock_time, mock_date, mock_mail):

        """Function:  test_no_err_verb_all2

        Description:  Test with no errors detected - all - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array18

        mock_get.return_value = self.data
        mock_date.return_value = self.date
        mock_time.return_value = self.time
        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(self.mail.msg, self.results2)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs.get_date")
    @mock.patch("rmq_admin.gen_libs.get_time")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_all(self, mock_get, mock_time, mock_date, mock_mail):

        """Function:  test_no_err_verb_all

        Description:  Test with no errors detected - all - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array18

        mock_get.return_value = self.data
        mock_date.return_value = self.date
        mock_time.return_value = self.time
        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(linecnt(self.file), 5)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_all2(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_all2

        Description:  Test with no errors detected - all outputs.

        Arguments:

        """

        self.args.args_array = self.args_array17

        mock_get.return_value = self.data
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_all(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_all

        Description:  Test with no errors detected - all outputs.

        Arguments:

        """

        self.args.args_array = self.args_array17

        mock_get.return_value = self.data
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.rmq, self.args)

        self.assertFalse(os.path.isfile(self.file))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_std_file(self, mock_get):

        """Function:  test_no_err_verb_std_file

        Description:  Test no erro to std out & file - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array16

        mock_get.return_value = self.data

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.node_health(self.rmq, self.args))

        self.assertEqual(linecnt(self.file), 5)

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_std_file2(self, mock_get):

        """Function:  test_no_err_std_file2

        Description:  Test with no errors to standard out and file.

        Arguments:

        """

        self.args.args_array = self.args_array15

        mock_get.return_value = self.data

        self.assertFalse(rmq_admin.node_health(self.rmq, self.args))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_std_file(self, mock_get):

        """Function:  test_no_err_std_file

        Description:  Test with no errors to standard out and file.

        Arguments:

        """

        self.args.args_array = self.args_array15

        mock_get.return_value = self.data

        self.assertFalse(os.path.isfile(self.file))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs.get_date")
    @mock.patch("rmq_admin.gen_libs.get_time")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_file_mail2(self, mock_get, mock_time, mock_date,
                                    mock_mail):

        """Function:  test_no_err_verb_file_mail2

        Description:  Test with no errors detected - file and mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array14

        mock_get.return_value = self.data
        mock_date.return_value = self.date
        mock_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(linecnt(self.file), 5)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs.get_date")
    @mock.patch("rmq_admin.gen_libs.get_time")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_file_mail(self, mock_get, mock_time, mock_date,
                                   mock_mail):

        """Function:  test_no_err_verb_file_mail

        Description:  Test with no errors detected - file and mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array14

        mock_get.return_value = self.data
        mock_date.return_value = self.date
        mock_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(self.mail.msg, self.results2)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_file_mail2(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_file_mail2

        Description:  Test with no errors detected - file and mail.

        Arguments:

        """

        self.args.args_array = self.args_array13

        mock_get.return_value = self.data
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.rmq, self.args)

        self.assertFalse(os.path.isfile(self.file))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_file_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_file_mail

        Description:  Test with no errors detected - file and mail.

        Arguments:

        """

        self.args.args_array = self.args_array13

        mock_get.return_value = self.data
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_std_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_verb_std_mail

        Description:  Test no erro to std out & mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array12

        mock_get.return_value = self.data
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.node_health(self.rmq, self.args))

        self.assertEqual(self.mail.msg, self.results2)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_std_mail2(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_std_mail2

        Description:  Test with no errors to standard out and mail.

        Arguments:

        """

        self.args.args_array = self.args_array11

        mock_get.return_value = self.data
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_std_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_std_mail

        Description:  Test with no errors to standard out and mail.

        Arguments:

        """

        self.args.args_array = self.args_array11

        mock_get.return_value = self.data
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        self.assertFalse(
            rmq_admin.node_health(self.rmq, self.args))

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_err_verb_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_err_verb_mail

        Description:  Test with error for mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array10

        mock_get.return_value = self.data2
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(self.mail.msg, self.results3)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_err_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_err_mail

        Description:  Test with error for mail.

        Arguments:

        """

        self.args.args_array = self.args_array9

        mock_get.return_value = self.data2
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(self.mail.msg, self.results3)

    @mock.patch("rmq_admin.gen_class.setup_mail")
    @mock.patch("rmq_admin.gen_libs")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_mail(self, mock_get, mock_lib, mock_mail):

        """Function:  test_no_err_verb_mail

        Description:  Test with no error for mail - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array10

        mock_get.return_value = self.data
        mock_lib.get_date.return_value = self.date
        mock_lib.get_time.return_value = self.time
        mock_mail.return_value = self.mail

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(self.mail.msg, self.results2)

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_mail(self, mock_get):

        """Function:  test_no_err_mail

        Description:  Test with no error for mail.

        Arguments:

        """

        self.args.args_array = self.args_array9

        mock_get.return_value = self.data

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(self.mail.msg, self.results)

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_append_verb_file(self, mock_get):

        """Function:  test_append_verb_file

        Description:  Test with append file and verbose.

        Arguments:

        """

        self.args.args_array = self.args_array8

        mock_get.return_value = self.data

        rmq_admin.node_health(self.rmq, self.args)
        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(linecnt(self.file), 10)

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_append_file(self, mock_get):

        """Function:  test_append_file

        Description:  Test with errors detected - append file.

        Arguments:

        """

        self.args.args_array = self.args_array7

        mock_get.return_value = self.data2

        rmq_admin.node_health(self.rmq, self.args)
        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(linecnt(self.file), 12)

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_err_verb_file(self, mock_get):

        """Function:  test_err_verb_file

        Description:  Test with errors detected - write file - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array6

        mock_get.return_value = self.data2

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(linecnt(self.file), 6)

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_err_file(self, mock_get):

        """Function:  test_err_file

        Description:  Test with errors detected - write file.

        Arguments:

        """

        self.args.args_array = self.args_array5

        mock_get.return_value = self.data2

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(linecnt(self.file), 6)

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_file(self, mock_get):

        """Function:  test_no_err_verb_file

        Description:  Test with no errors detected - write file - verbose.

        Arguments:

        """

        self.args.args_array = self.args_array6

        mock_get.return_value = self.data

        rmq_admin.node_health(self.rmq, self.args)

        self.assertEqual(linecnt(self.file), 5)

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_file(self, mock_get):

        """Function:  test_no_err_file

        Description:  Test with no errors detected - write file.

        Arguments:

        """

        self.args.args_array = self.args_array5

        mock_get.return_value = self.data

        rmq_admin.node_health(self.rmq, self.args)

        self.assertFalse(os.path.isfile(self.file))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_errors_suppr(self, mock_get):

        """Function:  test_errors_suppr

        Description:  Test with errors detected - suppressed.

        Arguments:

        """

        self.args.args_array = self.args_array2

        mock_get.return_value = self.data2

        self.assertFalse(
            rmq_admin.node_health(self.rmq, self.args))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_err_verb_suppr(self, mock_get):

        """Function:  test_no_err_verb_suppr

        Description:  Test with no errors detected - verbose mode - suppressed.

        Arguments:

        """

        self.args.args_array = self.args_array4

        mock_get.return_value = self.data

        self.assertFalse(
            rmq_admin.node_health(self.rmq, self.args))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_errors_verbose(self, mock_get):

        """Function:  test_errors_verbose

        Description:  Test with errors detected - verbose mode.

        Arguments:

        """

        self.args.args_array = self.args_array3

        mock_get.return_value = self.data2

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.node_health(self.rmq, self.args))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_errors(self, mock_get):

        """Function:  test_errors

        Description:  Test with errors detected.

        Arguments:

        """

        self.args.args_array = self.args_array

        mock_get.return_value = self.data2

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.node_health(self.rmq, self.args))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_errors_verbose(self, mock_get):

        """Function:  test_no_errors_verbose

        Description:  Test with no errors detected - verbose mode.

        Arguments:

        """

        self.args.args_array = self.args_array3

        mock_get.return_value = self.data

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.node_health(self.rmq, self.args))

    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.get")
    def test_no_errors(self, mock_get):

        """Function:  test_no_errors

        Description:  Test with no errors detected.

        Arguments:

        """

        self.args.args_array = self.args_array

        mock_get.return_value = self.data

        self.assertFalse(
            rmq_admin.node_health(self.rmq, self.args))

    def tearDown(self):

        """Function:  tearDown

        Description:  Cleanup of unit testing.

        Arguments:

        """

        if os.path.isfile(self.file):
            os.remove(self.file)


if __name__ == "__main__":
    unittest.main()
