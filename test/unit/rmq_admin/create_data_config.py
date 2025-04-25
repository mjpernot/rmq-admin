# Classification (U)

"""Program:  create_data_config.py

    Description:  Unit testing of create_data_config in rmq_admin.py.

    Usage:
        python test/unit/rmq_admin/create_data_config.py
        python3 test/unit/rmq_admin/create_data_config.py

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
import rmq_admin                           # pylint:disable=E0401,C0413
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class ArgParser():                                      # pylint:disable=R0903

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

        self.args_array = {
            "-c": "rabbitmq", "-d": "config", "-t": "to_addr",
            "-o": "outfile", "-k": "indentation", "-a": "a", "-z": False}

    def get_val(self, skey, def_val=None):

        """Method:  get_val

        Description:  Method stub holder for gen_class.ArgParser.get_val.

        Arguments:

        """

        return self.args_array.get(skey, def_val)


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_mode_with_arg
        test_pprint_with_no_arg
        test_subj_with_no_arg
        test_to_addr_with_arg

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.args = ArgParser()
        self.args.args_array["-m"] = "mongo"
        self.args2 = ArgParser()
        self.results = None
        self.results2 = "to_addr"
        self.results3 = False
        self.results4 = "a"

    def test_mode_with_arg(self):

        """Function:  test_mode_with_arg

        Description:  Test with mode with argument passed.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_data_config(self.args)["mode"],
            self.results4)

    def test_pprint_with_no_arg(self):

        """Function:  test_pprint_with_no_arg

        Description:  Test with mailx with no data.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_data_config(self.args)["use_pprint"],
            self.results3)

    def test_subj_with_no_arg(self):

        """Function:  test_subj_with_no_arg

        Description:  Test with to_address with no argument passed.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_data_config(self.args)["subj"],
            self.results)

    def test_to_addr_with_arg(self):

        """Function:  test_to_addr_with_arg

        Description:  Test with to_address with argument passed.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_data_config(self.args)["to_addr"],
            self.results2)


if __name__ == "__main__":
    unittest.main()
