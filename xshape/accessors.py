
from __future__ import absolute_import

import xarray as xr
from xshape.xshape import choropleth, shapefile_overlay


@xr.register_dataarray_accessor('xshape')
class XShapeDataArrayAccessor(object):
    '''

    '''

    def __init__(self, xarray_obj):
        self._obj = xarray_obj

    def plot(
            self,
            shapefile,
            dim=None,
            region_name=None,
            ax=None,
            clim=None,
            cmap='jet',
            **kwargs):

        return choropleth(
            self._obj,
            shapefile=shapefile,
            dim=dim,
            region_name=region_name,
            ax=ax,
            clim=clim,
            cmap=cmap,
            **kwargs)

    def overlay(
            self,
            shapefile,
            ax=None,
            encoding='utf-8',
            **kwargs):

        return shapefile_overlay(
            self._obj, shapefile=shapefile, ax=ax, encoding=encoding, **kwargs)


@xr.register_dataset_accessor('xshape')
class XShapeDatasetAccessor(object):
    pass
