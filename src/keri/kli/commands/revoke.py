# -*- encoding: utf-8 -*-
"""
keri.kli.commands module

"""
import argparse

from keri.base import keeping
from keri.base.basing import Habitat
from keri.db import dbing
from keri.vdr.issuing import Issuer

parser = argparse.ArgumentParser(description='Revoke a verifiable credential')
parser.set_defaults(handler=lambda args: issue(args.name, args.vcdig))
parser.add_argument('--name', '-n', help='Humane reference')
parser.add_argument('--vcdig', help='vcdig is hash digest of vc content qb64')


def issue(name, vcdig):
    with dbing.openDB(name=name, temp=False) as db, keeping.openKS(name=name, temp=False) as ks:
        hab = Habitat(name=name, ks=ks, db=db, temp=False)
        iss = Issuer(hab=hab, name=name)

        iss.revoke(vcdig=vcdig)
