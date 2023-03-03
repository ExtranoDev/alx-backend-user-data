#!/usr/bin/env python3
""""Regex-ing"""
import re
import logging
from typing import List
import os
import mysql.connector
PII_FIELDS = ("name", "email", "phone", "ssn", "password")
""" list of fields that can are considered as “important” PIIs """


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


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated
        Uses a regex to replace occurrences of certain field values"""
    for field in fields:
        message = re.sub(fr"{field}=.+?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """ create logger object, formatter and handler """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ using databse details returns a connector to the database """
    return mysql.connector.connect(
                host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
                database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
                user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
                password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))


def main():
    """"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()
    for row in result:
        message = f"name={row[0]};email={row[1]};phone={row[2]}" + \
                    "ssn={row[3]};password={row[4]};"
        print(message)
        log_record = logging.LogRecord("my_logger", logging.INFO,
                                       None, None, message, None, None)
        formatter = RedactingFormatter(PII_FILEDS)
        formatter.format(log_record)
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
