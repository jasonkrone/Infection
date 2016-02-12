'''
By Jason Krone for Khan Academy

Implementation of Infection Class

'''

import networkx as nx
from user import User
from utils import *


def total_infection(G, source_id, version=None):
    '''
    infects the connected component containing the user with start_id 
    with the given version of the website and returns the uuid's of the 
    users in the infected component.
    '''
    assert source_id in G.node 

    # if not specified default to version of source_user 
    if version is None:
        version = G.node[source_id].site_version

    # spread the version using a BFS
    infected = bfs_apply(G, source_id, lambda uuid: G.node[uuid].set_site_version(version))

    return infected


def limited_infection(SG, n, delta, version):
    ''' 
    Infects m students with the given version where n - delta <= m <= n + delta

    Maintains contract that student who share a class must have the same version
    using the student graph (SG)
    '''

    infected = set()
    components = nx.connected_components(SG)
    component_dict = dict() 

    # use size of components as keys, with uuids of users in components as values
    for c in components:
        component_dict[len(c)] = c

    subset = subset_sum_within_range(component_dict.keys(), n, delta)

    # there was no subset that summed within our range 
    if subset is None:
        return None

    # infect students with version and add them to infected set
    for idx in subset:
        source_id = component_dict[idx].pop()
        infected.update(total_infection(SG, source_id, version)) 

    return infected



''' GRAPH HELPER METHODS '''



def bfs_apply(G, source_id, apply_fun=None):
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

