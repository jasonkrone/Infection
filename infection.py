'''
By Jason Krone for Khan Academy

Implementation of Infection Class

'''

import networkx as nx
from user import User


class Infection(object):

    def __init__(self, G):
        '''creates a new infection object with the given undirected graph'''
        
        self.graph = G


    def total_infection(version, start_user):
        '''infects the connected component containing start_user with the given version of the website''' 

        queue = [start_user]
        infected = set()

        while queue:
            u = queue.pop(0)
            if user not in infected:
                discovered.add(u)
                queue.extend(users_connected_to(u) - infected)

        return infected


    def users_connected_to(root_user):
        ''' returns a set containing the users that are connected to the given user '''