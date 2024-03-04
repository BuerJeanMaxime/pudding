from typing import List


class Token:

    def __init__(self,token):
        self.token: str = token
        self.relation: List[Token] = []
