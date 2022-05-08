import re


class Transformer(object):
    def __init__(self):
        self.pattern = self._get_regex_compiler()

    @staticmethod
    def _get_regex_compiler() -> re.Pattern:
        regex = r"\([\d]{4}\)$"
        return re.compile(regex)

    def substitute(self, text: str) -> str:
        return self.pattern.sub("", text.lower())

    def extract(self, text: str) -> str:
        return self.pattern.search(text).group()[1: -1]

    @staticmethod
    def refine_genres(text: str) -> str:
        return text.replace("|", " ")
