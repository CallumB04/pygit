import argparse
import configparser
from datetime import datetime
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib

arg_parser = argparse.ArgumentParser()

# declares that CLI must have atleast one subcommand (init, commit, etc)
# dest="command" determines field name that subparser will return subcommand in
arg_subparsers = arg_parser.add_subparsers(title="Commands", dest="command")
arg_subparsers.required = True

def main(argv=sys.argv[1:]):
    args = arg_parser.parse_args(argv)

    # match first subcommand after 'pygit' to the relevant functions
    # each function will handle subcommand validation internally
    match args.command:
        case "add": cmd_add(args)
        case "cat-file": cmd_cat_file(args)
        case "check-ignore": cmd_check_ignore(args)
        case "checkout": cmd_checkout(args)
        case "commit": cmd_commit(args)
        case "hash-object": cmd_hash_object(args)
        case "init": cmd_init(args)
        case "log": cmd_log(args)
        case "ls-files": cmd_ls_files(args)
        case "ls-tree": cmd_ls_tree(args)
        case "rev-parse": cmd_rev_parse(args)
        case "rm": cmd_rm(args)
        case "show-ref": cmd_show_ref(args)
        case "status": cmd_status(args)
        case "tag": cmd_tag(args)
        case _: print("Invalid command.")