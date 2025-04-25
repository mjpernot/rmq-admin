#!/usr/bin/python
# Classification (U)

"""Program:  rmq_admin.py

    Description:  Adminstrates a RabbitMQ system.

    Usage:
        rmq_admin.py -c config_file -d dir_path
            {-C [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -D [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -E [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -F [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -L [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -M [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -O [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -P [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -Q [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -U [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -V [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]] |
             -N [-t to_email [to_email2 ...] [-s subject_line]]
                [-o dir_path/file [-a a|w]]] [-w] [-z] [-r [-k N]
                [-r [-f FileName] [-n] [-g] [-m]]]}
            [-y flavor_id]
            [-v | -h]

    Arguments:
        -c config_file => RabbitMQ configuration file.
        -d dir_path => Directory path for option '-c'.

        -C -> List channels
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -D -> List connections
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -E -> List exchanges
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -F -> List consumers
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -L -> Get cluster name
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -M -> List nodes
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -O -> Show overview of node
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -P -> List permissions
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -Q -> List queues
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -U -> List users
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -V -> List vhosts
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

        -N -> Node health check
            -t to_email_address(es) => Enables emailing and sends output to one
                    or more email addresses.  Email addresses are delimited by
                    a space.
                -s subject_line => Subject line of email.  If none is provided
                    then a default one will be used.
                -e => Attach data to email as attachment.
                    -f {file_name} => Name of file attachment.
                    -n => Add hostname to file attachment name.
                    -g => Add datetime to file attachment name.
                    -m => Add microseconds to file attachment name.
            -o dir_path/file => Directory path and file name for output.
                -a a|w => Append or write to output to output file.
                    Note: Default is write.
            -w -> Print results even if no errors detected.
            -z => Suppress standard out.
            -r => Expand the JSON format.
                -k N => Indentation for expanded JSON format.

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
import socket
import pprint

try:
    import simplejson as json
except ImportError:
    import json

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


def create_filename(dtg=None, **kwargs):

    """Function:  create_filename

    Description:  Creates a filename for the attachment to an email.

    Arguments:
        (input) dtg -> TimeFormat instance
        (input) kwargs:
            to_addr -> To email address
            subj -> Email subject line
            outfile -> Name of output file name
            mode -> w|a => Write or append mode for file
            use_pprint -> True|False - Use Pretty Print JSON object
            indent -> Indentation of JSON document if expanded
            suppress -> True|False - Suppress standard out
            report -> True|False - Report even if no error was detected
            def_subj -> Default subject line for email if not provided
            attach -> True|False - Attach data to email as attachment
            attach_file -> Name of file attachment
            add_host -> True|False - Add hostname to file attachment name
            add_dtg -> True|False - Add datetime to file attachment name
            add_micro -> True|False - Add microseconds to file attachment name
        (output) -> File name for the email attachment

    """

    join_list = []
    join_list.append(kwargs.get("attach_file", kwargs.get("subj")))

    if kwargs.get("add_host"):
        join_list.append(socket.gethostname())

    if kwargs.get("add_dtg"):
        join_list.append(dtg.get_time("zulu"))

    if kwargs.get("add_micro"):
        join_list.append(dtg.msecs)

    join_list.append("json")

    return ".".join(join_list)


def create_data_config(args):

    """Function:  create_data_config

    Description:  Create data out config parameters.

    Arguments:
        (input) args -> ArgParser class instance
        (output) data_config -> Dictionary for data out config parameters

    """

    data_config = {}
    data_config["to_addr"] = args.get_val("-t")
    data_config["subj"] = args.get_val("-s")
    data_config["outfile"] = args.get_val("-o")
    data_config["mode"] = args.get_val("-a", def_val="w")
    data_config["use_pprint"] = args.arg_exist("-r")
    data_config["indent"] = args.get_val("-k")
    data_config["suppress"] = args.arg_exist("-z")
    data_config["report"] = args.arg_exist("-w")
    data_config["attach"] = args.arg_exist("-e")
    data_config["attach_file"] = args.get_val("-f", def_val="RabbitmqAdmin")
    data_config["add_host"] = args.arg_exist("-n")
    data_config["add_dtg"] = args.arg_exist("-g")
    data_config["add_micro"] = args.arg_exist("-m")

    return data_config


def create_header(dtg, rmq):

    """Function:  create_header

    Description:  Create standard header for JSON object.

    Arguments:
        (input) dtg -> TimeFormat instance
        (input) rmq -> RabbitMQAdmin class instance
        (output) header -> Dictionary header for reports

    """

    header = {
        "Application": "RabbitMQ_Admin",
        "Node": rmq.host,
        "AsOf": dtg.get_time("zulu")}

    return header


def data_out(data, **kwargs):

    """Function:  data_out

    Description:  Outputs the data in a variety of formats and media.

    Arguments:
        (input) data -> Data results from RabbitMQ command
        (input) kwargs:
            dtg -> TimeFormat instance
            to_addr -> To email address
            subj -> Email subject line
            outfile -> Name of output file name
            mode -> w|a => Write or append mode for file
            use_pprint -> True|False - Use Pretty Print JSON object
            indent -> Indentation of JSON document if expanded
            suppress -> True|False - Suppress standard out
            report -> True|False - Report even if no error was detected
            def_subj -> Default subject line for email if not provided
            attach -> True|False - Attach data to email as attachment
            attach_file -> True|False - Name of file attachment
            add_host -> True|False - Add hostname to file attachment name
            add_dtg -> True|False - Add datetime to file attachment name
            add_micro -> True|False - Add microseconds to file attachment name

    """

    data = dict(data)
    cfg = {"indent": kwargs.get("indent", 4)} if kwargs.get("indent", False) \
        else {}

    if kwargs.get("to_addr") and kwargs.get("attach"):
        mail = gen_class.Mail2(
            kwargs.get("subj", kwargs.get("def_subj")), kwargs.get("to_addr"))
        fname = create_filename(**kwargs)
        mail.add_attachment(fname, "json", data)
        mail.send_email()

    elif kwargs.get("to_addr"):
        mail = gen_class.setup_mail(
            kwargs.get("to_addr"),
            subj=kwargs.get("subj", kwargs.get("def_subj")))
        mail.add_2_msg(json.dumps(data, **cfg))
        mail.send_mail()

    if kwargs.get("outfile", False) and kwargs.get("use_pprint", False):
        with open(kwargs.get("outfile"), mode=kwargs.get("mode", "w"),
                  encoding="UTF-8") as ofile:
            pprint.pprint(data, stream=ofile, **cfg)

    elif kwargs.get("outfile", False):
        gen_libs.write_file(
            kwargs.get("outfile"), kwargs.get("mode", "w"), data)

    if not kwargs.get("suppress", False) and kwargs.get("use_pprint", False):
        pprint.pprint(data, **cfg)

    elif not kwargs.get("suppress", False):
        print(data)


def node_health(data_config, dtg, rmq, **kwargs):

    """Function:  node_health

    Description:  RabbitMQ Node health check.

    Arguments:
        (input) data_config -> Dictionary of data configuration options
        (input) dtg -> TimeFormat instance
        (input) rmq -> RabbitMQAdmin class instance
        (input) kwargs:
            method -> Name of RabbitMQAdmin class method
            subj -> Subject line for email
            func -> Name of function

    """

    results = create_header(dtg, rmq)
    data = rmq.get(
        url=rmq.url + "/api/healthchecks/node", headers=rmq.headers,
        auth=rmq.auth)
    results["NodeHealth"] = data

    if data["status"] != "ok" or data_config["report"]:
        data_out(results, dtg=dtg, def_subj="Node_Health_Check", **data_config)


def generic_call(data_config, dtg, rmq, **kwargs):

    """Function:  list_nodes

    Description:  Return list of nodes in a RabbitMQ cluster.

    Arguments:
        (input) data_config -> Dictionary of data configuration options
        (input) dtg -> TimeFormat instance
        (input) rmq -> RabbitMQAdmin class instance
        (input) kwargs:
            method -> Name of RabbitMQAdmin class method
            subj -> Subject line for email
            dkey -> Dictionary key for the results
            func -> Name of function

    """

    results = create_header(dtg, rmq)
    results[kwargs.get("dkey")] = kwargs.get("method")()
    data_out(
        data, dtg=dtg, def_subj=kwargs.get("subj", "RabbitMQAdmin"),
        **data_config)


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
    data_config = dict(create_data_config(args))

    # The func_dict variable will contain the key for the option selected and
    #   each option will contain the class method name, function name to call
    #   the subject line for the email and the dictionary key which will
    #   contain the results the RabbitMQ command.  Enter "None" for subject if
    #   no email is required.  The "generic_call" is for most calls, only if
    #   other requirements are needed then call another function.
    func_dict = {
        "-C": {
            "method": rmq.list_channels, "def_subj": "List_Channels",
            "func": generic_call, "dkey": "Channels"},
        "-D": {
            "method": rmq.list_connections, "def_subj": "List_Connections",
            "func": generic_call, "dkey": "Connections"},
        "-E": {
            "method": rmq.list_exchanges, "def_subj": "List_Exchanges",
            "func": generic_call, "dkey": "Exchanges"},
        "-F": {
            "method": rmq.list_consumers, "def_subj": "List_Consumers",
            "func": generic_call, "dkey": "Consumers"},
        "-L": {
            "method": rmq.get_cluster_name, "def_subj": "Cluster_Name",
            "func": generic_call, "dkey": "ClusterName"},
        "-M": {
            "method": rmq.list_nodes, "def_subj": "List_Nodes",
            "func": generic_call, "dkey": "Nodes"},
        "-N": {
            "method": node_health, "def_subj": "List_Nodes",
            "func": node_health},
        "-O": {
            "method": rmq.overview, "def_subj": "Node_OverView",
            "func": generic_call, "dkey": "NodeOverView"},
        "-P": {
            "method": rmq.list_permissions, "def_subj": "List_Permissions",
            "func": generic_call, "dkey": "Permissions"},
        "-Q": {
            "method": rmq.list_queues, "def_subj": "List_Queues",
            "func": generic_call, "dkey": "Queues"},
        "-U": {
            "method": rmq.list_users, "subj": "List_Users",
            "func": generic_call, "dkey": "Users"},
        "-V": {
            "method": rmq.list_vhosts, "def_subj": "List_Vhosts",
            "func": generic_call, "dkey": "Vhosts"}}

    dtg = gen_class.TimeFormat()
    dtg.create_time()

    # Intersect args.args_array & func_dict to find which functions to call
    for opt in set(args.get_args_keys()) & set(func_dict.keys()):
        func_dict[opt]["func"](data_config, dtg, rmq, **func_dict[opt])


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
