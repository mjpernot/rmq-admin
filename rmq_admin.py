#!/usr/bin/python
# Classification (U)

"""Program:  rmq_admin.py

    Description:  Adminstrates a RabbitMQ system.

    Usage:
        rmq_admin.py -c config_file -d dir_path
            {-M [-w] [-z] [-t ToEmail {ToEmail2 ...} {-s Subject Line}]
                [-o path/filename [-a]] |
             -N [-w] [-z] [-t ToEmail {ToEmail2 ...} {-s Subject Line}]
                [-o path/filename [-a]] |
             -Q [-z] [-t ToEmail {ToEmail2 ...} {-s Subject Line}]
                [-o path/filename [-a]]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c config_file => RabbitMQ configuration file. Required argument.
        -d dir_path => Directory path for option '-c'. Required argument.

        -M -> List nodes
            -z => Suppress standard out.
            -t to_email to_email2 => Enables emailing capability for an option
                if the option allows it.  Sends output to one or more email
                addresses.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to output file.

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


def data_out(data, args, def_subj="NoSubjectLine"):

    """Function:  data_out

    Description:  Outputs the data in a variety of formats and media.

    Arguments:
        (input) data -> Data results from RabbitMQ command
        (input) args -> ArgParser class instance
        (input) def_subj -> Default subject line for email if not provided

    """

    if args.get_val("-t", def_val=False):
        mail = gen_class.setup_mail(
            args.get_val("-t"), subj=args.get_val("-s", def_val=def_subj))
        mail.add_2_msg(data)
        mail.send_mail()

    gen_libs.print_dict(
        data, ofile=args.get_val("-o", def_val=None),
        mode="a" if args.get_val("-a", def_val=False) else "w", json_fmt=True,
        no_std=args.get_val("-z", def_val=False))


def node_health(rmq, args, **kwargs):

    """Function:  node_health

    Description:  RabbitMQ Node health check.

    Arguments:
        (input) rmq -> RabbitMQAdmin class instance
        (input) args -> ArgParser class instance
        (input) kwargs:
            method -> Name of RabbitMQAdmin class method
            subj -> Subject line for email

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


def generic_call(rmq, args, **kwargs):

    """Function:  list_nodes

    Description:  Return list of nodes in a RabbitMQ cluster.

    Arguments:
        (input) rmq -> RabbitMQAdmin class instance
        (input) args -> ArgParser class instance
        (input) kwargs:
            method -> Name of RabbitMQAdmin class method
            subj -> Subject line for email

    """

    data = kwargs.get("method")()
    data_out(data, args, def_subj=kwargs.get("subj", None))


def run_program(args):

    """Function:  run_program

    Description:  Creates class instance and controls flow of the program.
        Set a program lock to prevent other instantiations from running.


    Arguments:
        (input) args -> ArgParser class instance

    """

    cfg = gen_libs.load_module(args.get_val("-c"), args.get_val("-d"))
    rmq = rabbitmq_class.RabbitMQAdmin(
        cfg.user, cfg.japd, host=cfg.host, port=cfg.m_port, scheme=cfg.scheme)

    # The func_dict variable will contain the key for the option selected and
    #   each option will contain the class method name, function name to call
    #   and the subject line for the email.  Enter "None" for subject if no
    #   email is required.  The "generic_call" is for most calls, only if other
    #   requirements are needed then call another function.
    func_dict = {
        "-M": {"method": rmq.list_nodes,
               "subj": "List_Nodes",
               "func": generic_call},
        "-N": {"method": node_health,
               "subj": "List_Nodes",
               "func": node_health},
        "-Q": {"method": rmq.list_queues,
               "subj": "List_Queues",
               "func": generic_call},
        }

    # Intersect args.args_array & func_dict to find which functions to call.
    for opt in set(args.args_array.keys()) & set(func_dict.keys()):
        func_dict[opt]["func"](
            rmq, args, method=func_dict[opt]["method"],
            subj=func_dict[opt]["subj"])


def main(**kwargs):

    """Function:  main

    Description:  Initializes program-wide variables and processes command
        line arguments and values.

    Variables:
        dir_chk_list -> contains options which will be directories.
        file_chk_list -> contains the options which will have files included.
        file_crt_list -> contains options which require files to be created.
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
            run_program(args)
            del prog_lock

        except gen_class.SingleInstanceException:
            print("rmq_admin lock in place for: %s"
                  % (args.get_val("-y", def_val="")))


if __name__ == "__main__":
    sys.exit(main())
