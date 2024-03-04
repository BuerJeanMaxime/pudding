from typing import Dict


class Token:

    def __init__(self,spacy_token):
        self.spacy_token = spacy_token
        self.relation: Dict[Token,float] = {}

    def __repr__(self):
        return f"{self.spacy_token.text}"
