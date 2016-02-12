'''
By Jason Krone for Khan Academy

Implementation of Infection Class

'''

import networkx as nx
from user import User


class Infection(object):


    def __init__(self, user_graph, student_graph=None):
        '''creates a new infection object with the given nx.Graph'''
        assert type(user_graph) is nx.Graph
        
        self.G = user_graph
        self.CG = student_graph # this will look like connected cliques


    # TODO change this to take the graph
    def total_infection(self, G, source_id, version=None):
        '''
        infects the connected component containing the user with start_id 
        with the given version of the website and returns the uuid's of the 
        users in the infected component.
        '''
        assert source_id in G 

        # if not specified default to version of source_user 
        if version is None:
            version = G.node[source_id].site_version

        # spread the version using a BFS
        infected = self._bfs_apply(G, source_id, lambda uuid: G.node[uuid].set_site_version(version))

        return infected


    def limited_infection(self, n, delta, version):
        ''' 
        Infects m students with the given version where n - delta <= m <= n + delta

        Maintains contract that student who share a class must have the same version
        using the student graph (SG)
        '''


        infected = None
        components = nx.connected_components(self.SG)
        component_dict = dict() 

        # use size of components as keys, with uuids of users in components as values
        for c in component:
            component_dict[len(c)] = c

        subset = self._subset_sum_within_range(n - delta, n + delta)

        # there was no subset that summed within our range 
        if subset is None:
            return None

        # infect students with version and add them to infected set
        for idx in subset:
            source_id = component_dict[idx].pop
            infected.extend(self.total_infection(source_id, version))    # add graph to this

        return Infected



    ''' GRAPH HELPER METHODS '''
   


    def _bfs_apply(self, G, source_id, apply_fun=None):
        '''
        conducts a BFS of G starting at the user with the given source_id
        and calling the given apply function when nodes are first discovered
        '''
        assert source_id in G.node

        queue = [source_id]
        seen = set()

        while queue:
            uuid = queue.pop(0)
            if uuid not in seen:
                if apply_fun is not None:
                    apply_fun(uuid)

                seen.add(uuid)
                # add uninfected neighbors (i.e. students and teachers)
                queue.extend(set(G.neighbors(uuid)) - seen)

        return seen 



    ''' SUBSET SUM HELPER METHODS '''



    def _subset_sum_within_range(nums, n, delta):
        ''' 
        returns a subset of the given numbers that sum within the given range
        (n - delta, n + delta) if such a subset exists.  Otherwise, returns None
        '''

        subset = None
        subset_sum_arr = self._positive_subset_sum_table(nums, n + delta)

        # loop through values in range n - k to n + k
        for i in range(n - delta, n + delta + 1):

            # check if there is a sum set sum to i
            if type(subset_sum_arr[i]) is tuple:
                # get the subset that sums to i
                subset = self._get_subset_with_sum(subset_sum_arr, i)
                break

        return subset


    def _get_subset_with_sum(table, n):
        '''
        returns the subset of numbers listed in the table that sum to n
        '''

        subset = []
        i = n

        while i > 0:
            subset.append(table[i][1])
            i = table[i][2]

        return subset


    def _positive_subset_sum_table(A, x):
        '''
        attribution: this code was modified from
        http://www.geekviewpoint.com/python/dynamic_programming/positive_subset_sum
        '''

        # preliminary
        if x < 0 or x > sum( A ): # T = sum(A)
            return None 
     
        # algorithm
        sub_sum = [None] * ( x + 1 )
        sub_sum[0] = (True, 0, 0)
        p = 0
        while not sub_sum[x] and p < len( A ):
            a = A[p]
            q = x
            while not sub_sum[x] and q >= a:
                if not sub_sum[q] and sub_sum[q - a]:
                    sub_sum[q] = (True , a, q - a)
                q -= 1
            p += 1
        return sub_sum

