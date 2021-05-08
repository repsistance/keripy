# -*- encoding: utf-8 -*-
"""
tests.cli.wallet module

"""

from keri.cli.common.wallet import Wallet, Identifier, Credential


def test_wallet_with_identifiers():
    p = "prefix"
    w = Wallet('test')

    ids = w.list_identifiers()
    assert len(ids) == 0

    i = Identifier(p, "name")
    w.add_identifier(i)
    ids = w.list_identifiers()
    assert len(ids) == 1

    actual = w.get_identifier(p)
    assert actual.kid == "prefix"
    assert actual.psn == "name"

    w.remove_identifier(p)
    ids = w.list_identifiers()
    assert len(ids) == 0

    w.destroy()


def test_wallet_with_credentials():
    w = Wallet('cred_test')
    creds = w.list_credentials()
    assert len(creds) == 0

    c = Credential({'foo': 'bar'})
    w.add_credential(c)
    creds = w.list_credentials()
    assert len(creds) == 1

    actual = w.get_credential(c.cid)
    assert actual.body['foo'] == 'bar'

    w.remove_credential(c.cid)
    creds = w.list_credentials()
    assert len(creds) == 0

    w.destroy()
