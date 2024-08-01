#!/usr/bin/env python3
"""
Module contains filter_datum
"""
import re
from typing import (
    List,
)


def filter_datum(
    fields: List[str],
    replacer: str,
    message: str,
    separator: str,
) -> str:
    """
    This function filters the given message by replacing the specified\
        fields with the replacer string.

    Args:
        fields (str): A string containing the fields to be replaced.
        replacer (str): The string to replace the fields with.
        message (str): The message to be filtered.
        separator (str): The separator used to separate \
            the fields in the fields string.

    Returns:
        str: The filtered message.
    """
    for f in fields:
        message = re.sub(
            f"{f}=.*?{separator}",
            f"{f}={replacer}{separator}",
            message,
        )
    return message
