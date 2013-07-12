``monoseq``
===========

``monoseq`` is a Python library for pretty-printing sequence strings using a
monospace font. It also provides a simple command line interface.

Sequences are pretty-printed in the for DNA and proteins traditional way
using blocks of letters where each line is prefixed with the sequence
position. User-specified regions are highlighted using different formatting
styles. The output format can be HTML or plaintext with optional styling
using ANSI escape codes for use in a UNIX terminal.

::

    >>> import monoseq
    >>> sequence = 'MIMANQPLWLDSEVEMNHYQQSHIKSKSPYFPEDKHICWIKIFKAFGT' * 4
    >>> print monoseq.pprint_sequence(sequence, mode='plaintext')
      1  MIMANQPLWL DSEVEMNHYQ QSHIKSKSPY FPEDKHICWI KIFKAFGTMI MANQPLWLDS
     61  EVEMNHYQQS HIKSKSPYFP EDKHICWIKI FKAFGTMIMA NQPLWLDSEV EMNHYQQSHI
    121  KSKSPYFPED KHICWIKIFK AFGTMIMANQ PLWLDSEVEM NHYQQSHIKS KSPYFPEDKH
    181  ICWIKIFKAF GT


User documentation
------------------

New users should probably start here.

.. toctree::
   :maxdepth: 1

   install
   guide
   commands


API reference
-------------

Documentation on a specific function, class or method can be found in the API
reference.

.. toctree::
   :maxdepth: 2

   api


Additional notes
----------------

.. toctree::
   :maxdepth: 2

   development
   changelog
   copyright


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
