# -*- coding: utf-8 -*-

from __future__ import absolute_import

"""Top-level package for xshape."""

__author__ = """Michael Delgado"""
__email__ = 'delgado.michaelt@gmail.com'
__version__ = '0.1.1'

from xshape.accessors import (
    XShapeDataArrayAccessor,
    XShapeDatasetAccessor)

from xshape.xshape import (
    parse_shapefile)

_module_imports = (
    XShapeDataArrayAccessor,
    XShapeDatasetAccessor,
    parse_shapefile
)

__all__ = list(map(lambda x: x.__name__, _module_imports))
