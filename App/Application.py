from App.tokenizer.Tokenizer import Tokenizer


class Application:

    def __init__(self,tokenizer,graph_builder,communities_finder):
        self.tokenizer: Tokenizer = tokenizer
        self.graph_builder = graph_builder
        self.communities_finder = communities_finder

    def run(self):
        enchanced_tokens = self.tokenizer.tokenize()
        graph = self.graph_builder.create_graph(enchanced_tokens)
        communities = self.communities_finder.extract_communities(graph)
        return communities