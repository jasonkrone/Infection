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


    # TODO: connect user objects correctly
    # set every user to coach every other user since its a complete graph
    # map(lambda u: u.add_coaches([x for x in users if x is not u]), users)DO: fix so that users are correctly represented as mentors etc
    def random_user_graph(self):
        ''' returns a random graph of users'''

        G = self._random_graph(rand.randint(1, self.max_subgraphs))

        users = [User(uuid, 'v.' + str(uuid)) for uuid in G.node]

        # insert user objects into graph under their uuid
        for uuid in G.node:
            G.node[uuid] = users[uuid]

        return G 


    def _random_graph(self, num_subgraphs):
        ''' returns a graph made up of the given number of random subgraphs '''

        graph_size = rand.randint(1, self.max_subgraph_size)
        G = self._random_subgraph(graph_size)
        
        # we just created a component
        num_subgraphs = num_subgraphs - 1

        # union subgraphs  
        for i in range(num_subgraphs):
            graph_size = rand.randint(1, self.max_subgraph_size)
            H = self._random_subgraph(graph_size)
            G = nx.disjoint_union(G, H)

        return G


    def _random_subgraph(self, graph_size):
        ''' return a random type of graph of the given size '''

        idx = rand.randint(0, len(self.GRAPH_GENERATORS)-1)
        graph_gen = self.GRAPH_GENERATORS[idx]
        G = graph_gen(graph_size)
        return G

