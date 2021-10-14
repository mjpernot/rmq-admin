#!/usr/bin/python
# Classification (U)

"""Program:  rmq_admin.py

    Description:  Adminstrates a RabbitMQ system.

    Usage:
        rmq_admin.py -c config_file -d dir_path
            {-N [-w] [-z] [-t ToEmail {ToEmail2 ...} {-s Subject Line}]
                [-o path/filename [-a]]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c config_file => RabbitMQ configuration file.
            Required argument.
        -d dir_path => Directory path for option '-c'.
            Required argument.

        -N -> Node health check.
            -w -> Print results of check for all returns.
            -z => Suppress standard out.
            -t to_email to_email2 => Enables emailing capability for an option
                if the option allows it.  Sends output to one or more email
                addresses.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to output file.

        -y value => A flavor id for the program lock.  To create unique lock.
        -v => Display version of this program.
        -h => Help and usage message.

        NOTE 1:  -v or -h overrides all other options.

        RabbitMQ configuration file format (config/rabbitmq.py.TEMPLATE).

            # RabbitMQ Configuration file
            user = "USER"
            japd = "PSWORD"
            host = "HOSTNAME"
            # RabbitMQ management port, default is 15672
            m_port = 15672
            # RabbitMQ listening port, default is 5672.
            q_port = 5672

    Example:
        rmq_admin.py -c rabbitmq -d config -N

"""

# Libraries and Global Variables

# Standard
from __future__ import print_function
import sys

# Third-party
import requests

# Local
import lib.arg_parser as arg_parser
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import version

__version__ = version.__version__

# Global
TAB_LEN = 4


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def create_base(cfg):

    """Function:  create_base

    Description:  Create base url to connect to RabbitMQ node.

    Arguments:
        (input) cfg -> Configuration module name.

    """

    http = "http"

    return http + "://" + cfg.host + ":" + str(cfg.m_port) + "/api/"


def fill_body(mail, data):

    """Function:  fill_body

    Description:  Add data to mail body from data list.

    Arguments:
        (input) mail -> Mail class instance.
        (input) data -> List of data strings.

    """

    data = list(data)

    for line in data:
        mail.add_2_msg(line)


def node_health(base_url, cfg, args_array):

    """Function:  node_health

    Description:  RabbitMQ Node health check.

    Arguments:
        (input) base_url -> Base URL for connection to RabbitMQ node.
        (input) cfg -> Configuration module name.
        (input) args_array -> Array of command line options and values.

    """

    global TAB_LEN

    mail = None
    verbose = args_array.get("-w", False)
    no_std = args_array.get("-z", False)
    ofile = args_array.get("-o", False)
    results = ["Node Health Check"]
    dtg = gen_libs.get_date() + " " + gen_libs.get_time()
    results.append(("\tAsOf: %s" % (dtg)).expandtabs(TAB_LEN))
    data = requests.get(base_url + "healthchecks/node",
                        auth=(cfg.user, cfg.japd)).json()
    mode = "a" if args_array.get("-a", False) else "w"

    if args_array.get("-t", False):
        mail = gen_class.setup_mail(
            args_array.get("-t"),
            subj=args_array.get("-s", "Node Health Check"))

    if data["status"] != "ok":
        results.append(("\tError detected in node").expandtabs(TAB_LEN))

        results.append(("\tStatus: %s" % (data["status"])).expandtabs(TAB_LEN))
        results.append(
            ("\tMessage: %s" % (data["reason"])).expandtabs(TAB_LEN))

    else:
        results.append(("\tStatus: %s" % (data["status"])).expandtabs(TAB_LEN))

    if (data["status"] != "ok" and not no_std) or (verbose and not no_std):
        gen_libs.print_list(results)

    if mail and (data["status"] != "ok" or verbose):
        fill_body(mail, results)
        mail.send_mail()

    if ofile and (data["status"] != "ok" or verbose):
        gen_libs.print_list(results, mode=mode, ofile=ofile)


def run_program(args_array, func_dict):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Set a program lock to prevent other instantiations from running.

    Arguments:
        (input) args_array -> Dict of command line options and values.
        (input) func_dict -> Dict of function calls and associated options.

    """

    args_array = dict(args_array)
    func_dict = dict(func_dict)
    cfg = gen_libs.load_module(args_array["-c"], args_array["-d"])
    base_url = create_base(cfg)

    # Intersect args_array & func_dict to find which functions to call.
    for opt in set(args_array.keys()) & set(func_dict.keys()):
        func_dict[opt](base_url, cfg, args_array)


def main(**kwargs):

    """Function:  main

    Description:  Initializes program-wide variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        file_chk_list -> contains the options which will have files included.
        file_crt_list -> contains options which require files to be created.
        func_dict -> dictionary list for the function calls or other options.
        opt_con_req_list -> contains the options that require other options.
        opt_multi_list -> contains the options that will have multiple values.
        opt_req_list -> contains options that are required for the program.
        opt_val_list -> contains options which require values.

    Arguments:
        (input) sys.argv -> Arguments from the command line.
        (input) **kwargs:
            argv_list -> List of arguments from another program.

    """

    cmdline = gen_libs.get_inst(sys)
    cmdline.argv = list(kwargs.get("argv_list", cmdline.argv))
    dir_chk_list = ["-d"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-N": node_health}
    opt_con_req_list = {"-s": ["-t"]}
    opt_multi_list = ["-s", "-t"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-o", "-t", "-s", "-y"]

    # Process argument list from command line.
    args_array = arg_parser.arg_parse2(
        cmdline.argv, opt_val_list, multi_val=opt_multi_list)

    if not gen_libs.help_func(args_array, __version__, help_message) \
       and not arg_parser.arg_require(args_array, opt_req_list) \
       and not arg_parser.arg_dir_chk_crt(args_array, dir_chk_list) \
       and not arg_parser.arg_file_chk(args_array, file_chk_list,
                                       file_crt_list) \
       and arg_parser.arg_cond_req(args_array, opt_con_req_list):

        try:
            prog_lock = gen_class.ProgramLock(
                cmdline.argv, args_array.get("-y", ""))
            run_program(args_array, func_dict)
            del prog_lock

        except gen_class.SingleInstanceException:
            print("rmq_admin lock in place for: %s"
                  % (args_array.get("-y", "")))


if __name__ == "__main__":
    sys.exit(main())
