
import unittest

from code import cicdexample

def test_sample_single_word():
    l = ('foo', 'bar', 'foobar')
    word = cicdexample.sample(l)
    assert word in l

def test_sample_multiple_words():
    l = ('foo', 'bar', 'foobar')
    words = cicdexample.sample(l, 2)
    assert len(words) == 2
    assert words[0] in l
    assert words[1] in l
    assert words[0] is not words[1]

def test_generate_phrase_length():
    phrase = cicdexample.generate_phrase()
    assert len(phrase.split()) >= 2