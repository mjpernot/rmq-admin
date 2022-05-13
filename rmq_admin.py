#!/usr/bin/python
# Classification (U)

"""Program:  rmq_admin.py

    Description:  Adminstrates a RabbitMQ system.

    Usage:
        rmq_admin.py -c config_file -d dir_path
            {-N [-w] [-z] [-t ToEmail {ToEmail2 ...} {-s Subject Line}]
                [-o path/filename [-a]] |
             -Q [-z] [-t ToEmail {ToEmail2 ...} {-s Subject Line}]
                [-o path/filename [-a]]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c config_file => RabbitMQ configuration file. Required argument.
        -d dir_path => Directory path for option '-c'. Required argument.

        -N -> Node health check
            -w -> Print results of check for all returns.
            -z => Suppress standard out.
            -t to_email to_email2 => Enables emailing capability for an option
                if the option allows it.  Sends output to one or more email
                addresses.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to output file.

        -Q -> List queues
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
            port = 5672

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
import lib.gen_libs as gen_libs
import lib.gen_class as gen_class
import rabbit_lib.rabbitmq_class as rabbitmq_class
import version

__version__ = version.__version__


def help_message():

    """Function:  help_message

    Description:  Displays the program's docstring which is the help and usage
        message when -h option is selected.

    Arguments:

    """

    print(__doc__)


def list_queues(rmq, args):

    """Function:  list_queues

    Description:  Return list of queues in the RabbitMQ node.

    Arguments:
        (input) rmq -> RabbitMQAdmin class instance
        (input) args -> ArgParser class instance

    """

    data = rmq.list_queues()

    data_out(data, args, def_subj="List Queues")


def node_health(rmq, args):

    """Function:  node_health

    Description:  RabbitMQ Node health check.

    Arguments:
        (input) rmq -> RabbitMQAdmin class instance
        (input) args -> ArgParser class instance

    """

    mail = None
    verbose = args.get_val("-w", def_val=False)
    no_std = args.get_val("-z", def_val=False)
    ofile = args.get_val("-o", def_val=None)
    mode = "a" if args.get_val("-a", def_val=False) else "w"
    dtg = gen_libs.get_date() + " " + gen_libs.get_time()
    results = {"Type": "Node Health Check", "AsOf": dtg}
    data = rmq.get(
        url=rmq.url + "/api/healthchecks/node", headers=rmq.headers,
        auth=rmq.auth)
    results["Status"] = data["status"]

    if args.get_val("-t", def_val=False):
        mail = gen_class.setup_mail(
            args.get_val("-t"),
            subj=args.get_val("-s", def_val="Node Health Check"))

    if data["status"] != "ok":
        results["Message"] = data["reason"]

    if (data["status"] != "ok" and not no_std) or (verbose and not no_std):
        gen_libs.print_dict(results, json_fmt=True)

    if mail and (data["status"] != "ok" or verbose):
        mail.add_2_msg(results)
        mail.send_mail()

    if ofile and (data["status"] != "ok" or verbose):
        gen_libs.print_dict(
            results, ofile=ofile, mode=mode, json_fmt=True, no_std=True)


def run_program(args, func_dict):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Set a program lock to prevent other instantiations from running.

    Arguments:
        (input) args -> ArgParser class instance
        (input) func_dict -> Dict of function calls and associated options

    """

    func_dict = dict(func_dict)
    cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
    rmq = rabbitmq_class.RabbitMQAdmin(
        cfg.user, cfg.japd, host=cfg.host, port=cfg.m_port, scheme=cfg.scheme)

    # Intersect args.args_array & func_dict to find which functions to call.
    for opt in set(args.args_array.keys()) & set(func_dict.keys()):
        func_dict[opt](rmq, args)


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

    """

    dir_chk_list = ["-d"]
    file_chk_list = ["-o"]
    file_crt_list = ["-o"]
    func_dict = {"-N": node_health, "-Q": list_queues}
    opt_con_req_list = {"-s": ["-t"]}
    opt_multi_list = ["-s", "-t"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-o", "-t", "-s", "-y"]

    cmdline = gen_libs.get_inst(sys)

    # Process argument list from command line.
    args = gen_class.ArgParser(
        cmdline.argv, opt_val=opt_val_list, multi_val=opt_multi_list,
        do_parse=True)

    if not gen_libs.help_func(args.args_array, __version__, help_message) \
       and args.arg_require(opt_req=opt_req_list) \
       and args.arg_dir_chk_crt(dir_chk=dir_chk_list) \
       and args.arg_file_chk(file_chk=file_chk_list, file_crt=file_crt_list) \
       and args.arg_cond_req(opt_con_req=opt_con_req_list):

        try:
            prog_lock = gen_class.ProgramLock(
                cmdline.argv, args.get_val("-y", def_val=""))
            run_program(args, func_dict)
            del prog_lock

        except gen_class.SingleInstanceException:
            print("rmq_admin lock in place for: %s"
                  % (args.get_val("-y", def_val="")))


if __name__ == "__main__":
    sys.exit(main())
