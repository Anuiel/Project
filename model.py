import string
import re
import numpy as np
import os


class GenWords:
    def __init__(self):
        self.data = None

    def fit(self, dir, prefix_size=1):
        self.prefix_size = prefix_size
        files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
        prefix_dict = {}
        for file in files:
            with open(os.path.join(dir, file)) as f:
                text = f.read()
            words = self.fix_text(text).split(" ")
            for prefix, words_dict in self.count_prefixes(words, prefix_size).items():
                if prefix not in prefix_dict:
                    prefix_dict[prefix] = {}
                for word, count in words_dict.items():
                    if word not in prefix_dict[prefix]:
                        prefix_dict[prefix][word] = 0
                    prefix_dict[prefix][word] += count
        data = {}
        for prefix, words_dict in prefix_dict.items():
            data[prefix] = (tuple(words_dict.keys()), tuple([float(value) / sum(words_dict.values())
                                                             for value in words_dict.values()]))

        self.data = data

    @staticmethod
    def fix_text(word):
        return re.sub(r'[-!@#$%^&*()_+=\[\]{}\|`~;:\'"“<>?,’./]', '', re.sub(r'[\t\n]', ' ', word)).lower()

    @staticmethod
    def count_prefixes(words, prefix_size):
        n = len(words)
        prefix_dict = {}

        for i in range(prefix_size, n):
            prev = tuple(words[i - prefix_size: i])
            next = words[i]
            if prev not in prefix_dict:
                prefix_dict[prev] = {}
            if next not in prefix_dict[prev]:
                prefix_dict[prev][next] = 0
            prefix_dict[prev][next] += 1
        return prefix_dict

    def new_word(self, prefix):
        if prefix not in self.data:
            prefix = self.random_prefix()
        return np.random.choice(self.data[prefix][0], p=self.data[prefix][1])

    def random_prefix(self):
        return list(self.data.keys())[np.random.choice(len(self.data.keys()))]

    def generate(self, length, prefix=""):
        if self.data is None:
            return "Where is my data"
        if prefix == "":
            prefix = self.random_prefix()
        ans = list(prefix)
        for _ in range(length):
            ans.append(self.new_word(tuple(ans[-self.prefix_size:])))
        return " ".join(ans)

    def get_data(self):
        return self.data
