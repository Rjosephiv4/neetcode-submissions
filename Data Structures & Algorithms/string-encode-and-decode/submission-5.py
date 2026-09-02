class Solution:
    def __init__(self):
        self.lengths = []

    def encode(self, strs: List[str]) -> str:
        self.lengths = []  # reset every encode
        output = ""
        for string in strs:
            self.lengths.append(len(string))
            output += string
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        last = 0

        for length in self.lengths:
            output.append(s[last:last + length])
            last += length

        return output