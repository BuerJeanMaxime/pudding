from typing import Dict, List

import community as community_louvain
import networkx as nx

from App.Token.Token import Token


class CommunityCenter:
    def __init__(self,graph):
        self.graph: nx.Graph = graph

    def get_communities(self):
        communities: List[List[str]] = self._translate_at_the_right_format(community_louvain.best_partition(self.graph,randomize=False,weight='weight'))
        return communities

    def _translate_at_the_right_format(self, community_wrong_format : Dict[Token,int]) -> List[List[str]]:
        nb_communities: int = max(community_wrong_format.values())
        community_right_format: List[List[str]] = [[] for _ in range(nb_communities+1)]
        for node,nb_community in community_wrong_format.items():
            community_right_format[nb_community].append(node.spacy_token.text)
        return community_right_format