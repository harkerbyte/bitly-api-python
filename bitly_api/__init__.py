from bitly_api import Connection, BitlyError, Error
__version__ = '0.3'
__author__ = "shade <cybersalimn@gmail.com>"
__all__ = ["Connection", "BitlyError", "Error"]
__doc__ = """
This is a python library for the bitly api

all methods raise BitlyError on an unexpected response, or a problem with input
format
"""
