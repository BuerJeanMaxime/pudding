from typing import List

import networkx as nx
from cdlib import algorithms


class CommunityCenter:
    def __init__(self,graph):
        self.graph: nx.Graph = graph

    def get_communities(self):
        communities: List[List[str]] = [[el.spacy_token.text for el in first_list] for first_list in algorithms.louvain(self.graph, weight='weight').communities]
        return communities