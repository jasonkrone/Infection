'''
By Jason Krone for Khan Academy

Contains tests for functions in infection
'''

from user import User
from infection import Infection 
from graph_generator import UserGraphGenerator as gg

import networkx as nx
from nose.tools import with_setup
import random as rand


class TestInfection(object):

    TEST_SIZE = 10
    MAX_NUM_SUBGRAPHS = 20
    MAX_SUBGRAPH_SIZE = 100

    @classmethod
    def setup_class(cls):
        print('called setup')


    @classmethod
    def teardown_class(cls):
        print('called teardown')


    def test_limited_infection(self):
        # get a random graph of somewhat connected cliques to test on

        # set ones that sum, set others that don't 

        # check that we infect the one's at sum

        # check that it spread within these

        # and it didn't spread within the others



    def test_total_infection(self):

        # generate a random graph to test on
        graph_generator = gg(self.MAX_NUM_SUBGRAPHS, self.MAX_SUBGRAPH_SIZE)

        for i in range(self.TEST_SIZE):
            G = graph_generator.random_user_graph()
            infection = Infection(G)

            # version to infect
            version = 'v.Test' 

            # randomly pick a user to infect
            rand_uuid = rand.randint(1, len(G)-1 )

            # get component that user is in which should be infected
            expect_infected = self._get_cc_containing_uuid(G, rand_uuid) 
            actual_infected = infection.total_infection(rand_uuid, version) 

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
      
