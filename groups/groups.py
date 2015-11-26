from .group import Group
import itertools


def Sn(N):
    ''' Generate symmetric group
    '''
    if N == 0:
        raise Exception("Size must be > 0")
    items = [item for item in itertools.permutations(list(range(N)))]
    gr = Group(items, 'Sn({0})'.format(N))
    gr.add_property('rational', True)
    return gr


def Zn(N):
    ''' Generate cyclic group
        Graphical representation of finite groups
        https://en.wikipedia.org/wiki/Cyclic_group#Cycle_graph
    '''
    if N == 0:
        raise Exception("Size must be > 0")
    items = list(range(N))
    result = []
    for item in items:
        tmpresult = []
        for item2 in items:
            tmpresult.append((item + item2) % N)
        result.append(tmpresult)
    return Group(result, 'Zn({0})'.format(N))
