#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  rmq_admin.py"
test/unit/rmq_admin/create_base.py
test/unit/rmq_admin/fill_body.py
test/unit/rmq_admin/help_message.py
test/unit/rmq_admin/main.py
test/unit/rmq_admin/node_health.py
test/unit/rmq_admin/run_program.py

