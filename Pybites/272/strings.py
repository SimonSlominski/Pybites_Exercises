from typing import List


def common_words(sentence1: List[str], sentence2: List[str]) -> List[str]:
    """
    Input:  Two sentences - each is a  list of words in case insensitive ways.
    Output: those common words appearing in both sentences. Capital and lowercase
            words are treated as the same word.

            If there are duplicate words in the results, just choose one word.
            Returned words should be sorted by word's length.
    """
    result = list(set([word
                       for word in _set_words_lower(sentence1)
                       if word in _set_words_lower(sentence2)]))

    return sorted(result, key=len)

def _set_words_lower(sentence):
    return [word.lower()
            for word in sentence]
