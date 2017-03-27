# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .compressors import RJSMinCompressor, RCSSMinCompressor


__all__ = ['RJSMinCompressor', 'RCSSMinCompressor', 'VERSION', 'get_version']


__version_info__ = '0.1.0'
__version__ = '0.1.0'
version = '0.1.0'
VERSION = '0.1.0'

def get_version():
    return version  # pragma: no cover
