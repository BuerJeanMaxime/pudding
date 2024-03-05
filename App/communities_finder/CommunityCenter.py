from typing import Dict, List

import community as community_louvain

from App.Token.Token import Token


class CommunityCenter:
    def __init__(self,graph):
        self.graph = graph

    def get_communities(self):
        communities = self._translate_at_the_right_format(community_louvain.best_partition(self.graph,randomize=False,weight='weight'))
        return communities

    def _translate_at_the_right_format(self, community_wrong_format : Dict[Token,int]) -> List[List[str]]:
        nb_communities = max(community_wrong_format.values())
        community_right_format = [[] for _ in range(nb_communities+1)]
        for node,nb_community in community_wrong_format.items():
            community_right_format[nb_community].append(node.spacy_token.text)
        return community_right_format