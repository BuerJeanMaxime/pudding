from App.tokenizer.Tokenizer import TokenWizard


class Application:

    def __init__(self,token_wizard,graph_builder,communities_finder):
        self.token_wizard: TokenWizard = token_wizard
        self.graph_builder = graph_builder
        self.communities_finder = communities_finder

    def run(self):
        enchanced_tokens = self.token_wizard.enchance_tokens()
        graph = self.graph_builder.create_graph(enchanced_tokens)
        communities = self.communities_finder.extract_communities(graph)
        return communities