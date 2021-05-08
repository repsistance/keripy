# -*- encoding: utf-8 -*-
"""
keri.cli.wallet.commands module

"""
import argparse
import os

parser = argparse.ArgumentParser(description='Create a new wallet')
parser.set_defaults(handler=lambda args: create(args.path, args.replace))
parser.add_argument('path', help='filesystem location for wallet')
parser.add_argument('-r', '--replace', action='store_true', help='replace any existing wallet at the given path',
                    default=False)


def create(p, r):
    if r and os.path.isdir(p):
        os.rmdir(p)

    os.mkdir(p)
    print("Created new wallet at", p)
