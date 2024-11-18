#!/usr/bin/env python3

""" Module of Auth views"""

from flask import json, request, abort
from typing import List, TypeVar


class Auth:
    """ Authentiction class

    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth
        Args:
            path: request path
            excluded_paths: list of paths that don't need authentication
        Return:
            True if the path is not in excluded_paths
        """

        if path is None or not excluded_paths:
            return True
        elif path[-1] != '/':
            path += '/'
        for excluded_path in excluded_paths:
            if excluded_path[-1] == '*':
                if path.startswith(excluded_path[:-1]):
                    return False
            else:
                if path == excluded_path:
                    return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ CURRENT USER"""

        if request is None:
            return None
        auth_header = request.headers.get("Authorization", None)
        print(auth_header)
        if auth_header is None:
            return None
        b64_header = self.extract_base64_authorization_header(
            auth_header)
        if b64_header is None:
            return None
        decoded_header = self.decode_base64_authorization_header(
            b64_header)
        if decoded_header is None:
            return None
        creditials = self.extract_user_credentials(decoded_header)
        if creditials is None:
            return None
        user = self.user_object_from_credentials(
            creditials[0], creditials[1])
        return user
