#!/usr/bin/env python3
# @Author: shengtudai
# @Date: 2023-03-29 12:00:00
# @Description: This script is used for sending private/group messages via HTTP API.
# @filename: notify.py


import requests


def private_notice(msg, url, qq):
    """
    Send a private message to the specified user via HTTP API.

    Args:
        msg (str): The content of the message.
        url (str): The URL of the HTTP API.
        qq (str): The user qq of the recipient.

    Returns:
        int: 1 if the message was sent successfully, otherwise 0.
    """
    post_url = url
    post_msg = {
        "message_type": "private",
        "message": msg,
        "user_id": qq
    }
    try:
        requests.get(post_url, params=post_msg)
    except Exception as e:
        print(e)
        return 0
    return 1


def group_notice(msg, url, qq):
    """
    Send a group message to the specified group via HTTP API.

    Args:
        msg (str): The content of the message.
        url (str): The URL of the HTTP API.
        qq (str): The group qq of the recipient.

    Returns:
        int: 1 if the message was sent successfully, otherwise 0.
    """
    post_url = url
    post_msg = {
        "message_type": "group",
        "message": msg,
        "group_id": qq
    }
    try:
        requests.get(post_url, params=post_msg)
    except Exception as e:
        print(e)
        return 0
    return 1
