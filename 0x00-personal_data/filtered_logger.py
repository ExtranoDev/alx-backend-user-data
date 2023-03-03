#!/usr/bin/env python3
""""Regex-ing"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log message obfuscated
        Uses a regex to replace occurrences of certain field values"""
    for field in fields:
        message = re.sub(fr"{field}=.+?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
