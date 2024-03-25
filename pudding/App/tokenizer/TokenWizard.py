import math
from itertools import permutations
from typing import List, Union

import spacy

from pudding.App.Token.Token import Token


class TokenWizard:
    def __init__(self,syntagms,mwes,spacy_name):
        self.syntagms: List[str] = syntagms
        self.mwes: List[str] = mwes
        self.spacy = spacy.load(spacy_name)

    def enchance_tokens(self) -> List[Token]:
        tokens: List[Token] = [Token(spacy_token,self.is_relevent_token(spacy_token)) for spacy_token in self.spacy(" ".join(self.syntagms))]
        self.find_relations_between_tokens(tokens)
        return tokens
    def find_relations_between_tokens(self, tokens: List[Token]):
        for token_1,token_2 in permutations(tokens, r=2):
            if not token_1.is_relevent or not token_2.is_relevent:
                continue
            score = token_1.spacy_token.similarity(token_2.spacy_token)
            if score < 0.45:
                continue
            token_1.relation[token_2] = (
                        math.log2(
                            (score*1000 * self.is_same_tokens(token_1,token_2)) *
                            self.is_identical_tokens(token_1, token_2)
                        )
            )

    def is_same_tokens(self,token_1,token_2) -> Union[int,float]:
        return 0.5 if token_1.spacy_token.lemma_ == token_2.spacy_token.lemma_ else 1

    def is_same_pos(self, token_1, token_2) -> Union[int,float]:
        return 0.5 if token_1.spacy_token.pos_ == token_2.spacy_token.pos_ else 1

    def is_identical_tokens(self,token_1, token2) -> Union[int,float]:
        return 0.5 if token_1.spacy_token.text == token2.spacy_token.text else 1

    def is_relevent_token(self,spacy_token) -> bool:
        return not ((spacy_token.is_punct)
            or (spacy_token.is_stop)
            or (spacy_token.is_bracket)
            or (spacy_token.is_quote)
            or (spacy_token.is_oov)
            or (spacy_token.pos_ == "DET")
            or (spacy_token.pos_ == "PRON"))
