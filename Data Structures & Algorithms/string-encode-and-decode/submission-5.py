class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_s = ""

        for word in strs:
            encode_s += str(len(word)) + "#" + word

        return encode_s

    def decode(self, s: str) -> List[str]:
        decode_s = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length

            decode_s.append(s[word_start:word_end])

            i = word_end

        return decode_s