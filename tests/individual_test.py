#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' Test case for GAIndividual
'''

import unittest

from gapy.components.individual import GAIndividual

class IndividualTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = True

    def test_binary_encoding(self):
        ''' Make sure individual can decode and encode binary gene correctly.
        '''
        indv = GAIndividual(ranges=[(0, 1)], encoding='binary', eps=0.001)
        indv.init(variants=[0.398])

        # Test binary chromsome.
        ref_chromsome = [0, 1, 1, 0, 0, 0, 1, 1, 1, 0]
        self.assertListEqual(indv.chromsome, ref_chromsome)

        # Test decode.
        self.assertListEqual(indv.decode(), [0.398])

        indv = GAIndividual(ranges=[(0, 1), (-1, 1)], encoding='binary', eps=0.001)
        indv.init(variants=[0.398, 0.66])

        # Test binary chromsome.
        ref_chromsome = [0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0]
        self.assertListEqual(indv.chromsome, ref_chromsome)

        # Test decode.
        self.assertListEqual(indv.decode(), [0.398, 0.6600000000000001])

    def test_decimal_construction(self):
        ''' Make sure individual can decode and encode decimal gene correctly.
        '''
        indv = GAIndividual(ranges=[(0, 1)], encoding='decimal', eps=0.001)

        indv.init(variants=[0.398])
        self.assertListEqual(indv.encode(), [0.398])
        self.assertListEqual(indv.decode(), [0.398])

    def test_init(self):
        ''' Make sure the individual can be initialized correctly.
        '''
        indv = GAIndividual(ranges=[(0, 1)], encoding='binary', eps=0.001)

        ref_chromsome = [0, 1, 1, 0, 0, 0, 1, 1, 1, 0]
        ref_variants = [0.398]

        # Check chromsome initialization.
        indv.init(chromsome=ref_chromsome)
        
        self.assertListEqual(ref_chromsome, indv.chromsome)
        self.assertListEqual(ref_variants, indv.variants)

        # Check variants initialization.
        indv.init(variants=ref_variants)
        
        self.assertListEqual(indv.variants, ref_variants)
        self.assertListEqual(indv.chromsome, ref_chromsome)

    def test_clone(self):
        ''' Make sure individual can be cloned correctly.
        '''
        indv = GAIndividual(ranges=[(0, 1)],
                            encoding='binary',
                            eps=0.001).init(variants=[0.398])
        indv_clone = indv.clone()

        self.assertListEqual(indv.chromsome, indv_clone.chromsome)
        self.assertAlmostEqual(indv.variants[0], indv_clone.variants[0], places=2)
        self.assertEqual(indv.ranges, indv_clone.ranges)
        self.assertEqual(indv.eps, indv_clone.eps)
        self.assertEqual(indv.encoding, indv_clone.encoding)

if '__main__' == __name__:
    suite = unittest.TestLoader().loadTestsFromTestCase(IndividualTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
