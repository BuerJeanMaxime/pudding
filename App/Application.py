from App.tokenizer.TokenWizard import TokenWizard


class Application:

    def __init__(self,token_wizard,graph_builder,community_center):
        self.token_wizard: TokenWizard = token_wizard
        self.graph_builder = graph_builder
        self.community_center = community_center

    def run(self):
        enchanced_tokens = self.token_wizard.enchance_tokens()
        graph = self.graph_builder.get_complete_graph()
        communities = self.community_center.get_communities()
        return communities