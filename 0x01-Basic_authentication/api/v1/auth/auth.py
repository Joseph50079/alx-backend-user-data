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

        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        elif path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        if request is None or "Authorization" not in request.headers:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user
        """
        return None
