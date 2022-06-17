xshape is no longer in development. This repository is a read-only archive.

To plot xarray data using a shapefile, I suggest simply dumping into geopandas:

.. code-block:: python

    # for some DataArray da indexed by a single coordinate,
    # matching the values in a column of a shapefile

    import geopandas as gpd
    shp = gpd.read_file('some_shapefile').set_index(
        column_name_with_values_matching_da_coordinate)

    shp.assign(myvar=da.to_series()).plot('myvar')


If you'd like to take over development of xshape, feel free to reach out!
