# -*- encoding: utf-8 -*-
"""
Use command ...

"""
import argparse
import os

parser = argparse.ArgumentParser(description='Set the context for what wallet to use')
parser.set_defaults(handler=lambda args: use(args.path, args.replace))
parser.add_argument('path', help='filesystem location for wallet')


def use(p, r):
    if r and os.path.isdir(p):
        os.rmdir(p)

    os.mkdir(p)
    print("Created new wallet at", p)
