import unittest

import networkx as nx

from pudding.App.Token.Token import Token
from pudding.App.graph_builder.GraphBuilder import GraphBuilder
from pudding.Test.mocks.MockSpacyToken import MockSpacyToken


class TestGraphBuilder(unittest.TestCase):

    def helper_init_graph_builder_object(self):
        def _helper_init_enchanced_tokens():
            foot = Token(MockSpacyToken("foot"),True)
            gf38 = Token(MockSpacyToken("gf38"),True)

            foot.relation[gf38] = 900
            gf38.relation[foot] = 878
            enchanced_tokens = [foot,gf38]
            return enchanced_tokens

        enchanced_tokens = _helper_init_enchanced_tokens()
        graph_builder = GraphBuilder(enchanced_tokens)
        return graph_builder

    def helper_asser_graph(self,graph_output):
        graph_assertable = {}
        for key, value in graph_output.items():
            graph_assertable[str(key)] = str(value)
        return graph_assertable

    def test_graph_constitution(self):
        graph_output = nx.to_dict_of_dicts(self.helper_init_graph_builder_object().get_complete_graph())
        expected = {'foot': "{gf38: {'weight': 878}}", 'gf38': "{foot: {'weight': 878}}"}
        graph_assertable = self.helper_asser_graph(graph_output)
        self.assertEqual(expected,graph_assertable)
