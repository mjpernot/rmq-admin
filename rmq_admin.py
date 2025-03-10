#!/usr/bin/python
# Classification (U)

"""Program:  rmq_admin.py

    Description:  Adminstrates a RabbitMQ system.

    Usage:
        rmq_admin.py -c config_file -d dir_path
            {
             [-C | -D | -E | -F | -L | -M | -O | -P | -Q | -U | -V]
                [-z] [-t ToEmail {ToEmail2 ...} {-s Subject Line}]
                [-o path/filename [-a]] |
             -N [-w] [-z] [-t ToEmail {ToEmail2 ...} {-s Subject Line}]
                [-o path/filename [-a]] |
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c config_file => RabbitMQ configuration file. Required argument.
        -d dir_path => Directory path for option '-c'. Required argument.

        -C -> List channels
        -D -> List connections
        -E -> List exchanges
        -F -> List consumers
        -L -> Get cluster name
        -M -> List nodes
        -O -> Show overview of node
        -P -> List permissions
        -Q -> List queues
        -U -> List users
        -V -> List vhosts
            -z => Suppress standard out.
            -t to_email to_email2 => Enables emailing capability for an option
                if the option allows it.  Sends output to one or more email
                addresses.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
            -o directory_path/file => Directory path and file name for output.
                -a => Append output to output file.

        -N -> Node health check
            -w -> Verbose, print results of check for all returns.
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
import sys

# Local
try:
    from .lib import gen_libs
    from .lib import gen_class
    from .rabbit_lib import rabbitmq_class
    from . import version

except (ValueError, ImportError) as err:
    import lib.gen_libs as gen_libs                     # pylint:disable=R0402
    import lib.gen_class as gen_class                   # pylint:disable=R0402
    import rabbit_lib.rabbitmq_class as rabbitmq_class  # pylint:disable=R0402
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

    data = dict(data)

    if args.get_val("-t", def_val=False):
        mail = gen_class.setup_mail(
            args.get_val("-t"), subj=args.get_val("-s", def_val=def_subj))
        mail.add_2_msg(data)
        mail.send_mail()

    gen_libs.print_dict(
        data, ofile=args.get_val("-o", def_val=None),
        mode="a" if args.arg_exist("-a") else "w", json_fmt=True,
        no_std=args.arg_exist("-z"))


def node_health(args, **kwargs):

    """Function:  node_health

    Description:  RabbitMQ Node health check.

    Arguments:
        (input) args -> ArgParser class instance
        (input) kwargs:
            rmq -> RabbitMQAdmin class instance
            method -> Name of RabbitMQAdmin class method
            subj -> Subject line for email

    """

    rmq = kwargs.get("rmq")
    dtg = gen_libs.get_date() + " " + gen_libs.get_time()
    results = {"Type": "Node Health Check", "AsOf": dtg}
    data = rmq.get(
        url=rmq.url + "/api/healthchecks/node", headers=rmq.headers,
        auth=rmq.auth)
    results["Status"] = data["status"]

    if data["status"] != "ok":
        results["Message"] = data["reason"]

    if data["status"] != "ok" or args.arg_exist("-w"):
        data_out(results, args, def_subj="Node_Health_Check")


def generic_call(args, **kwargs):

    """Function:  list_nodes

    Description:  Return list of nodes in a RabbitMQ cluster.

    Arguments:
        (input) rmq -> RabbitMQAdmin class instance
        (input) args -> ArgParser class instance
        (input) kwargs:
            rmq -> RabbitMQAdmin class instance
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
        "-C": {
            "method": rmq.list_channels, "subj": "List_Channels",
            "func": generic_call},
        "-D": {
            "method": rmq.list_connections, "subj": "List_Connections",
            "func": generic_call},
        "-E": {
            "method": rmq.list_exchanges, "subj": "List_Exchanges",
            "func": generic_call},
        "-F": {
            "method": rmq.list_consumers, "subj": "List_Consumers",
            "func": generic_call},
        "-L": {
            "method": rmq.get_cluster_name, "subj": "Cluster_Name",
            "func": generic_call},
        "-M": {
            "method": rmq.list_nodes, "subj": "List_Nodes",
            "func": generic_call},
        "-N": {
            "method": node_health, "subj": "List_Nodes", "func": node_health},
        "-O": {
            "method": rmq.overview, "subj": "Node_OverView",
            "func": generic_call},
        "-P": {
            "method": rmq.list_permissions, "subj": "List_Permissions",
            "func": generic_call},
        "-Q": {
            "method": rmq.list_queues, "subj": "List_Queues",
            "func": generic_call},
        "-U": {
            "method": rmq.list_users, "subj": "List_Users",
            "func": generic_call},
        "-V": {
            "method": rmq.list_vhosts, "subj": "List_Vhosts",
            "func": generic_call}}

    # Intersect args.args_array & func_dict to find which functions to call
    for opt in set(args.get_args_keys()) & set(func_dict.keys()):
        func_dict[opt]["func"](
            args, rmq=rmq, method=func_dict[opt]["method"],
            subj=func_dict[opt]["subj"])


def main():

    """Function:  main

    Description:  Initializes program-wide variables and processes command
        line arguments and values.

    Variables:
        dir_perms_chk -> contains directories and their octal permissions
        file_perm_chk -> file check options with their perms in octal
        file_crt -> contains options which require files to be created
        opt_con_req_list -> contains the options that require other options
        opt_multi_list -> contains the options that will have multiple values
        opt_req_list -> contains options that are required for the program
        opt_val_list -> contains options which require values

    Arguments:
        (input) sys.argv -> Arguments from the command line

    """

    dir_perms_chk = {"-d": 5}
    file_perm_chk = {"-o": 6}
    file_crt = ["-o"]
    opt_con_req_list = {"-s": ["-t"]}
    opt_multi_list = ["-s", "-t"]
    opt_req_list = ["-c", "-d"]
    opt_val_list = ["-c", "-d", "-o", "-t", "-s", "-y"]

    # Process argument list from command line
    args = gen_class.ArgParser(
        sys.argv, opt_val=opt_val_list, multi_val=opt_multi_list)

    if args.arg_parse2()                                                     \
       and not gen_libs.help_func(args, __version__, help_message)           \
       and args.arg_require(opt_req=opt_req_list)                            \
       and args.arg_dir_chk(dir_perms_chk=dir_perms_chk)                     \
       and args.arg_file_chk(file_perm_chk=file_perm_chk, file_crt=file_crt) \
       and args.arg_cond_req(opt_con_req=opt_con_req_list):

        try:
            prog_lock = gen_class.ProgramLock(
                sys.argv, args.get_val("-y", def_val=""))
            run_program(args)
            del prog_lock

        except gen_class.SingleInstanceException:
            print(f'rmq_admin lock in place for:'
                  f' {args.get_val("-y", def_val="")}')


if __name__ == "__main__":
    sys.exit(main())
