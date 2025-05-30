#!/bin/bash
# Unit test code coverage for SonarQube to cover all modules.
# This will run the Python code coverage module against all unit test modules.
# This will show the amount of code that was tested and which lines of code
#	that was skipped during the test.

coverage erase

echo ""
echo "Running unit test modules in conjunction with coverage"
coverage run -a --source=rmq_admin test/unit/rmq_admin/create_data_config.py
coverage run -a --source=rmq_admin test/unit/rmq_admin/create_filename.py
coverage run -a --source=rmq_admin test/unit/rmq_admin/create_header.py
coverage run -a --source=rmq_admin test/unit/rmq_admin/data_out.py
coverage run -a --source=rmq_admin test/unit/rmq_admin/generic_call.py
coverage run -a --source=rmq_admin test/unit/rmq_admin/help_message.py
coverage run -a --source=rmq_admin test/unit/rmq_admin/main.py
coverage run -a --source=rmq_admin test/unit/rmq_admin/node_health.py
coverage run -a --source=rmq_admin test/unit/rmq_admin/queue_count.py
coverage run -a --source=rmq_admin test/unit/rmq_admin/run_program.py

echo ""
echo "Producing code coverage report"
coverage combine
coverage report -m
coverage xml -i

