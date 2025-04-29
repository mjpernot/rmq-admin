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
import unittest

# Local
sys.path.append(os.getcwd())
import rmq_admin                                # pylint:disable=E0401,C0413
import lib.gen_class as gen_class           # pylint:disable=E0401,C0413,R0402
import lib.gen_libs as gen_libs             # pylint:disable=E0401,C0413,R0402
import rabbit_lib.rabbitmq_class as rmqcls  # pylint:disable=E0401,C0413,R0402
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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_verb_std_file
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

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.http = "http"
        self.mod = "rabbitmq"
        self.dir = "test/integration/rmq_admin/config"
        self.file = "test/integration/rmq_admin/tmp/outfile.txt"
        self.cfg = gen_libs.load_module(self.mod, self.dir)
        self.rmq = rmqcls.RabbitMQAdmin(
            self.cfg.user, self.cfg.japd, host=self.cfg.host,
            port=self.cfg.m_port, scheme=self.cfg.scheme)
        self.data_config = {"report": False}
        self.data_config2 = {"report": True}
        self.data_config3 = {"report": True, "suppress": True}
        self.data_config4 = {
            "report": False, "suppress": True, "outfile": self.file}
        self.data_config5 = {
            "report": True, "suppress": True, "outfile": self.file}
        self.data_config6 = {
            "report": True, "suppress": True, "outfile": self.file,
            "mode": "a"}

    def test_append_verb_file(self):

        """Function:  test_append_verb_file

        Description:  Test with append file and verbose.

        Arguments:

        """

        rmq_admin.node_health(self.data_config6, self.dtg, self.rmq)
        rmq_admin.node_health(self.data_config6, self.dtg, self.rmq)

        self.assertEqual(linecnt(self.file), 2)

    def test_no_err_verb_file(self):

        """Function:  test_no_err_verb_file

        Description:  Test with no errors detected - write file - verbose.

        Arguments:

        """

        rmq_admin.node_health(self.data_config5, self.dtg, self.rmq)

        self.assertEqual(linecnt(self.file), 1)

    def test_no_err_file(self):

        """Function:  test_no_err_file

        Description:  Test with no errors detected - write file.

        Arguments:

        """

        rmq_admin.node_health(self.data_config4, self.dtg, self.rmq)

        self.assertFalse(os.path.isfile(self.file))

    def test_no_err_verb_suppr(self):

        """Function:  test_no_err_verb_suppr

        Description:  Test with no errors detected - verbose mode - suppressed.

        Arguments:

        """

        self.assertFalse(
            rmq_admin.node_health(self.data_config3, self.dtg, self.rmq))

    def test_no_errors_verbose(self):

        """Function:  test_no_errors_verbose

        Description:  Test with no errors detected - verbose mode.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(
                rmq_admin.node_health(self.data_config2, self.dtg, self.rmq))

    def test_no_errors(self):

        """Function:  test_no_errors

        Description:  Test with no errors detected - no report.

        Arguments:

        """

        self.assertFalse(
            rmq_admin.node_health(self.data_config, self.dtg, self.rmq))

    def tearDown(self):

        """Function:  tearDown

        Description:  Cleanup of unit testing.

        Arguments:

        """

        if os.path.isfile(self.file):
            os.remove(self.file)


if __name__ == "__main__":
    unittest.main()
