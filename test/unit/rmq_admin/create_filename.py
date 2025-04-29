# Classification (U)

"""Program:  create_filename.py

    Description:  Unit testing of create_filename in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/create_filename.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os
import unittest
import mock

# Local
sys.path.append(os.getcwd())
import rmq_admin                                # pylint:disable=E0401,C0413
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_subj_all
        test_filename_all
        test_subj_host_msecs
        test_filename_host_msecs
        test_subj_host_dtg
        test_filename_host_dtg
        test_subj_dtg_msecs
        test_filename_dtg_msecs
        test_subj_msecs
        test_filename_msecs
        test_subj_dtg
        test_filename_dtg
        test_subj_hostname
        test_filename_hostname
        test_subj
        test_filename_subj
        test_filename

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()

        # -f = FileName
        # -u = SubjectName
        # -n = True|False - Use Hostname
        # -g = True|False - Use DTG
        # -m = True|False - Use Microseconds
        self.data_config1 = {"attach_file": "FileName"}
        self.data_config2 = {"attach_file": "FileName", "subj": "SubjectLine"}
        self.data_config3 = {"subj": "SubjectLine"}
        self.data_config4 = {"attach_file": "FileName", "add_host": True}
        self.data_config4a = {"subj": "SubjectLine", "add_host": True}
        self.data_config5 = {"attach_file": "FileName", "add_dtg": True}
        self.data_config5a = {"subj": "SubjectLine", "add_dtg": True}
        self.data_config6 = {"attach_file": "FileName", "add_micro": True}
        self.data_config6a = {"subj": "SubjectLine", "add_micro": True}
        self.data_config7 = {
            "attach_file": "FileName", "add_dtg": True, "add_micro": True}
        self.data_config7a = {
            "subj": "SubjectLine", "add_dtg": True, "add_micro": True}
        self.data_config8 = {
            "attach_file": "FileName", "add_dtg": True, "add_host": True}
        self.data_config8a = {
            "subj": "SubjectLine", "add_dtg": True, "add_host": True}
        self.data_config9 = {
            "attach_file": "FileName", "add_micro": True, "add_host": True}
        self.data_config9a = {
            "subj": "SubjectLine", "add_micro": True, "add_host": True}
        self.data_config10 = {
            "attach_file": "FileName", "add_dtg": True, "add_host": True,
            "add_micro": True}
        self.data_config10a = {
            "subj": "SubjectLine", "add_dtg": True, "add_host": True,
            "add_micro": True}

        dtg = self.dtg.get_time("zulu")
        msecs = self.dtg.msecs
        json = ".json"
        fname = "FileName."
        subj = "SubjectLine."
        fname_host = "FileName.Hostname."
        subj_host = "SubjectLine.Hostname."
        self.results1 = "FileName.json"
        self.results2 = "FileName.json"
        self.results3 = "SubjectLine.json"
        self.results4 = "FileName.Hostname.json"
        self.results4a = "SubjectLine.Hostname.json"
        self.results5 = fname + dtg + json
        self.results5a = subj + dtg + json
        self.results6 = fname + msecs + json
        self.results6a = subj + msecs + json
        self.results7 = fname + dtg + "." + msecs + json
        self.results7a = subj + dtg + "." + msecs + json
        self.results8 = fname_host + dtg + json
        self.results8a = subj_host + dtg + json
        self.results9 = fname_host + msecs + json
        self.results9a = subj_host + msecs + json
        self.results10 = fname_host + dtg + "." + msecs + json
        self.results10a = subj_host + dtg + "." + msecs + json

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_subj_all(self):

        """Function:  test_subj_all

        Description:  Test with subject and hostname and dtg and microseconds.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config10a), self.results10a)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_filename_all(self):

        """Function:  test_filename_all

        Description:  Test with subject and hostname and dtg and microseconds.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config10), self.results10)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_subj_host_msecs(self):

        """Function:  test_subj_host_msecs

        Description:  Test with subject and hostname and microseconds.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config9a), self.results9a)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_filename_host_msecs(self):

        """Function:  test_filename_host_msecs

        Description:  Test with filename and hostname and microseconds.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config9), self.results9)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_subj_host_dtg(self):

        """Function:  test_subj_host_dtg

        Description:  Test with subject and hostname and dtg.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config8a), self.results8a)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_filename_host_dtg(self):

        """Function:  test_filename_host_dtg

        Description:  Test with filename and hostname and dtg.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config8), self.results8)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_subj_dtg_msecs(self):

        """Function:  test_subj_dtg_msecs

        Description:  Test with subject and dtg and microseconds.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config7a), self.results7a)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_filename_dtg_msecs(self):

        """Function:  test_filename_dtg_msecs

        Description:  Test with filename and dtg and microseconds.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config7), self.results7)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_subj_msecs(self):

        """Function:  test_subj_msecs

        Description:  Test with subject and microseconds.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config6a), self.results6a)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_filename_msecs(self):

        """Function:  test_filename_msecs

        Description:  Test with filename and microseconds.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config6), self.results6)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_subj_dtg(self):

        """Function:  test_subj_dtg

        Description:  Test with subject and DTG.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config5a), self.results5a)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_filename_dtg(self):

        """Function:  test_filename_dtg

        Description:  Test with filename and DTG.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config5), self.results5)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_subj_hostname(self):

        """Function:  test_subj_hostname

        Description:  Test with subject and hostname.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config4a), self.results4a)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_filename_hostname(self):

        """Function:  test_filename_hostname

        Description:  Test with filename and hostname.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config4), self.results4)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_subj(self):

        """Function:  test_subj

        Description:  Test with subject option only.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config3), self.results3)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_filename_subj(self):

        """Function:  test_filename_subj

        Description:  Test with filename and subj passed.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config2), self.results2)

    @mock.patch("rmq_admin.socket.gethostname",
                mock.Mock(return_value="Hostname"))
    def test_filename(self):

        """Function:  test_filename

        Description:  Test with filename option only.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_filename(
                dtg=self.dtg, **self.data_config1), self.results1)


if __name__ == "__main__":
    unittest.main()
