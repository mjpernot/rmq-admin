# Changelog
All notable changes to this project will be documented in this file.

The format is based on "Keep a Changelog".  This project adheres to Semantic Versioning.


## [0.0.2] - 2021-10-14
### Changed
- node_health: Replace current api call with RabbitMQAdmin class, changed output from list to dictionary format, removed fill_body call.
- run_program: Replaced create_base call with gen_class.RabbitMQAdmin class instance.
- config/rabbitmq.py.TEMPLATE: Added new configuration options.
- main, run_program, node_health: Replaced processing of args_array with the gen_class.ArgParser class.

### Removed
- create_base
- fill_body


## [0.0.1] - 2020-07-22
- Initial development with node health check.

