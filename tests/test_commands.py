"""
Tests for the commands module.
"""


from nose.tools import *


from monoseq.commands import _fasta_iter


class TestCommands(object):
    """
    Tests for the commands module.
    """
    def test_fasta_iter(self):
        """
        Iterate over a multi-record FASTA file.
        """
        fasta = ('>sequence 1\n',
                 'TTACAGGCTACATTGCATGATCATTGCATGATTTACAGGCTACATTGCATGAT\n',
                 'TGCATGATTTACAGGCTACATTGCATGATCATTGCATGATTTACAGGCTACAT\n',
                 'GGCTACATTGCATGATCATTG\n',
                 '>sequence 2\n',
                 'GGCTACATTTACAGGCTACATTGCATGATCATTGCATGAGGCTACATTTACAG\n',
                 'AGGCTACATTGCATGATCATTGCA\n')
        assert_equal(list(_fasta_iter(fasta)),
                     [('sequence 1',
                       'TTACAGGCTACATTGCATGATCATTGCATGATTTACAGGCTACATTGCATGAT'
                       'TGCATGATTTACAGGCTACATTGCATGATCATTGCATGATTTACAGGCTACAT'
                       'GGCTACATTGCATGATCATTG'),
                      ('sequence 2',
                       'GGCTACATTTACAGGCTACATTGCATGATCATTGCATGAGGCTACATTTACAG'
                       'AGGCTACATTGCATGATCATTGCA')])
