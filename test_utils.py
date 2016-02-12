'''
By Jason Krone for Khan Academy

Contains tests for functions in utils
'''

from utils import *

class TestUtils(object):

    def test_subset_sum_within_range(self):
        print "\n TESTING SUBSET SUM WITHIN RANGE \n"

        assert(subset_sum_within_range([2, 5, 6], 5, 0) == [5])
        print "PASSED TEST # 1 OF SUBSET SUM WITHIN RANGE" 

        assert(subset_sum_within_range([1, 3, 4], 8, 2) == [4, 3])
        print "PASSED TEST # 2 OF SUBSET SUM WITHIN RANGE" 

        assert(subset_sum_within_range([1], 1, 1) == [1])
        print "PASSED TEST # 3 OF SUBSET SUM WITHIN RANGE" 

        assert(subset_sum_within_range([200, 100, 1, 2], 303, 1) == [2, 100, 200])
        print "PASSED TEST # 4 OF SUBSET SUM WITHIN RANGE" 

        assert(subset_sum_within_range([200], 100, 100) == [200])
        print "PASSED TEST # 5 OF SUBSET SUM WITHIN RANGE" 

        assert(subset_sum_within_range([29, 3, 1], 30, 1) == [29])
        print "PASSED TEST # 6 OF SUBSET SUM WITHIN RANGE" 

        assert(subset_sum_within_range([300, 2200, 222], 1, 20) == None)
        print "PASSED TEST # 7 OF SUBSET SUM WITHIN RANGE" 

        assert(subset_sum_within_range([243], 200, 42) == None)
        print "PASSED TEST # 8 OF SUBSET SUM WITHIN RANGE" 

        assert(subset_sum_within_range([1, 2, 3, 4], 50, 0) == None)
        print "PASSED TEST # 9 OF SUBSET SUM WITHIN RANGE" 

        assert(subset_sum_within_range([2, 1, 2, 3], 9, 0) == None)
        print "PASSED TEST # 10 OF SUBSET SUM WITHIN RANGE" 

