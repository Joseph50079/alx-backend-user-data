#!/usr/bin/env python3

""" Module of Auth views"""

from .auth import Auth
from typing import List, TypeVar
import base64


class BasicAuth(Auth):
    """ BasicAuth class

    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ extract_base64_authorizaton_header
        """

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
        # b_encoded = authorization_header[6:].encode('utf-8')
        # return base64.b64encode(b_encoded)

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode_base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(
                base64_authorization_header).decode('utf-8')
        except Exception:
            return None
