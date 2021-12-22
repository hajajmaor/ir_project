"""
methods to do the indexing
"""
from os import listdir
from typing import List, Dict
from pickle import loads as load_from_pickle_file
from pickle import dump as save_to_pickle_file
from nltk.stem.porter import PorterStemmer
from position_index_class import PositionalIndex
INDEX_DIR = "./indexes/"
ARTICLES_DIR = "./articles/"

with open("stopWordPickle", "rb") as stopWordPickle:
    stop_words: List[str] = load_from_pickle_file(stopWordPickle.read())
del stopWordPickle


def _is_stop_word(word: str) -> bool:
    """sumary_line: check if the word is a stop word

    Keyword arguments:
    word -- word to test
    Return: true/false if the word is a stop word
    """
    return word in stop_words


def _do_case_folding(text: str) -> str:
    """sumary_line: do case folding

    Keyword arguments:
    text -- text to fold
    Return: text after case folding
    """
    # TODO: 1. remove dots space ? ! " ' `
    return text.lower()


def _remove_stop_words(text: str) -> str:
    """
    remove stop words from the text
    """
    text = _do_case_folding(text)
    text = text.split(" ")
    text = [word for word in text if not _is_stop_word(word)]
    text = " ".join(text)
    return text


def _preform_stemming_using_porter(text: str) -> str:
    """
    preform stemming using porter
    """
    stemmer = PorterStemmer()
    text = text.split(" ")
    text = [stemmer.stem(word) for word in text]
    text = " ".join(text)
    return text


def _generate_index_for_an_article(text: str) -> Dict[str, List[int]]:
    """generate index for an article

    Args:
        text (str): text of the article
        doc_id (int): id of the article

    Returns:
        Dict[str, List[PositionIndex]]:
            keys == the words,
            values == list of indexes of the token in the article
    """
    index: Dict[str, List[int]] = {}
    text = text.split(" ")
    for index_position, word in enumerate(text):
        if word not in index:
            # index[word] = PositionalIndex(doc_id, index_position)
            index[word] = [index_position]
        else:
            index[word].append(index_position)
    return index


def _add_to_index(index_for_file: Dict[str, List[int]], doc_id: int):
    """
    add the index to the global index
    """

    try:
        with open(f"{INDEX_DIR}indexPickle", "rb") as index_pickle:
            main_index: Dict[str, List[PositionalIndex]] = load_from_pickle_file(
                index_pickle.read()
            )
    except:
        main_index: Dict[str, List[PositionalIndex]] = {}

    for word, positions in index_for_file.items():
        if word not in main_index:
            main_index[word] = [PositionalIndex(doc_id, positions)]
        else:
            main_index[word].append(PositionalIndex(doc_id, positions))

    # index_pickle = open(f"{INDEX_DIR}indexPickleAfterDoc{doc_id}", "w")
    # temp_file = open(f"{INDEX_DIR}indexPickleAfterDoc{doc_id}", "w+")
    with open(f"{INDEX_DIR}indexPickleAfterDoc{doc_id}", "w+") as index_pickle:
        with open(f"{INDEX_DIR}indexPickleAfterDoc{doc_id}", "w+") as temp_file:
            save_to_pickle_file(main_index, index_pickle)
            save_to_pickle_file(main_index, temp_file)
    # index_pickle.close()
    # temp_file.close()


def process_document(doc_id: int, text: str = None, file_name: str = None):
    """
        process a document
    """
    if file_name:
        with open(file_name, "r", encoding="utf-8") as file:
            text = file.read()
    elif not text:
        # """if the text and file_name are None"""
        raise ValueError("Either text or file_name must be provided")
    # else - there is a text
    doc_processed = _remove_stop_words(text)
    doc_processed = _do_case_folding(doc_processed)
    doc_processed = _preform_stemming_using_porter(doc_processed)
    index_for_file = _generate_index_for_an_article(doc_processed)
    _add_to_index(index_for_file, doc_id)


process_document(
    1, file_name="articels/Visualizing clustering andpredicting the behavior of museum visitors.txt")
