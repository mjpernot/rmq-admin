# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.1.3] - 2025-09-25
- Updated simplejson=3.19.2
- Added support for Python 3.13
- Updated mock==5.2.0
- Updated python-lib to v4.1.0
- Updated rabbitmq-lib to v2.4.2


## [0.1.2] - 2025-05-02
- Added option (-T) to view queue message counts.
- Added ability to check threshold queue message count (-j) option.
- Added ability to set threshold queue count (-x) option.
- Added ability to not report threshold queue if no queues meet threshold (-u) option.
- Updated rabbitmq-lib v2.4.0

### Added
- queue_count: RabbitMQ Queue count

### Changed
- main: Added "-x" to opt_val_list.
- create_data_config: Added "threshold" (-j), "threshold_cnt" (-x) and "threshold_rpt" (-u) options.
- run_program: Added -T option func_dict dictionary.
- Documentation changes.


## [0.1.1] - 2025-04-25
Breaking Change

- Updated python-lib v4.0.1
- Removed support for RabbitMQ v3.6/3.8/3.10
- Updated to work with RabbitMQ v4.0.4

### Added
- create_filename: Creates a filename for the attachment to an email.
- create_data_config: Create data out config parameters.
- create_header: Create standard header for JSON object.

### Changed
- data_out: Refactored the function to allow for email attachments for long data results and added pretty print command.
- generic_call: Added call to create_header for JSON object and add results of RabbitMQ call to the dictionary.
- run_program: Added calls to create_data_config and gen_class.TimeFormat to handle data configuration parameters and datetime group formats.
- node_health: Replaced creation of header with call to create_header and removed check to see if status is set to error status.
- Documentation changes.


## [0.1.0] - 2025-03-04
Alpha release

- Removed Python 2.7 code.
- Updated urllib3==1.26.20
- Added certifi==2024.12.14
- Updated python-lib==4.0.0
- Updated rabbitmq-lib==2.3.0

### Changed
- main: Converted string to f-string.
- Documentation updates.


## [0.0.10] - 2024-11-19
- Updated python-lib to v3.0.8
- Updated rabbitmq-lib to v2.2.8

### Fixed
- Set chardet==3.0.4 for Python 3.


## [0.0.9] - 2024-11-12
- Updated chardet==4.0.0 for Python 3.
- Added distro==1.9.0 for Python 3.
- Added idna==2.10 for Python 3.
- Updated pika==1.3.1 for Python 3.
- Added psutil==5.9.4 for Python 3.
- Updated requests==2.25.0 for Python 3.
- Updated urllib3==1.26.19 for Python 3.
- Updated six==1.16.0 for Python 3.
- Updated python-lib to v3.0.7
- Updated rabbitmq-lib to v2.2.7
        
### Deprecated
- Support for Python 2.7


## [0.0.8] - 2024-09-27
- Updated simplejson==3.13.2 for Python 3
- Updated python-lib to v3.0.5
- Updated rabbitmq-lib to v2.2.6


## [0.0.7] - 2024-08-08
- Updated simplejson==3.13.2
- Updated requests==2.25.0
- Added certifi==2019.11.28
- Added idna==2.10
- Updated rabbitmq-lib to v2.2.5

- ### Changed
- Updates to requirements.txt.


## [0.0.6] - 2024-07-31
- Set urllib3 to 1.26.19 for Python 2 for security reasons.
- Updated rabbitmq-lib to v2.2.4

### Changed
- main: Removed parsing from gen_class.ArgParser call and called arg_parse2 as part of "if" statement.


## [0.0.5] - 2024-03-06
- Updated to work in Red Hat 8
- Updated rabbitmq-lib to v2.2.3
- Updated python-lib to v3.0.3

### Changed
- Set simplejson to 3.12.0 for Python 3.
- Set chardet to 3.0.4 for Python 2.
- Documentation updates.


## [0.0.4] - 2023-10-18
- Upgraded python-lib to v2.10.1

### Fixed
- main: Fixed call to gen_libs.help_func by passing the gen_class.ArgParser instance.
- main: Fixed a number of errors when calling the gen_class.ArgParser methods.

### Changed
- main: Removed gen_libs.get_inst call.
- Documentation changes.


## [0.0.3] - 2021-12-06
- Updated to work in Python 3 too
- Upgraded python-lib to v2.9.4
- Upgraded rabbitmq-lib to v2.2.1
 
### Changed
- Converted imports to use Python 2.7 or Python 3.


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

