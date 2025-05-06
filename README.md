# Python project for adminstration of RabbitMQ system.
# Classification (U)

# Description:
  Administration program for a RabbitMQ system.


###  This README file is broken down into the following sections:
 * Features
 * Prerequisites
 * Installation
 * Configuration
 * Running
 * Program Help Function
 * Testing
   - Unit
   - Integration


# Features:
 * RabbitMQ Node health check.
 * RabbitMQ Queue message count.
 * Check for threshold on queue message count.
 * Display variable aspects of the RabbitMQ process: List channels, connections, users, exchanges, consumers, nodes, permissions, queues, vhosts
 * Display overview health of the RabbitMQ node


# Prerequisites:
  * List of Linux packages that need to be installed on the server.
    - python3-pip
    - gcc


# Installation:

Install the project using git.

```
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/rmq-admin.git
```

Install/upgrade system modules.

NOTE: Install as the user that will run the program.

```
python -m pip install --user -r requirements3.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
```


Install supporting classes and libraries.

NOTE: Install as the user that will run the program.

```
python -m pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
python -m pip install -r requirements-rabbitmq-lib.txt --target rabbit_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```


# Configuration:

Create RabbitMQ configuration file.

Make the appropriate changes to the RabbitMQ environment.
  * Make the appropriate changes to connect to a RabbitMQ node/cluster.
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOSTNAME"
    - host_list = ["HOSTNAME:PORT", "HOSTNAME2:PORT"]
    - exchange_name = "EXCHANGE_NAME"
    - to_line = None
    - scheme = "https"
  * Only change these if you know what you are doing.
  * Managment port is m_port and Listening port is port.
    - port = 5672
    - m_port = 15672

```
cp config/rabbitmq.py.TEMPLATE config/rabbitmq.py
chmod 600 config/rabbitmq.py
vim config/rabbitmq.py
```


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
rmq_admin.py -h
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Testing:

```
test/unit/rmq_admin/unit_test_run.sh
test/unit/rmq_admin/code_coverage.sh
```

# Integration Testing:

### Installation:

Install the project using the procedures in the Installation section.

# Configuration:
  * Please note that the integration testing will require access to a rabbitmq system to run the tests.

Create RabbitMQ configuration file.

Make the appropriate changes to the RabbitMQ environment.
  * Change these entries in the rabbitmq.py file.  The "user", "japd", and "host" variables are the connection information to a RabbitMQ node.
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOSTNAME"

```
cp config/rabbitmq.py.TEMPLATE test/integration/rmq_admin/config/rabbitmq.py
chmod 600 test/integration/rmq_admin/config/rabbitmq.py
vim test/integration/rmq_admin/config/rabbitmq.py
```

### Testing:

```
test/integration/rmq_admin/integration_test_run.sh
test/integration/rmq_admin/code_coverage.sh
```

