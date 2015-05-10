"""
Convenience wrapper around ``monoseq`` for use in the IPython Notebook.

.. moduleauthor:: Martijn Vermaat <martijn@vermaat.name>

.. Licensed under the MIT license, see the LICENSE.rst file.
"""


import binascii
import os

from IPython.display import HTML

from .monoseq import HtmlFormat, pprint_sequence


#: Default CSS for styling in the IPython Notebook, suporting up to four
#: levels of annotation. They are displayed as red, inverted, underlined, and
#: bold.
DEFAULT_STYLE = """
{selector} {{
    background: white;
    color: black;
    font-weight: normal;
    text-decoration: none;
}}
{selector} .monoseq-margin {{
    color: grey;
}}
{selector} .monoseq-annotation-0 {{
    color: red;
}}
{selector} .monoseq-annotation-1 {{
    background: black;
    color: white;
}}
{selector} .monoseq-annotation-1 .monoseq-annotation-0 {{
    background: red;
    color: white;
}}
{selector} .monoseq-annotation-2 {{
    text-decoration: underline;
}}
{selector} .monoseq-annotation-3 {{
    font-weight: bold;
}}
"""


def Seq(sequence, annotations=None, block_length=10, blocks_per_line=6,
        style=DEFAULT_STYLE):
    """
    Pretty-printed sequence object that's displayed nicely in the IPython
    Notebook.

    :arg style: Custom CSS as a `format string`, where a selector for the
        top-level ``<pre>`` element is substituted for `{selector}`. See
        :data:`DEFAULT_STYLE` for an example.
    :type style: str

    For a description of the other arguments, see
    :func:`monoseq.pprint_sequence`.
    """
    seq_id = 'monoseq-' + binascii.hexlify(os.urandom(4))
    pprinted = pprint_sequence(sequence,
                               annotations=annotations,
                               block_length=block_length,
                               blocks_per_line=blocks_per_line,
                               format=HtmlFormat)

    return HTML('<style>{style}</style><pre id="{seq_id}">{pprinted}</pre>'
                .format(style=style.format(selector='#' + seq_id),
                        seq_id=seq_id,
                        pprinted=pprinted))
