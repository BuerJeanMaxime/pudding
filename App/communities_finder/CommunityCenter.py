import community as community_louvain
class CommunityCenter:
    def __init__(self,graph):
        self.graph = graph

    def get_communities(self):
        communities = community_louvain.best_partition(self.graph,randomize=False,weight='weight')
        return communities