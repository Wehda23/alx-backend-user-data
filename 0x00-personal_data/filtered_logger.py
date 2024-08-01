#!/usr/bin/env python3
"""
Module contains filter_datum
"""


def filter_datum(fields, replacer: str, message: str, separator: str) -> str:
    """
    This function filters the given message by replacing the specified fields with the replacer string.

    Args:
        fields (str): A string containing the fields to be replaced.
        replacer (str): The string to replace the fields with.
        message (str): The message to be filtered.
        separator (str): The separator used to separate the fields in the fields string.

    Returns:
        str: The filtered message.
    """
    filtered_message: str = ""
    if message.endswith(";"):
        message = message[:-1]
    for field in message.split(separator):
        key, value = field.split("=")
        if key in fields:
            value: str = replacer
        filtered_message += f"{key}={value};"
    return filtered_message
