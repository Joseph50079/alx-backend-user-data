#!/usr/bin/env python3

""" Module of Auth views
"""

from flask import jsonify, request, abort

class Auth:
    """ Authentiction class
    """
    
    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        """ require_auth
        """
        return False
    
    def authorization_header(self, request=None) -> str:
        """ authorization_header
        """
        return None