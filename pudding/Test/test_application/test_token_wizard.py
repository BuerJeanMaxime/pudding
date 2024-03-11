import unittest

import spacy

from pudding.App.tokenizer.TokenWizard import TokenWizard


class TestTokenWizardWhithSpacy(unittest.TestCase):

    def helper_init_token_wizard__whith_spacy(self):
        syntagms = ["J'aime le foot", "Le football c'est bien", "Franchement le soccer c'est cool"]
        spacy_lang = spacy.load("fr_core_news_md")
        tw = TokenWizard(syntagms, [], spacy_lang)
        return tw

    def helper_assert_tokens_object(self, enchanced_tokens):
        assertable_tokens = [token.spacy_token.text for token in enchanced_tokens]
        return assertable_tokens

    def helper_assert_tokens_object__for_relations(self, enchanced_tokens):
        assertable_relations = [{token.spacy_token.text: str(token.relation)} for token in enchanced_tokens]
        return assertable_relations

    def test_enchance_tokens__with_spacy(self):
        tw = self.helper_init_token_wizard__whith_spacy()
        output = tw.enchance_tokens()
        assertable_tokens = self.helper_assert_tokens_object(output)
        expected_token = ["J'",
                          'aime',
                          'le',
                          'foot',
                          'Le',
                          'football',
                          "c'",
                          'est',
                          'bien',
                          'Franchement',
                          'le',
                          'soccer',
                          "c'",
                          'est',
                          'cool']
        expected_relations = [{"J'": '{}'},
                              {'aime': '{}'},
                              {'le': '{Le: 655.9335589408875, le: 1000.0}'},
                              {'foot': '{football: 723.4567403793335}'},
                              {'Le': '{le: 655.9335589408875, le: 655.9335589408875}'},
                              {'football': '{foot: 723.4567403793335, soccer: 650.7284045219421}'},
                              {"c'": "{c': 1000.0}"},
                              {'est': '{est: 1000.0}'},
                              {'bien': '{Franchement: 570.3409314155579}'},
                              {'Franchement': '{bien: 570.3409314155579}'},
                              {'le': '{le: 1000.0, Le: 655.9335589408875}'},
                              {'soccer': '{football: 650.7284045219421}'},
                              {"c'": "{c': 1000.0}"},
                              {'est': '{est: 1000.0}'},
                              {'cool': '{}'}]
        assertable_relations = self.helper_assert_tokens_object__for_relations(output)
        self.assertEqual(expected_token, assertable_tokens)
        self.assertEqual(expected_relations, assertable_relations)
