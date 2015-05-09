"""
Convenience wrapper around ``monoseq`` for use in the IPython Notebook.

.. moduleauthor:: Martijn Vermaat <martijn@vermaat.name>

.. Licensed under the MIT license, see the LICENSE.rst file.
"""


from IPython.display import HTML

from .monoseq import HtmlFormat, pprint_sequence


STYLE = """
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


def Seq(sequence, annotations=None, block_length=10, blocks_per_line=6):
    """
    Pretty-printed sequence object that's displayed nicely in the IPython
    Notebook.

    For a description of the arguments, see :func:`pprint_sequence`.

    This supports up to four levels of annotation, displayed as red, inverted,
    underlined, and bold.
    """
    style = STYLE.format(selector='#monoseq')
    pprinted = pprint_sequence(sequence,
                               annotations=annotations,
                               block_length=block_length,
                               blocks_per_line=blocks_per_line,
                               format=HtmlFormat)

    return HTML('<style>{style}</style><pre id="monoseq">{pprinted}</pre>'
                .format(style=style, pprinted=pprinted))
