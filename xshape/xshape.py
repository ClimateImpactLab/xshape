# -*- coding: utf-8 -*-

from __future__ import absolute_import

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

import shapefile as pyshp

import xarray as xr

try:
    u = unicode
    string_types = (str, unicode)
except NameError:
    u = str
    string_types = (str, )


# TODO:
#   figure out how to use toolz.memoize to pre-process
#   polygon creation. currently fails for shapefile_overlay
#   because artists cannot be re-used
def parse_shapefile(shapefile, encoding='utf-8', **kwargs):
    '''
    read shapefile and return arrays of fields and polygons

    Parameters
    ----------
    shapefile : str
        Path to shapefile

    encoding : str, optional
        encoding of shapefile, default 'utf-8'

    **kwargs
        keyword arguments passed to :py:class:`matplotlib.patches.Polygon`
        constructor.

    Returns
    -------
    (fields, polygons) : (DataArray, array)
        returns a tuple of two objects. The first, a
        :py:class:`xarray.DataArray`, includes all of the records associated
        with shapes in the shapefile. The second, an :py:class:`~numpy.array`
        of :py:class:`matplotlib.patches.Polygon` objects, contains the shapes.

    '''

    shp = pyshp.Reader(shapefile)

    poly = np.array(list(map(
        lambda s: Polygon(s.points, **kwargs),
        shp.iterShapes())))

    try:
        records = np.array(shp.records())
    except UnicodeDecodeError:
        all_records = []
        for s in shp.iterRecords():
            record_values = []
            for e in s:
                if isinstance(e, string_types):
                    record_values.append(e)
                elif isinstance(e, bytes):
                    record_values.append(e.decode(encoding))
                else:
                    record_values.append(e)
            all_records.append(record_values)

        records = np.array(all_records)

    fields = (
        xr.DataArray(
            records,
            dims=('shape', 'field'),
            coords={
                'field': [f[0] for f in shp.fields[1:]],
                'shape': np.arange(shp.numRecords)})
        .to_dataset(dim='field'))

    return fields, poly


def choropleth(
        da,
        shapefile,
        dim=None,
        region_name=None,
        ax=None,
        clim=None,
        cmap='jet',
        encoding='utf-8',
        **kwargs):

    if dim is None:
        if len(da.dims) != 1:
            raise ValueError(
                'Cannot infer choropleth dimension on' +
                'DataArray with more than one dimension')

        dim = da.dims[0]

    if region_name is None:
        region_name = dim

    if ax is None:
        ax = plt.subplot(111)

    if clim is None:
        clim = [da.min(), da.max()]

    fields, poly = parse_shapefile(shapefile, encoding=encoding, closed=True)

    regions = fields[region_name].values

    geo_mask = np.in1d(regions, da[dim].values)

    poly = poly[geo_mask]
    regions = regions[geo_mask]

    color = da.sel(**{dim: regions}).values

    c = PatchCollection(poly, array=color, cmap=cmap, **kwargs)

    bbox = c.get_window_extent(ax).get_points()

    ax.set_xlim(bbox[0][0], bbox[1][0])
    ax.set_ylim(bbox[0][1], bbox[1][1])

    c.set_clim(clim)     # set the range of colorbar here
    ax.add_collection(c)
    plt.colorbar(c, ax=ax)

    return ax


def shapefile_overlay(da, shapefile, ax=None, encoding='utf-8', **kwargs):

    if ax is None:
        fig, ax = plt.subplots(1, 1)

    da.plot(ax=ax, **kwargs)

    fields, poly = parse_shapefile(
        shapefile,
        encoding=encoding,
        closed=False,
        fill=False,
        facecolor=None,
        edgecolor='black')

    for p in list(poly):
        ax.add_patch(p)

    return ax
