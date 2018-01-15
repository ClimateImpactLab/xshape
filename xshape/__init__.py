# -*- coding: utf-8 -*-

from __future__ import absolute_import

"""Top-level package for xshape."""

__author__ = """Michael Delgado"""
__email__ = 'delgado.michaelt@gmail.com'
__version__ = '0.2.0'

from xshape.accessors import (
    XShapeDataArrayAccessor,
    XShapeDatasetAccessor)

from xshape.xshape import (
    parse_shapefile)

__all__ = [
    XShapeDataArrayAccessor,
    XShapeDatasetAccessor,
    parse_shapefile]
