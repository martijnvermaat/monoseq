Command line interface
======================

Simple pretty-printing of sequences on the command line is done with the
``monoseq`` command. It reads a sequence from a file or from standard input
and accepts any number of subsequences to annotate.

Use the ``--help`` argument for more information.

Example::

    martijn@hue:~$ S=MIMANQPLWLDSEVEMNHYQQSHIKSKSPYFPEDKHICWIKIFKAFGT
    martijn@hue:~$ echo $S$S$S$S | monoseq -a 3 4 -a 97 145
      1  MIMANQPLWL DSEVEMNHYQ QSHIKSKSPY FPEDKHICWI KIFKAFGTMI MANQPLWLDS
     61  EVEMNHYQQS HIKSKSPYFP EDKHICWIKI FKAFGTMIMA NQPLWLDSEV EMNHYQQSHI
    121  KSKSPYFPED KHICWIKIFK AFGTMIMANQ PLWLDSEVEM NHYQQSHIKS KSPYFPEDKH
    181  ICWIKIFKAF GT

The actual annotation is not visible here, so you'll have to trust me on that.
Or try it yourself of course.
