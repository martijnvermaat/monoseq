User guide
==========

So let's say we have this DNA sequence we want to pretty-print::

    >>> sequence = ('cgcactcaaaacaaaggaagaccgtcctcgactgcagaggaagcaggaagctgtc'
    ...             'ggcccagctctgagcccagctgctggagccccgagcagcggcatggagtccgtgg'
    ...             'ccctgtacagctttcaggctacagagagcgacgagctggccttcaacaagggaga'
    ...             'cacactcaagatcctgaacatggaggatgaccagaactggtacaaggccgagctc'
    ...             'cggggtgtcgagggatttattcccaagaactacatccgcgtcaag')

We can do it with :func:`.pprint_sequence`::

    >>> from monoseq import pprint_sequence
    >>> print pprint_sequence(sequence)
      1  cgcactcaaa acaaaggaag accgtcctcg actgcagagg aagcaggaag ctgtcggccc
     61  agctctgagc ccagctgctg gagccccgag cagcggcatg gagtccgtgg ccctgtacag
    121  ctttcaggct acagagagcg acgagctggc cttcaacaag ggagacacac tcaagatcct
    181  gaacatggag gatgaccaga actggtacaa ggccgagctc cggggtgtcg agggatttat
    241  tcccaagaac tacatccgcg tcaag

(This also works if `sequence` is a Biopython :class:`Bio.Seq.Seq` object.)


Controlling block and line lengths
----------------------------------

By default, sequences are printed in blocks of 10 letters, 6 blocks per
line. This can be customized with the `block_length` and `blocks_per_line`
arguments::

    >>> print pprint_sequence(sequence, block_length=8, blocks_per_line=7)
      1  cgcactca aaacaaag gaagaccg tcctcgac tgcagagg aagcagga agctgtcg
     57  gcccagct ctgagccc agctgctg gagccccg agcagcgg catggagt ccgtggcc
    113  ctgtacag ctttcagg ctacagag agcgacga gctggcct tcaacaag ggagacac
    169  actcaaga tcctgaac atggagga tgaccaga actggtac aaggccga gctccggg
    225  gtgtcgag ggatttat tcccaaga actacatc cgcgtcaa g

::

    >>> print pprint_sequence(sequence, block_length=20, blocks_per_line=2)
      1  cgcactcaaaacaaaggaag accgtcctcgactgcagagg
     41  aagcaggaagctgtcggccc agctctgagcccagctgctg
     81  gagccccgagcagcggcatg gagtccgtggccctgtacag
    121  ctttcaggctacagagagcg acgagctggccttcaacaag
    161  ggagacacactcaagatcct gaacatggaggatgaccaga
    201  actggtacaaggccgagctc cggggtgtcgagggatttat
    241  tcccaagaactacatccgcg tcaag


Output formats
--------------

As we'll see in the next section, certain parts of the sequence can be
annotated for highlighting. For this to work, we need to specify another
output format than the default :data:`.PlaintextFormat`.

``monoseq`` includes three built-in output formats:

- :data:`.PlaintextFormat` for, well, generating plaintext.
- :data:`.AnsiFormat` adds ANSI escape codes for use in a terminal.
- :data:`.HtmlFormat` adds HTML tags for inclusion in an HTML document.

(And if this doesn't satisfy our needs, we can define custom output formats by
implementing :class:`.Format`.)

