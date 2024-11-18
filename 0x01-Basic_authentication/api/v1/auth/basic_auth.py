#!/usr/bin/env python3

""" Module of Auth views"""

from .auth import Auth
from typing import List, TypeVar
import base64
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extract_user_credentials"""

        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        user_pass = decoded_base64_authorization_header.split(':', 1)
        return user_pass[0], user_pass[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ user_object_from_crediantials"""

        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        if not User.search({'email': user_email}):
            return None
        else:
            user = User.search({'email': user_email})
            if not user[0].is_valid_password(user_pwd):
                return None
            return user[0]