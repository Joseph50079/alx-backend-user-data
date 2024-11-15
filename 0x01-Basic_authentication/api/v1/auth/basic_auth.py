#!/usr/bin/env python3

""" Module of Auth views"""

from .auth import Auth


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