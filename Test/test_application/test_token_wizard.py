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

    def test_enchance_tokens__with_spacy(self):
        tw = self.helper_init_token_wizard__whith_spacy()
        assertable_tokens = tw.enchance_tokens()
        output = self.helper_assert_tokens_object(assertable_tokens)
        expected = ["J'",
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
        self.assertEqual(expected, output)
