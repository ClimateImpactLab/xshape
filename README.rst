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


Plotting regional data in a choropleth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the xarray extension, we can plot ``DataArray`` data directly:

.. ipython::

    In [1]: import xshape, xarray as xr, pandas as pd

    In [2]: df = pd.read_csv('tests/data/datasets/co-est2016.csv', encoding='latin1')
       ...: ca = df[(df['STATE'] == 6) & (df['COUNTY'] > 0)].copy()
       ...: ca['fips'] = df['STATE'] * 1000 + df['COUNTY']
       ...: da = ca.set_index(['fips'])['POPESTIMATE2016'].to_xarray()
       ...: da.coords['GEOID'] = ('fips', ), list(map('{:05}'.format, da.fips.values))
       ...: da = da.swap_dims({'fips': 'GEOID'})

    @savefig california_map.png width=4in
    In [3]: da.xshape.plot(
       ...:     'test/data/shapefiles/CA_counties/CA_counties',
       ...:     encoding='latin1',
       ...:     cmap='YlGnBu')



TODO
----

* Use shapefiles to reshape gridded/pixel data

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

