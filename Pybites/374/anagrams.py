"""
Bite 374. Group Anagrams
As defined by the OED, an anagram is a word, phrase, or name formed by rearranging the letters of another.

Given a list of strings, return a list with any anagrams grouped together into sub-lists.

Example:
# >>> from  anagram import group_anagrams
# >>> anagrams = ["eat", "tea", "tan", "ate", "nat", "bat"]
# >>> group_anagrams(anagrams)
[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Example 2:
# >>> from  anagram import group_anagrams
# >>> anagrams = ["bat", "tab", "bad", "dab", "nat", "tan"]
# >>> group_anagrams(anagrams)
[["bad", "dab"], ["bat", "tab"], ["nat", "tan"]]
"""
def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Group anagrams together."""
    anagrams = {}

    for string in strings:
        sorted_string = ''.join(sorted(string))

        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]

    result = list(anagrams.values())
    return result
