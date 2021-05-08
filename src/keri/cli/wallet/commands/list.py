# -*- encoding: utf-8 -*-
"""
Use command ...

"""
import argparse
import os

parser = argparse.ArgumentParser(description='Set the context for what wallet to use')
parser.set_defaults(handler=lambda args: list(args.credentials, args.identifiers))
parser.add_argument('--credentials', '-c', help='list credentials')
parser.add_argument('--identifiers', '-i', help='list identifiers')


def list(c,r):
    print("listing", c, r)
