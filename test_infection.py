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
    graph_funs = [
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
        size = rand.randint(1, 100)
        G = self.get_graph(size)

        # run the algorithm 
        infection = Infection(G)
        print(type(infection.G))
        version = 'vT'
        infection.total_infection(1, version) 

        # check that version was spread properly
        assert(any(u.site_version != version for u in G.node.values()) == False)
        


    def get_graph(self, graph_size):
        ''' returns a random graph to use for testing purposes'''

        G = nx.complete_graph(graph_size)

        users = [User(uuid, 'v.' + str(uuid)) for uuid in G.node]

        # set every user to coach every other user since its a complete graph
        map(lambda u: u.add_coaches([x for x in users if x is not u]), users)

        # insert user objects into graph under their uuid
        for uuid in G.node:
            G.node[uuid] = users[uuid]

        return G 













