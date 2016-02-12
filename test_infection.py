'''
By Jason Krone for Khan Academy

Contains tests for functions in infection
'''

from user import User
from infection import * 
from graph_generator import UserGraphGenerator as gg
from utils import *

import networkx as nx
from nose.tools import with_setup
import random as rand


class TestInfection(object):

    # number of tests that we run
    TEST_SIZE = 10

    # changes the size of the graphs we test on
    MAX_NUM_SUBGRAPHS = 20
    MAX_SUBGRAPH_SIZE = 100


    def test_limited_infection(self):
        print 'TESTING LIMITED INFECTION \n'
        graph_generator = gg(self.MAX_NUM_SUBGRAPHS, self.MAX_SUBGRAPH_SIZE)

        for i in range(self.TEST_SIZE):
            # get a random graph of somewhat connected cliques to test on
            SG = graph_generator.random_student_graph()
            version = 'v.Test' 
            num_to_infect = rand.randint(1, 100)
            delta = int(num_to_infect / 5)
            actual_infected = limited_infection(SG, num_to_infect, delta, version)

            if actual_infected is None:
                # check that there were no components with in the size range
                component_len = [len(c) for c in nx.connected_components(SG)]
                assert subset_sum_within_range(component_len, num_to_infect, delta) is None
                print 'PASSED TEST #', i + 1, 'OF TEST LIMITED INFECTION'
            else:
                # check that athe appropriate number of ppl were infected
                assert num_to_infect - delta <= len(actual_infected) <= num_to_infect + delta
                # check that version was spread properly
                assert(self._component_totally_infected(SG, actual_infected, version))
                assert(self._infection_contained(SG, actual_infected, version))
                print 'PASSED TEST #', i + 1, 'OF TEST LIMITED INFECTION'


    def test_total_infection(self):
        print '\n TESTING TOTAL INFECTION \n'
        # generate a random graph to test on
        graph_generator = gg(self.MAX_NUM_SUBGRAPHS, self.MAX_SUBGRAPH_SIZE)

        for i in range(self.TEST_SIZE):
            G = graph_generator.random_user_graph()

            # version to infect
            version = 'v.Test' 

            # randomly pick a user to infect
            rand_uuid = rand.randint(1, len(G)-1 )

            # get component that user is in which should be infected
            expect_infected = self._get_cc_containing_uuid(G, rand_uuid) 
            actual_infected = total_infection(G, rand_uuid, version) 

            # check that version was spread properly
            assert(actual_infected == expect_infected)
            assert(self._component_totally_infected(G, actual_infected, version))
            assert(self._infection_contained(G, actual_infected, version))
            print 'PASSED TEST #', i + 1, 'OF TEST TOTAL INFECTION'


    def _component_totally_infected(self, G, component, version):
        ''' determines if every user in the given component was infected with version ''' 
        assert G

        was_infected = True

        for uuid in component:
            was_infected = was_infected and G.node[uuid].site_version == version

        return was_infected


    def _infection_contained(self, G, infected_component, version):
        ''' determines if the infection was contained to the given component '''
        assert G 

        was_contained = True

        # get ids of users that shouldn't have been infected
        non_infected_uuids = [uuid for uuid in G.node if uuid not in infected_component]

        for uuid in non_infected_uuids:
            was_contained = was_contained and G.node[uuid].site_version != version

        return was_contained


    def _get_cc_containing_uuid(self, G, uuid):
        ''' returns the connected component that contians the given uuid and None '''
        assert G 

        uuid_component = None
        component_generator = nx.connected_components(G)

        for s in component_generator:
            if uuid in s:
                uuid_component = s
                break

        return uuid_component


