#!/usr/bin/env python3

""" Module of Auth views
"""

from flask import json, request, abort
from typing import List, TypeVar


class Auth:
    """ Authentiction class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
        """

        if path is None or not excluded_paths:
            return True
        elif path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str | None:
        """ authorization_header
        """
        if request is None:
            return None
        else:
            return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None