Formats are specified with the `format` argument of the
:func:`.pprint_sequence` function. For example, this is the same example
pretty-printed with :data:`.HtmlFormat`::

    >>> from monoseq import HtmlFormat
    >>> print pprint_sequence(sequence, blocks_per_line=3, format=HtmlFormat)
      <span class="monoseq-margin">1</span>  cgcactcaaa acaaaggaag accgtcctcg
     <span class="monoseq-margin">31</span>  actgcagagg aagcaggaag ctgtcggccc
     <span class="monoseq-margin">61</span>  agctctgagc ccagctgctg gagccccgag
     <span class="monoseq-margin">91</span>  cagcggcatg gagtccgtgg ccctgtacag
    <span class="monoseq-margin">121</span>  ctttcaggct acagagagcg acgagctggc
    <span class="monoseq-margin">151</span>  cttcaacaag ggagacacac tcaagatcct
    <span class="monoseq-margin">181</span>  gaacatggag gatgaccaga actggtacaa
    <span class="monoseq-margin">211</span>  ggccgagctc cggggtgtcg agggatttat
    <span class="monoseq-margin">241</span>  tcccaagaac tacatccgcg tcaag

As you can see, :data:`.HtmlFormat` wraps the sequence positions in ``<span>``
tags with a ``class`` attribute value of ``monoseq-margin``. This allows us to
add custom styling to these numbers with a CSS stylesheet.

.. note:: In an HTML document, include the pretty-printed sequence within
    ``<pre>`` and ``</pre>``. This preserves all whitespace and automatically
    selects a monospace font.


Sequence annotations
--------------------

Subsequences can be highlighted in the pretty-printed sequence by specifying
their positions. Such a specification is called an annotation. Several
annotations can be provided and each of them will be highlighted in a distinct
style (e.g., the first annotation is colored red and the second is printed in
bold).

Let's assume our analysis shows positions 12 through 37 and 223 through 247 to
be highly conserved between species. Of course, we want to annotate our
sequence with this knowledge:

.. raw:: html

    <div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">monoseq</span> <span class="kn">import</span> <span class="n">AnsiFormat</span>
    <span class="gp">&gt;&gt;&gt; </span><span class="n">conserved</span> <span class="o">=</span> <span class="p">[[(</span><span class="mi">11</span><span class="p">,</span> <span class="mi">37</span><span class="p">),</span> <span class="p">(</span><span class="mi">222</span><span class="p">,</span> <span class="mi">247</span><span class="p">)]</span>
    <span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">pprint_sequence</span><span class="p">(</span><span class="n">sequence</span><span class="p">,</span> <span class="n">format</span><span class="o">=</span><span class="n">AnsiFormat</span><span class="p">,</span>
    <span class="gp">... </span>                      <span class="n">annotations</span><span class="o">=</span><span class="p">[</span><span class="n">conserved</span><span class="p">])</span>
    <span class="go">  1  cgcactcaaa a<span style="color:red">caaaggaag accgtcctcg actgcag</span>agg aagcaggaag ctgtcggccc</span>
    <span class="go"> 61  agctctgagc ccagctgctg gagccccgag cagcggcatg gagtccgtgg ccctgtacag</span>
    <span class="go">121  ctttcaggct acagagagcg acgagctggc cttcaacaag ggagacacac tcaagatcct</span>
    <span class="go">181  gaacatggag gatgaccaga actggtacaa ggccgagctc cg<span style="color:red">gggtgtcg agggatttat</span></span>
    <span class="go">241  <span style="color:red">tcccaag</span>aac tacatccgcg tcaag</span>
    </pre></div>
    </div>

.. note:: Regions are defined as in slicing notation, so zero-based and
    open-ended.

Just for lack of imagination, we also want to make it clear where every 12th
nucleotide is in our sequence. We can do this by defining a second
annotation, which is printed in bold by :data:`.AnsiFormat`:

