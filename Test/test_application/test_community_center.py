import unittest

from App.Token.Token import Token
from App.communities_finder.CommunityCenter import CommunityCenter
from App.graph_builder.GraphBuilder import GraphBuilder
from Test.mocks.MockSpacyToken import MockSpacyToken


class TestCommunityCenter(unittest.TestCase):

    def helper_create_token_list(self):
        foot = Token(MockSpacyToken("foot"),True)
        gf38 = Token(MockSpacyToken("gf38"),True)

        foot.relation[gf38] = 900
        gf38.relation[foot] = 878
        enchanced_tokens = [foot, gf38]
        return enchanced_tokens

    def helper_create_community_center_object(self):
        tokens = self.helper_create_token_list()
        graph = GraphBuilder(enchanced_tokens=tokens).get_complete_graph()
        cc = CommunityCenter(graph=graph)
        return cc

    def test_get_communities(self):
        output = self.helper_create_community_center_object().get_communities()
        expected = [['foot', 'gf38']]
        self.assertEqual(expected,output)