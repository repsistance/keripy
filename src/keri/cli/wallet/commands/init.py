# -*- encoding: utf-8 -*-
"""
keri.cli.wallet.commands module

"""
import argparse
import json

from keri.base import keeping
from keri.cli.common.wallet import Wallet, Identifier
from keri.core import eventing, coring

parser = argparse.ArgumentParser(description='Initialize a new wallet with a generated prefix')
parser.set_defaults(handler=lambda args: init(args.name, args.path))
parser.add_argument('name', help='Wallet name')
parser.add_argument('--path', help='filesystem location for wallet', default='/usr/local/var')


def init(name, path):
    with keeping.openKS(name=name, temp=False, headDirPath=path) as kpr:
        salt = coring.Salter().qb64
        w = Wallet(name)

        mgr = keeping.Manager(keeper=kpr, salt=salt)
        verfers, digers, cst, nst = mgr.incept(icount=1, ncount=1, transferable=True)

        keys = [verfers[0].qb64]

        nxt = coring.Nexter(digs=[digers[0].qb64]).qb64

        srdr = eventing.incept(keys=keys, nxt=nxt, code=coring.MtrDex.Blake3_256)
        i = json.loads(srdr.raw.decode("utf-8"))["i"]
        w.add_identifier(Identifier(i, 'root'))

        print(f'Initialized new identifier {i} for wallet {name}')
