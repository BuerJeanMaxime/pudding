import networkx as nx


class GraphBuilder:
    def __init__(self,enchanced_tokens):
        self.enchanced_tokens = enchanced_tokens
        self.graph = nx.Graph()

    def get_complete_graph(self):
        self._constitute_graph()
        return self.graph
    def _add_nodes(self):
        self.graph.add_nodes_from([token for token in self.enchanced_tokens if token.is_relevent])
    def _add_edges_and_weight(self):
        for token in self.enchanced_tokens:
            if token.relation == {}:
                continue
            for related_token, weight in token.relation.items():
                self.graph.add_edge(token,related_token,weight=weight)

    def _constitute_graph(self):
        self._add_nodes()
        self._add_edges_and_weight()