Django Vite Example
============

A reusable Django app integrated with vite.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install djv-example

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://VAR_GITHUB_REPO.git#egg=djv_example

TODO: Describe further installation steps (edit / remove the examples below):

Add ``djv_example`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'djv_example',
    )

Add the ``djv_example`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = [
        path('djv_example/', include('djv_example.urls')),
    ]

Before your tags/filters are available in your templates, load them by using

.. code-block:: html

	{% load djv_example_tags %}


Don't forget to migrate your database

.. code-block:: bash

    ./manage.py migrate djv_example


Usage
-----

TODO: Describe usage or point to docs. Also describe available settings and
templatetags.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python3 djv-example
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.8 and Django 1.9) and run the tests against both
environments.
