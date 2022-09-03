from collections import defaultdict


def anagrams(words: [str]):
    result = defaultdict(list)
    for word in words:
        result[''.join(sorted(word))].append(word)

    return list(result.values())


if __name__ == '__main__':
    import unittest

    expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    actual = anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])

    unittest.TestCase.assertListEqual(unittest.TestCase(), expected, actual)
