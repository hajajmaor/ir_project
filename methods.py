"""
methods to do the indexing
https://www.nltk.org/api/nltk.tokenize.html
"""
from re import split as re_split
from string import punctuation
# from os import listdir
# from pandas import DataFrame
from typing import List, Dict
from pickle import loads as load_from_pickle_file
# from pickle import dump as save_to_pickle_file
from nltk.stem.porter import PorterStemmer
# from nltk.tokenize import word_tokenize
# from position_index_class import PositionalIndex
INDEX_DIR = "./indexes/"
ARTICLES_DIR = "./articels"

with open("stop_words_english.txt", "r") as file:
    stop_words = file.read().split("\n")


def do_case_folding(text: str) -> str:
    """sumary_line: do case folding

    Keyword arguments:
    text -- text to fold
    Return: text after case folding
    """
    text = text.replace(".", " ")
    text = text.replace("?", " ")
    text = text.replace("!", " ")
    text = text.replace("\"", " ")
    text = text.replace("'", " ")
    text = text.replace("`", " ")
    text = text.replace("’", " ")

    return text.lower()


def remove_stop_words(text: str) -> str:
    """
    remove stop words from the text
    """
    # text = do_case_folding(text)
    text = text.split(" ")
    text = [word for word in text if word not in stop_words]
    text = " ".join(text)
    return text


def preform_stemming_using_porter(text: str) -> str:
    """
    preform stemming using porter
    """
    stemmer = PorterStemmer()
    text = text.split(" ")
    text = [stemmer.stem(word) for word in text]
    text = " ".join(text)
    return text


# def _generate_index_for_an_article(text: str) -> Dict[str, List[int]]:
#     """generate index for an article

#     Args:
#         text (str): text of the article
#         doc_id (int): id of the article

#     Returns:
#         Dict[str, List[PositionIndex]]:
#             keys == the words,
#             values == list of indexes of the token in the article
#     """
#     index: Dict[str, List[int]] = {}
#     text = text.split(" ")
#     for index_position, word in enumerate(text):
#         if word not in index:
#             # index[word] = PositionalIndex(doc_id, index_position)
#             index[word] = [index_position]
#         else:
#             index[word].append(index_position)
#     return index


# def _add_to_index(index_for_file: Dict[str, List[int]], doc_id: int):
#     """
#     add the index to the global index
#     """

#     try:
#         with open(f"{INDEX_DIR}indexPickle", "rb") as index_pickle:
#             main_index: Dict[str, List[PositionalIndex]] = load_from_pickle_file(
#                 index_pickle.read()
#             )
#     except:
#         main_index: Dict[str, List[PositionalIndex]] = {}

#     for word, positions in index_for_file.items():
#         if word not in main_index:
#             main_index[word] = [PositionalIndex(doc_id, positions)]
#         else:
#             main_index[word].append(PositionalIndex(doc_id, positions))

#     # index_pickle = open(f"{INDEX_DIR}indexPickleAfterDoc{doc_id}", "w")
#     # temp_file = open(f"{INDEX_DIR}indexPickleAfterDoc{doc_id}", "w+")
#     with open(f"{INDEX_DIR}indexPickleAfterDoc{doc_id}", "w+") as index_pickle:
#         with open(f"{INDEX_DIR}indexPickleAfterDoc{doc_id}", "w+") as temp_file:
#             save_to_pickle_file(main_index, index_pickle)
#             save_to_pickle_file(main_index, temp_file)
#     # index_pickle.close()
#     # temp_file.close()


# def process_document(doc_id: int, text: str = None, file_name: str = None):
#     """
#         process a document
#     """
#     if file_name:
#         with open(file_name, "r", encoding="utf-8") as file:
#             text = file.read()
#     elif not text:
#         # """if the text and file_name are None"""
#         raise ValueError("Either text or file_name must be provided")
#     # else - there is a text
#     doc_processed = _remove_stop_words(text)
#     doc_processed = _do_case_folding(doc_processed)
#     doc_processed = _preform_stemming_using_porter(doc_processed)
#     index_for_file = _generate_index_for_an_article(doc_processed)
#     _add_to_index(index_for_file, doc_id)


# process_document(
#     1, file_name="articels/Visualizing clustering andpredicting the behavior of museum visitors.txt")

def process_document(doc_path: str) -> Dict[str, int]:
    """
        doc
    """
    with open(doc_path, "r", encoding="utf-8") as file:
        text = file.read()
    doc_processed = remove_stop_words(text)
    doc_processed = do_case_folding(doc_processed)
    doc_processed = preform_stemming_using_porter(doc_processed)
    result: Dict[str, int] = {}
    for word in re_split(f"[{punctuation}\n ]", doc_processed):
        if word not in result:
            result[word] = 1
    return result
