from typing import Dict


class Token:

    def __init__(self,spacy_token,is_relevent: bool):
        self.spacy_token = spacy_token
        self.relation: Dict[Token,float] = {}
        self.is_relevent: bool = is_relevent

    def __repr__(self):
        return f"{self.spacy_token.text}"
