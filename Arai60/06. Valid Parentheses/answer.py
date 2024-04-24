class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        history = list()

        for char in s:
            if char in pairs:
                history.append(char)
                continue

            if history and pairs[history[-1]] == char:
                history.pop()
            else:
                return False

        return not history
