import re
from typing import List


class Tokenizer(object):
    def __init__(self):
        self.pattern = self._get_regex_compiler()

    @staticmethod
    def _get_regex_compiler() -> re.Pattern:
        tokenizing_rule_regex = "|".join([
            r"[가-힣]+",  # 연속된 한글
            r"[ㄱ-ㅎ]+",  # 연속된 자모
            r"[a-z|0-9]+",  # 연속된 영문 및 숫자
            r"[^\s|가-힣|ㄱ-ㅎ|a-z|0-9]+",  # 그 외 문자는 묶어서 하나로 취급(공백 기준으로 분리)
        ])
        return re.compile(f"({tokenizing_rule_regex})")

    def tokenize(self, text: str) -> List[str]:
        return self.pattern.findall(text.lower())
