'''
By Jason Krone for Khan Academy

Contains tests for functions in infection
'''

from user import User
from infection import Infection 

import networkx as nx
from nose.tools import with_setup
import random as rand


class TestInfection:

    MAX_NUM_SUBGRAPHS = 20
    MAX_SUBGRAPH_SIZE = 100

    # array of graph generating functions
    GRAPH_GENERATORS = [
        nx.complete_graph,
        nx.circular_ladder_graph,
        nx.cycle_graph, 
        nx.empty_graph,
        nx.ladder_graph,
    ]


    @classmethod
    def setup_class(cls):
        print('called setup')


    @classmethod
    def teardown_class(cls):
        print('called teardown')


    def test_total_infection(self):

        # get a graph to test on
        G = self._rand_user_graph()
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


    def _component_totally_infected(self, G, component, version):
        ''' determines if every user in the given component was infected with version ''' 

        was_infected = True

        for uuid in component:
            was_infected = was_infected and G.node[uuid].site_version == version

        return was_infected


    def _infection_contained(self, G, infected_component, version):
        ''' determines if the infection was contained to the given component '''

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
      

    # TODO: connect user objects correctly
    # set every user to coach every other user since its a complete graph
    # map(lambda u: u.add_coaches([x for x in users if x is not u]), users)DO: fix so that users are correctly represented as mentors etc
    def _rand_user_graph(self):
        ''' returns a random graph of users'''

        G = self._random_graph(rand.randint(1, self.MAX_NUM_SUBGRAPHS))

        users = [User(uuid, 'v.' + str(uuid)) for uuid in G.node]

        # insert user objects into graph under their uuid
        for uuid in G.node:
            G.node[uuid] = users[uuid]

        return G 


    def _random_graph(self, num_subgraphs):
        ''' returns a graph made up of the given number of random subgraphs '''

        graph_size = rand.randint(1, self.MAX_SUBGRAPH_SIZE)
        G = self._random_subgraph(graph_size)
        
        # we just created a component
        num_subgraphs = num_subgraphs - 1

        # union subgraphs  
        for i in range(num_subgraphs):
            graph_size = rand.randint(1, self.MAX_SUBGRAPH_SIZE)
            H = self._random_subgraph(graph_size)
            G = nx.disjoint_union(G, H)

        return G


    def _random_subgraph(self, graph_size):
        ''' return a random type of graph of the given size '''

        idx = rand.randint(0, len(self.GRAPH_GENERATORS)-1)
        graph_gen = self.GRAPH_GENERATORS[idx]
        G = graph_gen(graph_size)
        return G


