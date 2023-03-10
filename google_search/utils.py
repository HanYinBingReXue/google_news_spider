def word_count(str):
    counts = dict()
    words = str.split()
    # 不需要的单词
    blacklist = [
        "the",
        "and",
        "to",
        "in",
        "of",
        "a",
        "its",
        "for",
        "with",
        "that",
        "as",
        "it",
        "on",
        "is",
        "The",
        "from",
        "by",
        "has",
        "was",
        "at",
        "an",
        "are",
        "more",
        "have",
        "which",
        "be",
        "said",
    ]
    for word in words:
        word = word.lower()
        if word not in blacklist and (not word.isdigit()):
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts
