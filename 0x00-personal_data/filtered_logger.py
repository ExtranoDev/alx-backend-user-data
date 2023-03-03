#!/usr/bin/env python3
""""Regex-ing"""
import re
import logging
from typing import List
PII_FIELDS = ("name", "email", "phone", "ssn", "password")
""" list of fields that can are considered as “important” PIIs """


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated
        Uses a regex to replace occurrences of certain field values"""
    for field in fields:
        message = re.sub(fr"{field}=.+?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Initializing the Class """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records using filter_datum"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """ create logger object, formatter and handler """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    handler = logging.streamHandler()
    logger.propagate = False
    handler.setFormatter(RedactingFormatter())
    logger.addHandler(handler)
    return logger
