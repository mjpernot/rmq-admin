# Classification (U)

"""Program:  create_header.py

    Description:  Unit testing of create_header in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/create_header.py

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
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class RabbitMQAdmin():                                  # pylint:disable=R0903

    """Class:  RepSet

    Description:  Class stub holder for rabbitmq_class.RabbitMQAdmin class.

    Methods:
        __init__

    """

    def __init__(                                       # pylint:disable=R0913
        self, user, japd, host="localhost", port=15672, scheme="https"):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = user
        self.host = host
        self.port = port
        self.scheme = scheme
        self.url = self.scheme + "://" + self.host + ":" + str(self.port)
        self.auth = (self.name, japd)
        self.headers = {"Content-type": "application/json"}


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_header

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.rmq = RabbitMQAdmin("user", "japd")
        self.results = "localhost"

    def test_header(self):

        """Function:  test_state_fail

        Description:  Test with health failure check.

        Arguments:

        """

        self.assertEqual(
            rmq_admin.create_header(self.dtg, self.rmq)["Node"],
            self.results)


if __name__ == "__main__":
    unittest.main()
