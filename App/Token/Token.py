from typing import Dict


class Token:

    def __init__(self,spacy_token):
        self.spacy_token: str = spacy_token
        self.relation: Dict[Token,float] = {}
