# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from pipeline.compressors import CompressorBase


__all__ = ['RJSMinCompressor', 'RCSSMinCompressor']


class RJSMinCompressor(CompressorBase):
    def compress_js(self, js):
        from rjsmin import jsmin
        return jsmin(js)


class RCSSMinCompressor(CompressorBase):
    def compress_css(self, css):
        from rcssmin import cssmin
        return cssmin(css)
