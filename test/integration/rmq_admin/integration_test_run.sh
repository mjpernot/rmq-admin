#!/bin/bash
# Unit testing program for the module.
# This will run all the units tests for this program.
# Will need to run this from the base directory where the module file
#   is located at.

echo ""
echo "Integration test:  rmq_admin.py"
/usr/bin/python test/integration/rmq_admin/node_health.py

