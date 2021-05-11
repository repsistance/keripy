# -*- encoding: utf-8 -*-
"""
keri.cli.common module

"""
import itertools
import os
import shelve
import uuid


class Credential:
    def __init__(self, body):
        self.cid = str(uuid.uuid4())
        self.body = body


class Identifier:
    """
    kid - keri prefix
    psn - pseudonym provide by creator
    """

    def __init__(self, kid, psn):
        self.kid = kid
        self.psn = psn


class Wallet:
    """

    """

    def __init__(self, name='', path='/tmp'):
        self.store = path + os.sep + name

    def add_identifier(self, i: Identifier):
        d = shelve.open(self.store)
        d["id_" + i.kid] = i
        d.close()

    def get_identifier(self, kid):
        d = shelve.open(self.store)
        i = d["id_" + kid]
        d.close()

        return i

    def remove_identifier(self, kid):
        d = shelve.open(self.store)
        d.pop("id_" + kid)
        d.close()

    def list_identifiers(self):
        d = shelve.open(self.store)
        ids = list(itertools.takewhile(lambda i: i.startswith('id_'), iter(d)))
        ids = list(map(lambda i: i.removeprefix('id_'), ids))
        d.close()

        return ids

    def add_credential(self, c: Credential):
        d = shelve.open(self.store)
        d["cred_" + c.cid] = c
        d.close()

    def get_credential(self, cid):
        d = shelve.open(self.store)
        i = d["cred_" + cid]
        d.close()

        return i

    def remove_credential(self, cid):
        d = shelve.open(self.store)
        d.pop("cred_" + cid)
        d.close()

    def list_credentials(self):
        d = shelve.open(self.store)
        creds = list(itertools.takewhile(lambda i: i.startswith('cred_'), iter(d)))
        d.close()

        return creds

    def destroy(self):
        os.remove(self.store)
