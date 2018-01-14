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



Setting up this package
-----------------------

*Michael Delgado: complete these instructions and then remove this section from
the readme.*

1.  Create a matching repository on github if you haven't already:

    a.  go to https://github.com/organizations/ClimateImpactLab/repositories/new
    b.  enter the following information:

        owner
            ClimateImpactLab

        Repository Name
            xshape

        Description
            Tools for working with shapefiles, topographies, and polygons in xarray

        Privacy
            Public

        **Do not initialize the repo with a readme, license, or gitignore!**

    c.  Press the big green buttton

2.  Execute the following commands in this directory:

    .. code-block:: bash

        git init
        git add .
        git commit -m "initial commit"
        git remote add origin git@github.com:ClimateImpactLab/xshape.git
        git push -u origin master

3.  Set up automated testing, coverage, updates, and docs:

    a.  Set up testing

        i.      go to https://travis-ci.org/ and sign in/sign up with github.
                Make sure travis has access to the repositories on your github
                account *and* those owned by the ClimateImpactLab by enabling
                access in your account settings.
        ii.     Next to "My Repositories" click the '+' icon
        iii.    Flip the switch on ClimateImpactLab/xshape. If
                you don't see it in the list, click 'Sync account', and make
                sure you are looking at the ClimateImpactLab repositories.
        iv.     Push a change to your package (for example, you could delete
                this section). You should see tests start running on travis
                automatically.
        v.      Start writing tests for your code in the 
                ``xshape/tests`` folder. There are some
                examples already in there to get you started.

    b.  Set up docs

        i.      go to https://readthedocs.io and sign in/sign up with github.
                Same deal - make sure readthedocs has access to your github
                account and ClimateImpactLab.
        ii.     click 'Import a project', go to ClimateImpactLab, and refresh.
        iii.    click the '+' icon next to
                ClimateImpactLab/xshape. Pick a name for your
                project. The name has to be globally unique (not just within
                the ClimateImpactLab), so if you chose something with a common
                name you may have to rename the docs.
        iv.     go to the settings page for your new docs site, and navigate to the 'advanced settings' tab.
                add `requirements_rtd.txt` to the "requirements file" field.
        v.      next time you push code to master, docs should build
                automatically. You can view them at
                https://xshape.readthedocs.io/en/latest/
                (substitute whatever name you chose).


    c.  Set up updates

        i.      go to https://pyup.io. you know the drill.
        ii.     Go to your account, and click '+ Add Repo'. Sync.
        iii.    Add ClimateImpactLab/xshape
                with "Dependency Updates" and "SafetyCI" turned on. Leave 
                "Update Schedules" off.

    d.  Set up test coverage monitoring

        i.      next up: https://coveralls.io. you got this.

    e.  Breathe easy. The next time you push code, these should all update for
        you! Now that wasn't so bad, was it?

4.  Develop with github:

    a.  In general, it's best to file an issue when you want to change something
        or when you've found a bug, then write tests which test a-priori
        assertions about desired behavior, and then write the minimum amount of
        code required to pass these tests. See the contributing docs for more
        workflow suggestions.

        To run all tests on your local machine:

        .. code-block:: bash

            make test

5.  Deploy

    a.  Set up deployment by registering the package on the python package index
        (PyPI):

        i.      Create an account on PyPI: https://pypi.python.org/pypi
        ii.     Register the package:

                .. code-block:: bash

                    python setup.py register

        iii.    Encrypt & package your credentials so travis can deploy for you:

                .. code-block:: bash

                    python travis_pypi_setup.py

    b.  When you're ready to deploy this package, make sure all your changes are
        committed. Then run:

        .. code-block:: bash

            bumpversion patch # (or minor or major)
            git push
            git push --tags

        As soon as this new tagged commit passes tests, travis will deploy for
        you




    c.  Anyone (in the world) should now be able to install your package with

        .. code-block:: bash

            pip install [package-name]

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

