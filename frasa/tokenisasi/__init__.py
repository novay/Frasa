# Frasa NLP Services: Tokenisasi
#
# Copyright (C) 2023 Frasa Project
# Author: Novianto Rahmadi <novay@btekno.id>
# URL: <https://frasa.id/>
# For license information, see LICENSE.TXT

# Tokenization of words
def token_kata(text, preserve_line=False):
    """
    Return a tokenized copy of *text*,
    using NLTK's recommended word tokenizer
    (currently an improved :class:`.TreebankWordTokenizer`
    along with :class:`.PunktSentenceTokenizer`
    for the specified language).

    :param text: text to split into words
    :type text: str
    :param preserve_line: A flag to decide whether to sentence tokenize the text or not.
    :type preserve_line: bool
    """
    sentences = [text] if preserve_line else token_frasa(text)
    return [
        token for sent in sentences for token in _treebank_word_tokenizer.tokenize(sent)
    ]
    
def token_frasa(text, preserve_line=False):
    """
    Return a tokenized copy of *text*,
    using NLTK's recommended word tokenizer
    (currently an improved :class:`.TreebankWordTokenizer`
    along with :class:`.PunktSentenceTokenizer`
    for the specified language).

    :param text: text to split into words
    :type text: str
    :param preserve_line: A flag to decide whether to sentence tokenize the text or not.
    :type preserve_line: bool
    """
    sentences = [text] if preserve_line else token_frasa(text)
    return [
        token for sent in sentences for token in _treebank_word_tokenizer.tokenize(sent)
    ]