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


# Prerequisites:
  * List of Linux packages that need to be installed on the server.
    - git
    - python-pip

  * Local class/library dependencies within the program structure.
    - python-lib


# Installation:

Install the project using git.
  * From here on out, any reference to **{Python_Project}** or **PYTHON_PROJECT** replace with the baseline path of the python program.

```
umask 022
cd {Python_Project}
git clone git@sc.appdev.proj.coe.ic.gov:JAC-DSXD/rmq-admin.git
```

Install/upgrade system modules.

```
cd rmq-admin
sudo bash
umask 022
pip install -r requirements.txt --upgrade --trusted-host pypi.appdev.proj.coe.ic.gov
exit
```

Install supporting classes and libraries.

```
pip install -r requirements-python-lib.txt --target lib --trusted-host pypi.appdev.proj.coe.ic.gov
pip install -r requirements-rabbitmq-lib.txt --target rabbit_lib --trusted-host pypi.appdev.proj.coe.ic.gov
```

# Configuration:

Create RabbitMQ configuration file.

```
cd config
cp rabbitmq.py.TEMPLATE rabbitmq.py
```

Make the appropriate changes to the RabbitMQ environment.
  * Change these entries in the rabbitmq.py file.
  * The "user", "passwd", and "host" is connection to a RabbitMQ node.
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOSTNAME"
  * Only change these if you know what you are doing.
  * Managment port is m_port and Listening port is q_port.
    - m_port = 15672
    - q_port = 5672

```
vim rabbitmq.py
chmod 600 rabbitmq.py
```


# Program Help Function:

  All of the programs, except the command and class files, will have an -h (Help option) that will show display a help message for that particular program.  The help message will usually consist of a description, usage, arugments to the program, example, notes about the program, and any known bugs not yet fixed.  To run the help command:

```
`{Python_Project}/rmq-admin/rmq_admin.py -h`
```


# Testing:

# Unit Testing:

### Installation:

Install the project using the procedures in the Installation section.

### Testing:

```
cd {Python_Project}/rmq-admin
test/unit/rmq_admin/unit_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/rmq-admin
test/unit/rmq_admin/code_coverage.sh
```

# Integration Testing:

### Installation:

Install the project using the procedures in the Installation section.

# Configuration:
  * Please note that the integration testing will require access to a rabbitmq system to run the tests.

Create RabbitMQ configuration file.

```
cd test/integration/rmq_admin/config
cp ../../../../config/rabbitmq.py.TEMPLATE rabbitmq.py
```

Make the appropriate changes to the RabbitMQ environment.
  * Change these entries in the rabbitmq.py file.  The "user", "japd", and "host" variables are the connection information to a RabbitMQ node.
    - user = "USER"
    - japd = "PSWORD"
    - host = "HOSTNAME"

```
vim rabbitmq.py
chmod 600 rabbitmq.py
```

### Testing:

```
cd {Python_Project}/rmq-admin
test/integration/rmq_admin/integration_test_run.sh
```

### Code coverage:
```
cd {Python_Project}/rmq-admin
test/integration/rmq_admin/code_coverage.sh
```

