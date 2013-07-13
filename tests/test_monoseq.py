"""
Tests for the monoseq module.
"""


from nose.tools import *


from monoseq.monoseq import (HtmlFormat, AnsiFormat, PlaintextFormat,
                             partition_range, pprint_sequence)


class TestMonoseq(object):
    """
    Tests for the monoseq module.
    """
    def test_partition_range(self):
        """
        Simple partition of range with two annotation levels.
        """
        assert_equal(partition_range(50, annotations=[[(0, 21), (30, 35)],
                                                      [(15, 32), (40, 46)]]),
                     [(0, 15, {0}),
                      (15, 21, {0, 1}),
                      (21, 30, {1}),
                      (30, 32, {0, 1}),
                      (32, 35, {0}),
                      (35, 40, set()),
                      (40, 46, {1}),
                      (46, 50, set())])

    def test_pprint_sequence(self):
        """
        Pretty-print a simple sequence in plaintext.
        """
        sequence = 'MIMANQPLWLDSEVEMNHYQQSHIKSKSPYFPEDKHICWIKIFKAFGT' * 4
        assert_equal(pprint_sequence(sequence, format=PlaintextFormat),
                     '  1  MIMANQPLWL DSEVEMNHYQ QSHIKSKSPY FPEDKHICWI KIFKAFGTMI MANQPLWLDS\n'
                     ' 61  EVEMNHYQQS HIKSKSPYFP EDKHICWIKI FKAFGTMIMA NQPLWLDSEV EMNHYQQSHI\n'
                     '121  KSKSPYFPED KHICWIKIFK AFGTMIMANQ PLWLDSEVEM NHYQQSHIKS KSPYFPEDKH\n'
                     '181  ICWIKIFKAF GT')

    def test_pprint_sequence_html(self):
        """
        Pretty-print sequence to HTML with two annotation levels.
        """
        sequence = 'MIMANQPLWLDSEVEMNHYQQSHIKSKSPYFPEDKHICWIKIFKAFGT' * 4
        annotations = [[(12, 23)], [(14, 15), (38, 39), (82, 83)]]
        assert_equal(pprint_sequence(sequence, annotations=annotations, format=HtmlFormat),
                     '  <span class="pprint-margin">1</span>  MIMANQPLWL DS'
                     '<span class="level0-annotation">EV</span>'
                     '<span class="level1-annotation"><span class="level0-annotation">E</span></span>'
                     '<span class="level0-annotation">MNHYQ</span> '
                     '<span class="level0-annotation">QSH</span>'
                     'IKSKSPY FPEDKHIC'
                     '<span class="level1-annotation">W</span>'
                     'I KIFKAFGTMI MANQPLWLDS\n'
                     ' <span class="pprint-margin">61</span>  EVEMNHYQQS HIKSKSPYFP ED'
                     '<span class="level1-annotation">K</span>'
                     'HICWIKI FKAFGTMIMA NQPLWLDSEV EMNHYQQSHI\n'
                     '<span class="pprint-margin">121</span>  KSKSPYFPED KHICWIKIFK AFGTMIMANQ PLWLDSEVEM NHYQQSHIKS KSPYFPEDKH\n'
                     '<span class="pprint-margin">181</span>  ICWIKIFKAF GT')

    def test_pprint_sequence_ansi(self):
        """
        Pretty-print sequence to plaintext with ANSI escapes with two
        annotation levels.
        """
        sequence = 'MIMANQPLWLDSEVEMNHYQQSHIKSKSPYFPEDKHICWIKIFKAFGT' * 4
        annotations = [[(12, 23)], [(14, 15), (38, 39), (82, 83)]]
        assert_equal(pprint_sequence(sequence, annotations=annotations, format=AnsiFormat),
                     '  1  MIMANQPLWL DS'
                     '\033[91mEV\033[0m'
                     '\033[1m\033[91mE\033[0m\033[0m'
                     '\033[91mMNHYQ\033[0m '
                     '\033[91mQSH\033[0m'
                     'IKSKSPY FPEDKHIC'
                     '\033[1mW\033[0m'
                     'I KIFKAFGTMI MANQPLWLDS\n'
                     ' 61  EVEMNHYQQS HIKSKSPYFP ED'
                     '\033[1mK\033[0m'
                     'HICWIKI FKAFGTMIMA NQPLWLDSEV EMNHYQQSHI\n'
                     '121  KSKSPYFPED KHICWIKIFK AFGTMIMANQ PLWLDSEVEM NHYQQSHIKS KSPYFPEDKH\n'
                     '181  ICWIKIFKAF GT')
