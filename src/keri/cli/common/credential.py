# -*- encoding: utf-8 -*-
"""
keri.cli.common module

"""
import uuid


class Credential:
    def __init__(self, body):
        self.cid = str(uuid.uuid4())
        self.body = body
