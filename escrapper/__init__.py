""" Package escrapper, various objects to scrapp code portals
"""
from __future__ import absolute_import

from .websvn import WebSVN
from .exceptions import InvalidWebSVN

__all__ = ['WebSVN', 'InvalidWebSVN', ]
__author__ = "Espartaco Palma"
__version__ = "0.3.0"

