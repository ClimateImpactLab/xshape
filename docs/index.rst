======
xshape
======


.. image:: https://img.shields.io/pypi/v/xshape.svg
        :target: https://pypi.python.org/pypi/xshape

.. image:: https://img.shields.io/travis/ClimateImpactLab/xshape.svg
        :target: https://travis-ci.org/ClimateImpactLab/xshape

.. image:: https://readthedocs.org/projects/xshape/badge/?version=latest
        :target: https://xshape.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/ClimateImpactLab/xshape/shield.svg
     :target: https://pyup.io/repos/github/ClimateImpactLab/xshape/
     :alt: Updates


Tools for working with shapefiles, topographies, and polygons in xarray


* Free software: MIT license
* Documentation: https://xshape.readthedocs.io.


Features
--------

* Read a shapefile and obtain an xarray DataArray of field records
* Draw shapefile boundaries on gridded data
* Plot xarray DataArray data indexed by shapefile records as a choropleth

Usage
-----

Getting records for fields in a shapefile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ipython::

    In [1]: import xshape

    In [2]: fields, polygons = xshape.parse_shapefile(
       ...:     '../tests/data/shapefiles/CA_counties/CA_counties',
       ...:     encoding='latin1')

    In [3]: fields


Drawing shape boundaries on gridded data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ipython::

    In [4]: import xarray as xr, numpy as np, xshape

    # generate sample data
    In [5]: da = xr.DataArray(
       ...:    np.cos((
       ...:         np.arange(41*45).reshape((41, 45)) * np.arange(41*45).reshape((45, 41)
       ...:         ).T)/4e5),
       ...:    dims=('lat', 'lon'),
       ...:    coords={
       ...:        'lon': np.linspace(-125, -114, 45),
       ...:        'lat': np.linspace(32, 42, 41)})
       ...:

    @savefig california_map.png width=4in
    In [6]: da.xshape.overlay(
       ...:     '../tests/data/shapefiles/CA_counties/CA_counties',
       ...:     encoding='latin1',
       ...:     cmap='YlGnBu');
       ...:


Plotting regional data in a choropleth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the xarray extension, we can plot ``DataArray`` data directly:

.. ipython::

    In [7]: import xshape, xarray as xr, pandas as pd

    In [8]: df = pd.read_csv('../tests/data/datasets/co-est2016.csv', encoding='latin1')
       ...: ca = df[(df['STATE'] == 6) & (df['COUNTY'] > 0)].copy()
       ...: ca['fips'] = df['STATE'] * 1000 + df['COUNTY']
       ...: da = ca.set_index(['fips'])['POPESTIMATE2016'].to_xarray()
       ...: da.coords['GEOID'] = ('fips', ), list(map('{:05}'.format, da.fips.values))
       ...: da = da.swap_dims({'fips': 'GEOID'})

    @savefig california_map_pop.png width=4in
    In [9]: da.xshape.plot(
       ...:     '../tests/data/shapefiles/CA_counties/CA_counties',
       ...:     encoding='latin1',
       ...:     cmap='YlGnBu');
       ...:

We can also combine the information from the fields with the data contained in the DataArray:

.. ipython::

    In [10]: land_area = (
       ....:     fields
       ....:     .set_coords('GEOID')
       ....:     .swap_dims({'shape': 'GEOID'})
       ....:     .ALAND.astype(float))

    @savefig california_map_pop_per_m2.png width=4in
    In [11]: np.log(da / land_area).xshape.plot(
       ....:     '../tests/data/shapefiles/CA_counties/CA_counties',
       ....:     encoding='latin1',
       ....:     cmap='YlGnBu');
       ....:

Contents
--------

.. toctree::
   :maxdepth: 2

   installation
   usage
   modules
   contributing
   authors
   history

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
