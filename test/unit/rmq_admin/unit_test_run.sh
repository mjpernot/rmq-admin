#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Unit test:  rmq_admin.py"
/usr/bin/python test/unit/rmq_admin/data_out.py
/usr/bin/python test/unit/rmq_admin/generic_call.py
/usr/bin/python test/unit/rmq_admin/help_message.py
/usr/bin/python test/unit/rmq_admin/main.py
/usr/bin/python test/unit/rmq_admin/node_health.py
/usr/bin/python test/unit/rmq_admin/run_program.py

