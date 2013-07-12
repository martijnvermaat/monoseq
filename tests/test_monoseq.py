"""
Tests for the monoseq module.
"""


from nose.tools import *


from monoseq.monoseq import partition_range, pprint_sequence


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
        assert_equal(pprint_sequence(sequence, mode='plaintext'),
                     '  1  MIMANQPLWL DSEVEMNHYQ QSHIKSKSPY FPEDKHICWI KIFKAFGTMI MANQPLWLDS\n'
                     ' 61  EVEMNHYQQS HIKSKSPYFP EDKHICWIKI FKAFGTMIMA NQPLWLDSEV EMNHYQQSHI\n'
                     '121  KSKSPYFPED KHICWIKIFK AFGTMIMANQ PLWLDSEVEM NHYQQSHIKS KSPYFPEDKH\n'
                     '181  ICWIKIFKAF GT')
