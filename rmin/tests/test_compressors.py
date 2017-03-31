# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import pytest
from django.contrib.staticfiles.finders import AppDirectoriesFinder
from django.utils.encoding import force_text
from rmin import RCSSMinCompressor, RJSMinCompressor


@pytest.fixture
def cssmin():
    return RCSSMinCompressor(verbose=True).compress_css

@pytest.fixture
def jsmin():
    return RJSMinCompressor(verbose=True).compress_js


def test_cssminifcation(cssmin):
    css = """
    body { color: red; }
    head {
        display: block;
    }
    x { font: 1px }
    """
    output = cssmin(css)
    assert output == "body{color:red}head{display:block}x{font:1px}"


@pytest.mark.parametrize("filename", (
    ("admin/css/base.css"),
    ("admin/css/changelists.css"),
    ("admin/css/forms.css"),
))
def test_cssminifcation_of_adminfiles(cssmin, filename):
    filepath = AppDirectoriesFinder().find(filename)
    with open(filepath, 'rb') as f:
        css = force_text(f.read())
    out = cssmin(css)
    assert len(css) > len(out)


def test_jsminifcation(jsmin):
    js = """
    var x = 1;
    var y = {
        'this':
        'is',
        a: 'test'
    }
    var z = new Date();
    """
    output = jsmin(js)
    assert output == """var x=1;var y={'this':'is',a:'test'}
var z=new Date();"""


@pytest.mark.parametrize("filename", (
    ("admin/js/SelectBox.js"),
    ("admin/js/actions.js"),
    ("admin/js/urlify.js"),
))
def test_jsminifcation_of_adminfiles(cssmin, filename):
    filepath = AppDirectoriesFinder().find(filename)
    with open(filepath, 'rb') as f:
        css = force_text(f.read())
    out = cssmin(css)
    assert len(css) > len(out)
