``monoseq``
===========

``monoseq`` is a Python library for pretty-printing DNA and protein sequences
using a monospace font. It also provides a simple command line interface.

Sequences are pretty-printed in the traditional way using blocks of letters
where each line is prefixed with the sequence position. User-specified regions
are highlighted and the output format can be HTML or plaintext with optional
styling using ANSI escape codes for use in a terminal.

A simple example::

    >>> from monoseq import pprint_sequence
    >>> sequence = 'MIMANQPLWLDSEVEMNHYQQSHIKSKSPYFPEDKHICWIKIFKAFGT' * 4
    >>> print pprint_sequence(sequence)
      1  MIMANQPLWL DSEVEMNHYQ QSHIKSKSPY FPEDKHICWI KIFKAFGTMI MANQPLWLDS
     61  EVEMNHYQQS HIKSKSPYFP EDKHICWIKI FKAFGTMIMA NQPLWLDSEV EMNHYQQSHI
    121  KSKSPYFPED KHICWIKIFK AFGTMIMANQ PLWLDSEVEM NHYQQSHIKS KSPYFPEDKH
    181  ICWIKIFKAF GT

An example, admittedly contrived, with annotations:

.. raw:: html

    <div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">monoseq</span> <span class="kn">import</span> <span class="n">AnsiFormat</span>
    <span class="gp">&gt;&gt;&gt; </span><span class="n">twelves</span> <span class="o">=</span> <span class="p">[(</span><span class="n">p</span><span class="p">,</span> <span class="n">p</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">11</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">sequence</span><span class="p">),</span> <span class="mi">12</span><span class="p">)]</span>
    <span class="gp">&gt;&gt;&gt; </span><span class="n">conserved</span> <span class="o">=</span> <span class="p">[[(</span><span class="mi">11</span><span class="p">,</span> <span class="mi">37</span><span class="p">),</span> <span class="p">(</span><span class="mi">222</span><span class="p">,</span> <span class="mi">247</span><span class="p">)]</span>
    <span class="gp">&gt;&gt;&gt; </span><span class="n">middle</span> <span class="o">=</span> <span class="p">[(</span><span class="nb">len</span><span class="p">(</span><span class="n">sequence</span><span class="p">)</span> <span class="o">/</span> <span class="mi">3</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">sequence</span><span class="p">)</span> <span class="o">/</span> <span class="mi">3</span> <span class="o">*</span> <span class="mi">2</span><span class="p">)]</span>
    <span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">pprint_sequence</span><span class="p">(</span><span class="n">sequence</span><span class="p">,</span> <span class="n">format</span><span class="o">=</span><span class="n">AnsiFormat</span><span class="p">,</span>
    <span class="gp">... </span>                      <span class="n">annotations</span><span class="o">=</span><span class="p">[</span><span class="n">conserved</span><span class="p">,</span> <span class="n">twelves</span><span class="p">,</span> <span class="n">middle</span><span class="p">])</span>
    <span class="go">  1  cgcactcaaa a<span style="color:red"><span style="font-weight:bold">c</span>aaaggaag acc<span style="font-weight:bold">g</span>tcctcg actgc<span style="font-weight:bold">a</span>g</span>agg aagcagg<span style="font-weight:bold">a</span>ag ctgtcggcc<span style="font-weight:bold">c</span></span>
    <span class="go"> 61  agctctgagc c<span style="font-weight:bold">c</span>agctgctg gag<span style="font-weight:bold">c</span>cccg<span style="text-decoration:underline">ag cagcg<span style="font-weight:bold">g</span>catg gagtccg<span style="font-weight:bold">t</span>gg ccctgtaca<span style="font-weight:bold">g</span></span></span>
    <span class="go">121  <span style="text-decoration:underline">ctttcaggct a<span style="font-weight:bold">c</span>agagagcg acg<span style="font-weight:bold">a</span>gctggc cttca<span style="font-weight:bold">a</span>caag ggagaca<span style="font-weight:bold">c</span>ac tcaaga</span>tcc<span style="font-weight:bold">t</span></span>
    <span class="go">181  gaacatggag g<span style="font-weight:bold">a</span>tgaccaga act<span style="font-weight:bold">g</span>gtacaa ggccg<span style="font-weight:bold">a</span>gctc cg<span style="color:red">gggtg<span style="font-weight:bold">t</span>cg agggattta<span style="font-weight:bold">t</span></span></span>
    <span class="go">241  <span style="color:red">tcccaag</span>aac t<span style="font-weight:bold">a</span>catccgcg tca<span style="font-weight:bold">a</span>g</span>
    </pre></div>
    </div>


User documentation
------------------

New users should probably start here.

.. toctree::
   :maxdepth: 2

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
