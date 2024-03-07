from itertools import permutations
from typing import List

import spacy

from App.Token.Token import Token


class TokenWizard:
    def __init__(self,syntagms,mwes,spacy_name):
        self.syntagms = syntagms
        self.mwes = mwes
        self.spacy = spacy.load(spacy_name)

    def enchance_tokens(self):
        tokens = [Token(spacy_token,self.is_relevent_token(spacy_token)) for spacy_token in self.spacy(" ".join(self.syntagms))]
        self.find_relations_between_tokens(tokens)
        return tokens
    def find_relations_between_tokens(self, tokens: List):
        for token_1,token_2 in permutations(tokens, r=2):
            if not token_1.is_relevent or not token_2.is_relevent:
                continue
            score = token_1.spacy_token.similarity(token_2.spacy_token)
            if score < 0.55:
                continue
            token_1.relation[token_2] = (score*1000)

    def is_relevent_token(self,spacy_token):
        return not ((spacy_token.is_punct)
            or (spacy_token.is_stop)
            or (spacy_token.is_bracket)
            or (spacy_token.is_quote)
            or (spacy_token.is_oov)
            or (spacy_token.pos_ == "DET")
            or (spacy_token.pos_ == "PRON"))
