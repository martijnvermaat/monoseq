"""
``monoseq``, a Python library for pretty-printing sequence strings using a
monospace font.

.. moduleauthor:: Martijn Vermaat <martijn@vermaat.name>

.. Licensed under the MIT license, see the LICENSE.rst file.
"""


from .monoseq import (AnsiFormat, Format, HtmlFormat, partition_range,
                      PlaintextFormat, pprint_sequence)


# We follow a versioning scheme compatible with setuptools [1] where the
# package version is always that of the upcoming release (and not that of the
# previous release), post-fixed with ``.dev``. Only in a release commit, the
# ``.dev`` is removed (and added again in the next commit).
#
# Note that this scheme is not 100% compatible with SemVer [2] which would
# require ``-dev`` instead of ``.dev``.
#
# [1] http://peak.telecommunity.com/DevCenter/setuptools#specifying-your-project-s-version
# [2] http://semver.org/


__version_info__ = ('1', '0', '0')
__date__ = '13 Jul 2013'


__version__ = '.'.join(__version_info__)
__author__ = 'Martijn Vermaat'
__contact__ = 'martijn@vermaat.name'
__homepage__ = 'https://github.com/martijnvermaat/monoseq'
