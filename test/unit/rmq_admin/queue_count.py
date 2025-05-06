# Classification (U)

"""Program:  queue_count.py

    Description:  Unit testing of queue_count in rmq_admin.py.

    Usage:
        test/unit/rmq_admin/queue_count.py

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
import rabbit_lib.rabbitmq_class as rmqcls  # pylint:disable=E0401,C0413,R0402
import version                                  # pylint:disable=E0401,C0413

__version__ = version.__version__


class RabbitMQPub():

    """Class:  RabbitMQPub

    Description:  Class which is a representation of a RabbitMQPub class.

    Methods:
        __init__
        connect
        open_channel
        connect_queue
        queue_count
        close_channel
        close

    """

    def __init__(self, user, jpad):

        """Method:  __init__

        Description:  Initialization instance of the RabbitMQPub class.

        Arguments:

        """

        self.user = user
        self.japd = jpad
        self.queue_name = None
        self.count = 4

    def connect(self):

        """Method:  connect

        Description:  Stub holder for the RabbitMQPub.connect method.

        Arguments:

        """

        return True

    def open_channel(self):

        """Method:  open_channel

        Description:  Stub holder for the RabbitMQPub.open_channel method.

        Arguments:

        """

        return True

    def connect_queue(self):

        """Method:  connect_queue

        Description:  Stub holder for the RabbitMQPub.connect_queue method.

        Arguments:

        """

        return True

    def queue_count(self):

        """Method:  queue_count

        Description:  Stub holder for the RabbitMQPub.queue_count method.

        Arguments:

        """

        return self.count

    def close_channel(self):

        """Method:  close_channel

        Description:  Stub holder for the RabbitMQPub.close_channel method.

        Arguments:

        """

        return True

    def close(self):

        """Method:  close

        Description:  Stub holder for the RabbitMQPub.close method.

        Arguments:

        """

        return True


class CfgTest():                                        # pylint:disable=R0903

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp
        test_threshold_rpt_on_queue_meet
        test_threshold_on_queue_meet
        test_threshold_rpt_on
        test_threshold_on
        test_no_threshold
        test_multiple_queues
        test_single_queue
        test_no_queues

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.dtg = gen_class.TimeFormat()
        self.dtg.create_time()
        self.data_config = {
            "threshold": False, "threshold_cnt": 5, "threshold_rpt": False}
        self.data_config2 = {
            "threshold": True, "threshold_cnt": 5, "threshold_rpt": False}
        self.data_config3 = {
            "threshold": True, "threshold_cnt": 5, "threshold_rpt": True}
        self.data_config4 = {
            "threshold": True, "threshold_cnt": 3, "threshold_rpt": False}
        self.data_config5 = {
            "threshold": True, "threshold_cnt": 3, "threshold_rpt": True}

        self.cfg = CfgTest()
        self.rmq = rmqcls.RabbitMQAdmin(self.cfg.user, self.cfg.japd)
        self.rmq2 = RabbitMQPub(self.cfg.user, self.cfg.japd)
        self.queues = []
        self.queues2 = [{"name": "PackageAdmin"}]
        self.queues3 = [{"name": "PackageAdmin"}, {"name": "PackageAdmin2"}]

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQPub")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_queues")
    def test_threshold_rpt_on_queue_meet(self, mock_rmq, mock_pub):

        """Function:  test_threshold_rpt_on_queue_meet

        Description:  Test with threshold report set to True and queue
            threshold meet.

        Arguments:

        """

        mock_rmq.return_value = self.queues2
        mock_pub.return_value = self.rmq2

        self.assertFalse(
            rmq_admin.queue_count(
                self.data_config5, self.dtg, rmq=self.rmq,
                method=self.rmq.list_nodes, dkey="Nodes"))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQPub")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_queues")
    def test_threshold_on_queue_meet(self, mock_rmq, mock_pub):

        """Function:  test_threshold_on_queue_meet

        Description:  Test with threshold set to True and queue meets
            threshold.

        Arguments:

        """

        mock_rmq.return_value = self.queues2
        mock_pub.return_value = self.rmq2

        self.assertFalse(
            rmq_admin.queue_count(
                self.data_config4, self.dtg, rmq=self.rmq,
                method=self.rmq.list_nodes, dkey="Nodes"))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQPub")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_queues")
    def test_threshold_rpt_on(self, mock_rmq, mock_pub):

        """Function:  test_threshold_rpt_on

        Description:  Test with threshold report set to True.

        Arguments:

        """

        mock_rmq.return_value = self.queues2
        mock_pub.return_value = self.rmq2

        self.assertFalse(
            rmq_admin.queue_count(
                self.data_config3, self.dtg, rmq=self.rmq,
                method=self.rmq.list_nodes, dkey="Nodes"))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQPub")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_queues")
    def test_threshold_on(self, mock_rmq, mock_pub):

        """Function:  test_threshold_on

        Description:  Test with threshold set to True.

        Arguments:

        """

        mock_rmq.return_value = self.queues2
        mock_pub.return_value = self.rmq2

        self.assertFalse(
            rmq_admin.queue_count(
                self.data_config2, self.dtg, rmq=self.rmq,
                method=self.rmq.list_nodes, dkey="Nodes"))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQPub")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_queues")
    def test_no_threshold(self, mock_rmq, mock_pub):

        """Function:  test_no_threshold

        Description:  Test with no threshold set.

        Arguments:

        """

        mock_rmq.return_value = self.queues2
        mock_pub.return_value = self.rmq2

        self.assertFalse(
            rmq_admin.queue_count(
                self.data_config, self.dtg, rmq=self.rmq,
                method=self.rmq.list_nodes, dkey="Nodes"))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQPub")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_queues")
    def test_multiple_queues(self, mock_rmq, mock_pub):

        """Function:  test_multiple_queues

        Description:  Test with multiple queue counts.

        Arguments:

        """

        mock_rmq.return_value = self.queues3
        mock_pub.return_value = self.rmq2

        self.assertFalse(
            rmq_admin.queue_count(
                self.data_config, self.dtg, rmq=self.rmq,
                method=self.rmq.list_nodes, dkey="Nodes"))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQPub")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_queues")
    def test_single_queue(self, mock_rmq, mock_pub):

        """Function:  test_single_queue

        Description:  Test with single queue count.

        Arguments:

        """

        mock_rmq.return_value = self.queues2
        mock_pub.return_value = self.rmq2

        self.assertFalse(
            rmq_admin.queue_count(
                self.data_config, self.dtg, rmq=self.rmq,
                method=self.rmq.list_nodes, dkey="Nodes"))

    @mock.patch("rmq_admin.data_out", mock.Mock(return_value=True))
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQPub")
    @mock.patch("rmq_admin.rabbitmq_class.RabbitMQAdmin.list_queues")
    def test_no_queues(self, mock_rmq, mock_pub):

        """Function:  test_no_queues

        Description:  Test with no queues detected.

        Arguments:

        """

        mock_rmq.return_value = self.queues
        mock_pub.return_value = self.rmq2

        self.assertFalse(
            rmq_admin.queue_count(
                self.data_config, self.dtg, rmq=self.rmq,
                method=self.rmq.list_nodes, dkey="Nodes"))


if __name__ == "__main__":
    unittest.main()
