import unittest

import spacy

from App.tokenizer.Tokenizer import TokenWizard


class TestTokenWizardWhithoutSpacy(unittest.TestCase):

    def helper_init_token_wizard__whithout_spacy(self):
        pass


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
                              {'le': '{Le: 0.6559335589408875, le: 1.0}'},
                              {'foot': '{football: 0.7234567403793335}'},
                              {'Le': '{le: 0.6559335589408875}'},
                              {'football': '{soccer: 0.6507284045219421}'},
                              {"c'": "{c': 1.0}"},
                              {'est': '{est: 1.0}'},
                              {'bien': '{Franchement: 0.5703409314155579}'},
                              {'Franchement': '{}'},
                              {'le': '{}'},
                              {'soccer': '{}'},
                              {"c'": '{}'},
                              {'est': '{}'},
                              {'cool': '{}'}]
        assertable_relations = self.helper_assert_tokens_object__for_relations(output)
        self.assertEqual(expected_token, assertable_tokens)
        self.assertEqual(expected_relations, assertable_relations)
