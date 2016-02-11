'''
By Jason Krone for Khan Academy

Implementation of Infection Class

'''

import networkx as nx
from user import User


class Infection(object):


    def __init__(self, user_graph):
        '''creates a new infection object with the given nx.Graph'''
        assert type(user_graph) is nx.Graph
        
        self.G = user_graph


    def total_infection(self, source_id, version=None):
        '''
        infects the connected component containing the user with start_id 
        with the given version of the website and returns the uuid's of the 
        users in the infected component.
        '''
        assert source_id in self.G.node

        # if not specified default to version of source_user 
        if version is None:
            version = self.G.node[source_id].site_version

        # spread the version using a BFS
        infected = self._bfs_apply(source_id, lambda uuid: self.G.node[uuid].set_site_version(version))

        return infected


    def limited_infection(self, limit_fun, version):
        '''
        Infects a connect component of self.G whose size meets the contraints
        set by the given limit_fun, returning the component infected on success
        and None on failure.
        '''
        assert limit_fun is not None

        infected = None

        uuid_source = source_limited_infection(limit_fun)

        if uuid_source is not None:
            infected = total_infection(uuid_source)

        return infected


    def source_limited_infection(self, limit_fun):
        '''
        returns the uuid of the user from which you can spread an infection 
        that will be limited to m users where m is a number such that 
        limit_fun(m) returns True if such a user exists. Otherwise, returns none.
        '''
        assert limit_fun is not None

        seen = set()

        for uuid in self.G:
            if v not in seen:
                component = _bfs_apply(v) 
                seen.update(component)

            if limit_fun(len(component)):
                return v   

        return None


    def _bfs_apply(self, source_id, apply_fun=None):
        '''
        conducts a BFS of G starting at the user with the given source_id
        and calling the given apply function when nodes are first discovered
        '''
        assert source_id in self.G.node

        queue = [source_id]
        seen = set()

        while queue:
            uuid = queue.pop(0)
            if uuid not in seen:
                if apply_fun is not None:
                    apply_fun(uuid)

                seen.add(uuid)
                # add uninfected neighbors (i.e. students and teachers)
                queue.extend(set(self.G.neighbors(uuid)) - seen)

        return seen 


