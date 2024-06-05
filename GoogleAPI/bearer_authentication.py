#!/usr/bin/env python3

__AUTHOR__ = "Mark Van de Streek"
__VERSION__ = "1.0.0"
__DATE__ = "2024-03-11"

import requests


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
