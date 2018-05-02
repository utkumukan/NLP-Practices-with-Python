#!/usr/bin/python

######################################################################
#   Yunhao Xu
#
#   Reguler expression
#
#   To run this code in command line:
#   $ $ python tokenizer.py input_tweets
######################################################################

import sys
import nltk
import re
import collections
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize, sent_tokenize

pattern_strings = r'''(?x) ([A-Z]\.)+ | (?:
    [<>]?
    [:;=8]                      # eyes
    [\-o\*\']?                  # optional nose
    [\)\]\(\[dDpP/\:\}\{@\|\\]  # mouth
    |
    [\)\]\(\[dDpP/\:\}\{@\|\\]  # mouth
    [\-o\*\']?                  # optional nose
    [:;=8]                      # eyes
    [<>]?
    )
    | <[^>]+> | [Hh][Tt][Tt][Pp]([Ss])?:\/((\/\S+)+(\.\S+)?)+
    | (?:@[\w_]+)
    | (?:\#+[\w_]+[\w\'_\-]*[\w_]+)
    | \w+(-\w+)*
    | \$?\d+(\.\d+)?%?
    | \.\.\.
    | [][.,;"'?():-_`] '''

hashtag_pattern = r'''(?:\#+[\w_]+[\w\'_\-]*[\w_]+)'''

word_pattern = r'''(?x) ([A-Z]\.)+
    | <[^>]+> | [Hh][Tt][Tt][Pp]([Ss])?:\/((\/\S+)+(\.\S+)?)+
    | (?:@[\w_]+)
    | (?:\#+[\w_]+[\w\'_\-]*[\w_]+)
    | \w+(-\w+)*
    | \$?\d+(\.\d+)?%?'''


class AnalyzeHappiness:
    def __init__(self, file='project1_tweets.txt'):
        self.lines = [line.strip() for line in open(file, 'r')]

    def tokenizer(self, string, pattern=pattern_strings):
        """
            A tokenizer for tweets
            Argument:   string -- any string
            pattern:    the components of the tokenizer
            return:     a tokenize list of strings
            """
        return nltk.regexp_tokenize(string, pattern)

    def mostCommHashtag(self, tag):
        """
            Compute top 20 hashtags that appear the most commonly in the same tweet with input hashtag
            Argument:   tag -- a hashtag that we want to compute the most commonly hashtag with
            return:     a list of the top 20 hashtags associated with the input hashtag
            """
        tags = {}
        topTwenty = []
        for line in self.lines:
            tokens = self.tokenizer(line, hashtag_pattern)
            counts = FreqDist()
            for t in tokens:
                counts.inc(t)
            if counts[tag] > 0:
                for t in counts.keys():
                    if t != tag:
                        if tags.has_key(t):
                            tags[t] = tags[t] + counts[t]
                        else:
                            tags[t] = counts[t]
        tags_sorted_by_counts = sorted(tags.items(), key=lambda x: x[1], reverse=True)
        for i in range(0, 20):
            topTwenty.append(tags_sorted_by_counts[i][0])
        return topTwenty

    def mostCommWords(self, tag, pos_tag_pattern):
        """
            This is a help method for mostCommNouns and mostCommVerbs.
            Argument:   tag --  a hashtag that we want to compute the most commonly hashtag with
                        pos_tag_pattern
                            --  the regular expression that used to match the POS tags
            return:     a list of the top 20 nouns associated with the input hashtag
            """
        words = {}
        topTwenty = []
        j = 0
        for line in self.lines:
            hasTag = False
            for t in self.tokenizer(line, hashtag_pattern):
                if t == tag:
                    hasTag = True
                    break
            if hasTag:
                counts = FreqDist()
                tokens = self.tokenizer(line, word_pattern)
                pos = nltk.pos_tag(tokens)
                for p in pos:
                    if re.match(pos_tag_pattern, p[1]):
                        counts.inc(p[0])
                for n in counts.keys():
                    if words.has_key(n):
                        words[n] = words[n] + counts[n]
                    else:
                        words[n] = counts[n]
        words_sorted_by_counts = sorted(words.items(), key=lambda x: x[1], reverse=True)
        for i in range(0, 20):
            topTwenty.append(words_sorted_by_counts[i][0])

        return topTwenty

    def mostCommNouns(self, tag):
        """
            Compute top 20 nouns that appear the most commonly in the same tweet with input hashtag
            Argument:   tag -- a hashtag that we want to compute the most commonly hashtag with
            return:     a list of the top 20 nouns associated with the input hashtag
            """
        return self.mostCommWords(tag=tag, pos_tag_pattern='NN\w*')

    def mostCommVerbs(self, tag):
        """
            Compute top 20 verbs that appear the most commonly in the same tweet with input hashtag
            Argument:   tag -- a hashtag that we want to compute the most commonly hashtag with
            return:     a list of the top 20 verbs associated with the input hashtag
            """
        return self.mostCommWords(tag=tag, pos_tag_pattern='VB\w*')

    def conditionalProportion(self, tag):
        """
            Compute top 20 rank of the hashtags that are commonly associated with input hashtags
            Argument:   tag -- a hashtag that we want to compute the most commonly hashtag with
            return:     a list of the top 20 verbs associated with the input hashtag
            """
        tags = {}
        total = {}
        topTwenty = []
        for line in self.lines:
            tokens = self.tokenizer(line, hashtag_pattern)
            counts = FreqDist()
            for t in tokens:
                counts.inc(t)
                if total.has_key(t) and t != tag:
                    total[t] = total[t] + 1
                else:
                    total[t] = 1
            if counts[tag] > 0:
                for t in counts.keys():
                    if t != tag:
                        if tags.has_key(t):
                            tags[t] = tags[t] + counts[t]
                        else:
                            tags[t] = counts[t]
        prop = {}
        for t in total.keys():
            if tags.has_key(t):
                prop[t] = float(tags[t]) / total[t]
            else:
                prop[t] = 0.0
        prop_sorted_by_counts = sorted(prop.items(), key=lambda x: x[1], reverse=True)

        for i in range(0, 20):
            topTwenty.append(prop_sorted_by_counts[i][0])

        return topTwenty


if __name__ == '__main__':
    filename = 'project1_tweets.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    protect1 = AnalyzeHappiness(file=filename)
    print(
    'the top 20 hashtags associated with #happy:')
    print(
    protect1.mostCommHashtag('#happy'))
    print(
    'the top 20 hashtags associated with #sad:')
    print(
    protect1.mostCommHashtag('#sad'))
    print(
    'the top 20 nouns associated with #happy:')
    print(
    protect1.mostCommNouns('#happy'))
    print(
    'the top 20 nouns associated with #sad:')
    print(
    protect1.mostCommNouns('#sad'))
    print(
    'the top 20 verbs associated with #happy:')
    print(
    protect1.mostCommVerbs('#happy'))
    print(
    'the top 20 verbs associated with #sad:')
    print(
    protect1.mostCommVerbs('#sad'))
    print(
    'the conditional proportions of hashtags associated with "#happy":')
    print(
    protect1.conditionalProportion('#happy'))
    print(
    'the conditional proportions of hashtags associated with #sad:')
    print(
    protect1.conditionalProportion('#sad'))