''' 
By Jason Krone for Khan Academy

Implementation of UserGraphGenerator class
'''

import networkx as nx
from user import User
import random as rand


class UserGraphGenerator(object):

    # nx graph generating functions
    GRAPH_GENERATORS = [
        nx.complete_graph,
        nx.circular_ladder_graph,
        nx.cycle_graph,
        nx.empty_graph,
        nx.ladder_graph,
    ]


    def __init__(self, num_max_subgraphs, max_subgraph_size):
        self.max_subgraphs = num_max_subgraphs
        self.max_subgraph_size = max_subgraph_size


    def random_student_graph(self):
        ''' 
        returns a random graph of students with max size
        num_max_subgraphs * max_subgraph_size 
        '''
        # created random graph only using complete subgraphs
        SG = self._random_graph(rand.randint(1, self.max_subgraphs), self.GRAPH_GENERATORS[:1])

        users = [User(uuid, 'v.' + str(uuid)) for uuid in SG.node]

        # insert user objects into graph under their uuid
        for uuid in SG.node:
            SG.node[uuid] = users[uuid]

        return SG 


    def random_user_graph(self):
        ''' 
        returns a random graph of users  with max size
        num_max_subgraphs * max_subgraph_size 
        '''

        G = self._random_graph(rand.randint(1, self.max_subgraphs), self.GRAPH_GENERATORS)

        users = [User(uuid, 'v.' + str(uuid)) for uuid in G.node]

        # insert user objects into graph under their uuid
        for uuid in G.node:
            G.node[uuid] = users[uuid]

        return G 


    def _random_graph(self, num_subgraphs, generators):
        ''' 
        returns a graph made up of the given number of random subgraphs created
        using the given graph generation functions
        '''

        graph_size = rand.randint(1, self.max_subgraph_size)
        G = self._random_subgraph(graph_size, generators)
        
        # we just created a component
        num_subgraphs = num_subgraphs - 1

        # union subgraphs  
        for i in range(num_subgraphs):
            graph_size = rand.randint(1, self.max_subgraph_size)
            H = self._random_subgraph(graph_size, generators)
            G = nx.disjoint_union(G, H)

        return G


    def _random_subgraph(self, graph_size, generators):
        '''
        return a random graph of the given size using a method from 
        the given list of graph generators
        '''

        idx = rand.randint(0, len(generators)-1)
        graph_gen = generators[idx]
        G = graph_gen(graph_size)
        return G

