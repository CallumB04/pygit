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

import commands.init

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
        case "add": commands.add(args)
        case "cat-file": commands.cat_file(args)
        case "check-ignore": commands.check_ignore(args)
        case "checkout": commands.checkout(args)
        case "commit": commands.commit(args)
        case "hash-object": commands.hash_object(args)
        case "init": commands.init(args)
        case "log": commands.log(args)
        case "ls-files": commands.ls_files(args)
        case "ls-tree": commands.ls_tree(args)
        case "rev-parse": commands.rev_parse(args)
        case "rm": commands.rm(args)
        case "show-ref": commands.show_ref(args)
        case "status": commands.status(args)
        case "tag": commands.tag(args)
        case _: print("Invalid command.")