from itertools import combinations
from typing import List

from App.Token.Token import Token


class TokenWizard:
    def __init__(self,syntagms,mwes,spacy):
        self.syntagms = syntagms
        self.mwes = mwes
        self.spacy = spacy

    def enchance_tokens(self):
        tokens = [Token(spacy_token) for spacy_token in self.spacy(" ".join(self.syntagms))]
        self.find_relations_between_tokens(tokens)
        return tokens
    def find_relations_between_tokens(self, tokens: List):
        for token_1,token_2 in combinations(tokens, r=2):
            score = token_1.spacy_token.similarity(token_2.spacy_token)
            if score < 0.55:
                continue
            token_1.relation[token_2] = (score*1000)

