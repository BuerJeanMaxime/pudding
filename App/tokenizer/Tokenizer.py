from itertools import combinations
from typing import List

from App.Token.Token import Token


class Tokenizer:
    def __init__(self,syntagms,mwes,spacy,links_finder):
        self.syntagms = syntagms
        self.mwes = mwes
        self.spacy = spacy
        self.links_finder = links_finder

    def tokenize(self):
        tokens = [Token(spacy_token) for spacy_token in self.spacy(" ".join(self.syntagms))]
        self.find_relations_between_tokens(tokens)
        return tokens
    def find_relations_between_tokens(self, tokens: List):
        for token_1,token_2 in combinations(tokens, r=2):
            score = token_1.similarity(token_2)
            if score < 0.55:
                continue
            token_1.relation[token_2] = score

