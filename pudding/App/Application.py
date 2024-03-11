from pudding.App.communities_finder.CommunityCenter import CommunityCenter
from pudding.App.graph_builder.GraphBuilder import GraphBuilder
from pudding.App.tokenizer.TokenWizard import TokenWizard


class Application:

    def __init__(self,token_wizard,graph_builder,community_center):
        self.token_wizard: TokenWizard = token_wizard
        self.graph_builder: GraphBuilder = graph_builder
        self.community_center: CommunityCenter = community_center

    def run(self):
        self.token_wizard.enchance_tokens()
        self.graph_builder.get_complete_graph()
        communities = self.community_center.get_communities()
        return communities