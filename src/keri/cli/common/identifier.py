# -*- encoding: utf-8 -*-
"""
keri.cli.common module

"""


class Identifier:
    """
    kid - keri prefix
    psn - pseudonym provide by creator
    """

    def __init__(self, kid, psn):
        self.kid = kid
        self.psn = psn
