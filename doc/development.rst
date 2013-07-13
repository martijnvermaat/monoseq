Development
===========

Development of ``monoseq`` happens on GitHub:
https://github.com/martijnvermaat/monoseq


Contributing
------------

Contributions to ``monoseq`` are very welcome! They can be feature requests,
bug reports, bug fixes, unit tests, documentation updates, or anything els you
may come up with.


Coding style
------------

In general, try to follow the `PEP 8`_ guidelines for Python code and `PEP
257`_ for docstrings.


Unit tests
----------

To run the unit tests with `nose`_, just run ``nosetests -v``.


Versioning
----------

A normal version number takes the form X.Y.Z where X is the major version, Y
is the minor version, and Z is the patch version. Development versions take
the form X.Y.Z.dev where X.Y.Z is the closest future release version.

Note that this scheme is not 100% compatible with `SemVer`_ which would
require X.Y.Z-dev instead of X.Y.Z.dev but `compatibility with setuptools
<http://peak.telecommunity.com/DevCenter/setuptools#specifying-your-project-s-version>`_
is more important for us. Other than that, version semantics are as described
by SemVer.

Releases are `published at PyPI <https://pypi.python.org/pypi/monoseq>`_ and
available from the GitHub git repository as tags.


Release procedure
^^^^^^^^^^^^^^^^^

Releasing a new version is done as follows:

1. Make sure the section in the ``CHANGES`` file for this release is
   complete and there are no uncommitted changes.

   .. note::

    Commits since release X.Y.Z can be listed with ``git log vX.Y.Z..`` for
    quick inspection.

2. Update the ``CHANGES`` file to state the current date for this release
   and edit ``monoseq/__init__.py`` by updating `__date__` and removing the
   ``dev`` value from `__version_info__`.

   Commit and tag the version update::

       git commit -am 'Bump version to X.Y.Z'
       git tag -a 'vX.Y.Z'
       git push --tags

3. Upload the package to PyPI::

       python setup.py sdist upload

4. Add a new entry at the top of the ``CHANGES`` file like this::

       Version X.Y.Z+1
       ---------------

       Release date to be decided.

   Increment the patch version and add a ``dev`` value to `__version_info__`
   in ``monoseq/__init__.py`` and commit these changes::

       git commit -am 'Open development for X.Y.Z+1'


Todo
----

These are some general todo notes. More specific notes can be found by
grepping the source code for ``Todo``.

* Read annotations from BED track.
* User guide.
* User definable stylings.
* Example CSS rules for HTML format.


.. _nose: https://nose.readthedocs.org/
.. _PEP 8: http://www.python.org/dev/peps/pep-0008/
.. _PEP 257: http://www.python.org/dev/peps/pep-0257/
.. _SemVer: http://semver.org/
