'''
By Jason Krone for Khan Academy

Contains unit tests for functions in infection
'''

from user import User
from infection import Infection 

import networkx as nx
from nose.tools import with_setup
import random as rand


class TestInfection:

    # proably want like a lamda function about the number of ppl that are 
    # going to get infected if you target a person in the graph

    # array of graph functions
    graph_generators = [
        nx.complete_graph,
        nx.circular_ladder_graph,
        nx.cycle_graph, 
        nx.empty_graph,
        nx.ladder_graph,
    ]

    MAX_GRAPH_SIZE = 1000


    @classmethod
    def setup_class(cls):
        print('called setup')


    @classmethod
    def teardown_class(cls):
        print('called teardown')


    def test_total_infection(self):
        # get a graph to test on
        size = rand.randint(1, 100)
        G = self._rand_user_graph(size)

        infection = Infection(G)

        # version to infect
        version = 'vT' 


        # randomly pick a user to infect

        # check which component that user is in connected_components
        # make sure that component becomes infected with the verions
        # and that no other components are infected


        infection.total_infection(1, version) 

        # check that version was spread properly
        assert(any(u.site_version != version for u in G.node.values()) == False)
        

    # TODO: probably not going to take graph_size
    def _rand_user_graph(self, graph_size):
        ''' returns a graph to use for testing purposes'''

        G = nx.complete_graph(graph_size)


        users = [User(uuid, 'v.' + str(uuid)) for uuid in G.node]


        # TODO: this depends on the graph
        # set every user to coach every other user since its a complete graph
        map(lambda u: u.add_coaches([x for x in users if x is not u]), users)

        # insert user objects into graph under their uuid
        for uuid in G.node:
            G.node[uuid] = users[uuid]

        return G 


    def _random_graph_with_subs(self, num_subgraphs):
        ''' returns a graph made up of the given number of random subgraphs '''

        G = self._random_graph()
        
        # we just created a component
        num_subgraphs = num_subgraphs - 1

        # create subgraphs  
        for i in range(num_subgraphs)
            graph_size = rand.randint(1, some_max)
            H = graph_funs[RAND]()
            G = nx.disjoint_union(G, H)

        return G


    def _random_graph(self):
        ''' return a random type of graph of random size '''
        idx = rand.randint(0, len(graph_generators)-1)
        graph_gen = graph_generators[idx]
        size = rand.randint(1, MAX_GRAPH_SIZE)
        G = graph_gen(size)
        return G