.. raw:: html

    <div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">twelves</span> <span class="o">=</span> <span class="p">[(</span><span class="n">p</span><span class="p">,</span> <span class="n">p</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span> <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">11</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">sequence</span><span class="p">),</span> <span class="mi">12</span><span class="p">)]</span>
    <span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">pprint_sequence</span><span class="p">(</span><span class="n">sequence</span><span class="p">,</span> <span class="n">format</span><span class="o">=</span><span class="n">AnsiFormat</span><span class="p">,</span>
    <span class="gp">... </span>                      <span class="n">annotations</span><span class="o">=</span><span class="p">[</span><span class="n">conserved</span><span class="p">,</span> <span class="n">twelves</span><span class="p">])</span>
    <span class="go">  1  cgcactcaaa a<span style="color:red"><span style="font-weight:bold">c</span>aaaggaag acc<span style="font-weight:bold">g</span>tcctcg actgc<span style="font-weight:bold">a</span>g</span>agg aagcagg<span style="font-weight:bold">a</span>ag ctgtcggcc<span style="font-weight:bold">c</span></span>
    <span class="go"> 61  agctctgagc c<span style="font-weight:bold">c</span>agctgctg gag<span style="font-weight:bold">c</span>cccgag cagcg<span style="font-weight:bold">g</span>catg gagtccg<span style="font-weight:bold">t</span>gg ccctgtaca<span style="font-weight:bold">g</span></span>
    <span class="go">121  ctttcaggct a<span style="font-weight:bold">c</span>agagagcg acg<span style="font-weight:bold">a</span>gctggc cttca<span style="font-weight:bold">a</span>caag ggagaca<span style="font-weight:bold">c</span>ac tcaagatcc<span style="font-weight:bold">t</span></span>
    <span class="go">181  gaacatggag g<span style="font-weight:bold">a</span>tgaccaga act<span style="font-weight:bold">g</span>gtacaa ggccg<span style="font-weight:bold">a</span>gctc cg<span style="color:red">gggtg<span style="font-weight:bold">t</span>cg agggattta<span style="font-weight:bold">t</span></span></span>
    <span class="go">241  <span style="color:red">tcccaag</span>aac t<span style="font-weight:bold">a</span>catccgcg tca<span style="font-weight:bold">a</span>g</span>
    </pre></div>
    </div>

:data:`.AnsiFormat` supports up to three annotation levels and the third one
is printed underlined. So if the middle third of the sequence would be our
primary concern, we could underline it as follows:

