#!/usr/bin/env python

import pandas as pd
import networkx as nx
from matplotlib import pyplot as plt
if __name__ == "__main__":
    airports=pd.DataFrame.from_csv('airports.dat')
    airlines=pd.DataFrame.from_csv('airlines.dat')
    routes=pd.DataFrame.from_csv('routes.dat')

    network=nx.MultiGraph()
    # print(network)
    # print(airports['iata'])
    # network.add_nodes_from(airports['iata'])
    tst=list(zip(routes.source,routes.destination))
    # print(tst)
    network.add_edges_from(tst)
    giant = max(nx.connected_component_subgraphs(network), key=len)
    degree_cutoff=10
    # toremove = [node for node,degree in giant.degree().items() if degree <= degree_cutoff]
    # while len(toremove):
    #     giant.remove_nodes_from(toremove)
    #     giant = max(nx.connected_component_subgraphs(giant), key=len)
    #     print(len(toremove))
    #     toremove = [node for node,degree in giant.degree().items() if degree <= degree_cutoff]
    # print(network.edges())
    giant = max(nx.connected_component_subgraphs(giant), key=len)
    nx.draw(giant,node_size=10)
    nx.write_multiline_adjlist(giant,"test.adjlist")
    plt.show(block=True)
