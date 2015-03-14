__author__ = 'will@threadtheweb.co.uk'
# Error handling in SQLSploit

class DatabaseError(Exception):
    """
        DB Exception
    """


class Error(DatabaseError):
    """
        Generic DB Error
    """


class ParamError(Exception):
    """
        Errors with CLI parameters
    """


class AuthError(Exception):
    """
        Error with DB authentication
    """


class ConnectionLost(Exception):
    """
        Database Connection Dropped
    """