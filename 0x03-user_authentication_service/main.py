#!/usr/bin/env python3
"""End-to-end integration test"""
import request


def register_user(email: str, password: str) -> None:
    """"""
    user = {"email": email, "password": password}
    res = requests.post('http://localhost:5000/users', data=user)
    if res.status_code != 200:
        assert res.json() == {"message": "email already registered"}
    else:
        assert res.status_code == 200
        assert res.json() == {"email": f"{email}", "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """"""
    pass


def log_in(email: str, password: str) -> str:
    """"""
    pass


def profile_unlogged() -> None:
    """"""
    pass


def profile_logged(session_id: str) -> None:
    """"""
    pass


def log_out(session_id: str) -> None:
    """"""
    pass


def reset_password_token(email: str) -> str:
    """"""
    pass


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """"""
    pass


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    # log_in_wrong_password(EMAIL, NEW_PASSWD)
    # profile_unlogged()
    # session_id = log_in(EMAIL, PASSWD)
    # profile_logged(session_id)
    # log_out(session_id)
    # reset_token = reset_password_token(EMAIL)
    # update_password(EMAIL, reset_token, NEW_PASSWD)
    # log_in(EMAIL, NEW_PASSWD)
