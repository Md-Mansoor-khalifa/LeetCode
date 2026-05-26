from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Find starting indices of substring(s) in s that are concatenations of all words.

        Uses a sliding window over word-length chunks and counts word frequencies.
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        if len(s) < total_len:
            return []

        target_count = {}
        for word in words:
            target_count[word] = target_count.get(word, 0) + 1

        result: List[int] = []

        # Try all offsets within word length
        for offset in range(word_len):
            left = offset
            right = offset
            current_count = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in target_count:
                    current_count[word] = current_count.get(word, 0) + 1
                    count += 1

                    while current_count[word] > target_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == num_words:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    current_count.clear()
                    count = 0
                    left = right

        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
    ]

    for i, (s, words, expected) in enumerate(tests, start=1):
        out = sol.findSubstring(s, words)
        print(f"Test {i}: s={s}, words={words}")
        print(f"Output: {out}, Expected: {expected}")
        print(f"Pass: {sorted(out) == sorted(expected)}")
        print()