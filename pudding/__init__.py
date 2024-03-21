from typing import List

from pudding.App.Application import Application
from pudding.App.communities_finder.CommunityCenter import CommunityCenter
from pudding.App.graph_builder.GraphBuilder import GraphBuilder
from pudding.App.tokenizer.TokenWizard import TokenWizard


def get_communities_with_louvain_method(tokens: List[str],mwes: List[str],spacy_model: str) -> List[str]:
    communities = Application.create_App_object(tokens,mwes,spacy_model).run()
    return communities