.. raw:: html

    <div class="highlight-python"><div class="highlight"><pre><span class="gp">&gt;&gt;&gt; </span><span class="n">middle</span> <span class="o">=</span> <span class="p">[(</span><span class="nb">len</span><span class="p">(</span><span class="n">sequence</span><span class="p">)</span> <span class="o">/</span> <span class="mi">3</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">sequence</span><span class="p">)</span> <span class="o">/</span> <span class="mi">3</span> <span class="o">*</span> <span class="mi">2</span><span class="p">)]</span>
    <span class="gp">&gt;&gt;&gt; </span><span class="k">print</span> <span class="n">pprint_sequence</span><span class="p">(</span><span class="n">sequence</span><span class="p">,</span> <span class="n">format</span><span class="o">=</span><span class="n">AnsiFormat</span><span class="p">,</span>
    <span class="gp">... </span>                      <span class="n">annotations</span><span class="o">=</span><span class="p">[</span><span class="n">conserved</span><span class="p">,</span> <span class="n">twelves</span><span class="p">,</span> <span class="n">middle</span><span class="p">])</span>
    <span class="go">  1  cgcactcaaa a<span style="color:red"><span style="font-weight:bold">c</span>aaaggaag acc<span style="font-weight:bold">g</span>tcctcg actgc<span style="font-weight:bold">a</span>g</span>agg aagcagg<span style="font-weight:bold">a</span>ag ctgtcggcc<span style="font-weight:bold">c</span></span>
    <span class="go"> 61  agctctgagc c<span style="font-weight:bold">c</span>agctgctg gag<span style="font-weight:bold">c</span>cccg<span style="text-decoration:underline">ag cagcg<span style="font-weight:bold">g</span>catg gagtccg<span style="font-weight:bold">t</span>gg ccctgtaca<span style="font-weight:bold">g</span></span></span>
    <span class="go">121  <span style="text-decoration:underline">ctttcaggct a<span style="font-weight:bold">c</span>agagagcg acg<span style="font-weight:bold">a</span>gctggc cttca<span style="font-weight:bold">a</span>caag ggagaca<span style="font-weight:bold">c</span>ac tcaaga</span>tcc<span style="font-weight:bold">t</span></span>
    <span class="go">181  gaacatggag g<span style="font-weight:bold">a</span>tgaccaga act<span style="font-weight:bold">g</span>gtacaa ggccg<span style="font-weight:bold">a</span>gctc cg<span style="color:red">gggtg<span style="font-weight:bold">t</span>cg agggattta<span style="font-weight:bold">t</span></span></span>
    <span class="go">241  <span style="color:red">tcccaag</span>aac t<span style="font-weight:bold">a</span>catccgcg tca<span style="font-weight:bold">a</span>g</span>
    </pre></div>
    </div>


Styling :data:`.HtmlFormat` output
----------------------------------

The :data:`.HtmlFormat` output format supports up to 10 annotation levels, but
how to style them is up to the user. All ``monoseq`` does is add ``<span>``
tags around annotations with ``class`` attribute values of
``monoseq-annotation-{i}``, where ``{i}`` is the annotation level starting
from 0.

Here are some example CSS rules for styling 4 annotation levels:

.. code-block:: css

    pre {
        background: lightYellow;
        color: black;
    }
    .monoseq-margin {
        color: grey;
    }
    .monoseq-annotation-0 {
        color: red;
    }
    .monoseq-annotation-1 {
        background: black;
        color: lightYellow;
    }
    .monoseq-annotation-1 .monoseq-annotation-0 {
        background: red;
        color: lightYellow;
    }
    .monoseq-annotation-2 {
        text-decoration: underline;
    }
    .monoseq-annotation-3 {
        font-weight: bold;
    }

Using these rules, a pretty-printed protein sequence will look something like this:

.. raw:: html

    <style>
    pre.monoseq {
        background: lightYellow;
        color: black;
    }
    .monoseq-margin {
        color: grey;
    }
    .monoseq-annotation-0 {
        color: red;
    }
    .monoseq-annotation-1 {
        background: black;
        color: lightYellow;
    }
    .monoseq-annotation-1 .monoseq-annotation-0 {
        background: red;
        color: lightYellow;
    }
    .monoseq-annotation-2 {
        text-decoration: underline;
    }
    .monoseq-annotation-3 {
        font-weight: bold;
    }
    </style>
    <pre class="monoseq">
      <span class="monoseq-margin">1</span>  MIMANQPLWL DS<span
      class="monoseq-annotation-0">EV</span><span
      class="monoseq-annotation-1"><span
      class="monoseq-annotation-0">E</span></span><span
      class="monoseq-annotation-0">MNHYQ</span> <span
      class="monoseq-annotation-0">QSH</span>IKSKSPY FPEDKHIC<span
      class="monoseq-annotation-1">W</span>I KIFKAFGMIM ANQPLWLDSE
     <span class="monoseq-margin">61</span>  VEMNHYQQSH IKSKSPYFPE DK<span
      class="monoseq-annotation-1">H</span>ICWIKIF KAFGMIMAN<span
      class="monoseq-annotation-2">Q</span> <span
      class="monoseq-annotation-2">PLWLDSEVEM</span> <span
      class="monoseq-annotation-2">NHYQQSHIKS</span>
    <span class="monoseq-margin">121</span>  <span
      class="monoseq-annotation-2">KSPYFPEDKH</span> <span
      class="monoseq-annotation-2">ICWIK</span><span
      class="monoseq-annotation-3"><span
      class="monoseq-annotation-2">IF</span></span><span
      class="monoseq-annotation-3">KA</span>F GMIMANQPLW LDSEVEMNHY QQSHIKSKSP YFPEDKHICW
    <span class="monoseq-margin">181</span>  IKIFKAFG
    </pre>
