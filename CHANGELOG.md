# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


<<<<<<< HEAD
## [0.0.3] - 2021-12-06
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded rabbitmq-lib to v2.2.1
 
### Changed
- Converted imports to use Python 2.7 or Python 3.


=======
>>>>>>> d2949f9c489d26b40aa0fd748442b2789da7dc96
## [0.0.2] - 2021-10-14
- Added gen_class.RabbitMQAdmin class to handle RabbitMQ administration commands.
- Added a number of new command line options.

### Added
- generic_call: Generic call to a number of RabbitMQAdmin method calls.
- data_out: Outputs the data in a variety of formats and media.

### Changed
- node_health: Refactored the function to use the gen_class.RabbitMQAdmin class and data_out function.
- run_program: Replaced create_base call with gen_class.RabbitMQAdmin class instance and set up func_dict for calling functions and class methods.
- main: Removed func_dict, this was moved to run_program function.
- config/rabbitmq.py.TEMPLATE: Added new configuration options.
- main, run_program, node_health: Replaced processing of args_array with the gen_class.ArgParser class.

### Removed
- create_base
- fill_body


## [0.0.1] - 2020-07-22
- Initial development with node health check.

