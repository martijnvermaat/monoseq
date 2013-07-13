"""
Tests for the commands module.
"""


from nose.tools import *


from monoseq.commands import _bed_iter, _fasta_iter


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
        result = list(_fasta_iter(fasta))
        expected = [('sequence 1',
                     'TTACAGGCTACATTGCATGATCATTGCATGATTTACAGGCTACATTGCATGAT'
                     'TGCATGATTTACAGGCTACATTGCATGATCATTGCATGATTTACAGGCTACAT'
                     'GGCTACATTGCATGATCATTG'),
                    ('sequence 2',
                     'GGCTACATTTACAGGCTACATTGCATGATCATTGCATGAGGCTACATTTACAG'
                     'AGGCTACATTGCATGATCATTGCA')]
        assert_equal(result, expected)

    def test_chrom_iter(self):
        """
        Iterate over a multi-chromosome BED file.
        """
        bed = ('browser position chr7:127471196-127495720\n',
               'browser hide all\n',
               'track name="ItemRGBDemo" description="Item RGB demonstration" visibility=2 itemRgb="On"\n',
               'chr7	127471196	127472363	Pos1	0	+	127471196	127472363	255,0,0\n',
               'chr7	127472363	127473530	Pos2	0	+	127472363	127473530	255,0,0\n',
               'chr7	127473530	127474697	Pos3	0	+	127473530	127474697	255,0,0\n',
               'chr7	127474697	127475864	Pos4	0	+	127474697	127475864	255,0,0\n',
               'chr8	127475864	127477031	Neg1	0	-	127475864	127477031	0,0,255\n',
               'chr8	127477031	127478198	Neg2	0	-	127477031	127478198	0,0,255\n',
               'chr2	127478198	127479365	Neg3	0	-	127478198	127479365	0,0,255\n',
               'chr2	127479365	127480532	Pos5	0	+	127479365	127480532	255,0,0\n',
               'chr2	127480532	127481699	Neg4	0	-	127480532	127481699	0,0,255\n')
        result = [(chrom, list(chrom_iter))
                  for chrom, chrom_iter in _bed_iter(bed)]
        expected = [('chr7', [(127471196, 127472363),
                              (127472363, 127473530),
                              (127473530, 127474697),
                              (127474697, 127475864)]),
                    ('chr8', [(127475864, 127477031),
                              (127477031, 127478198)]),
                    ('chr2', [(127478198, 127479365),
                              (127479365, 127480532),
                              (127480532, 127481699)])]
        assert_equal(result, expected)
