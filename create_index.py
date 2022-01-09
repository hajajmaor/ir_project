"""
    create indes for the project
"""

from os import listdir
from pickle import dump as save_to_pickle_file
from typing import Counter, Dict, List
# from pandas import DataFrame
from methods import process_document, INDEX_DIR, ARTICLES_DIR

# df = DataFrame()


def create_language_model_from_collection(collection: List[str]) -> Dict[str, float]:
    """
        generate language model from collection

    Args:
        collection (List[str]): [description]

    Returns:
        Dict[str, float]: [description]
    """
    language_model = {}
    counter = 0

    for doc in collection:
        counter += len(doc)
        for word in doc.split():
            if word not in language_model:
                language_model[word] = 1
            else:
                language_model[word] += 1

    # calculate probability of a word in the collection
    for word in language_model:
        language_model[word] = round(language_model[word] / counter*100, 7)
        # language_model[word] / counter

    return language_model


res: Dict[str, float] = None


def main():
    global res
    articels = listdir(ARTICLES_DIR)
    collection = []
    for art in articels[:2]:
        with open(f"{ARTICLES_DIR}/{art}", "r") as file:
            collection.append(file.read())
    res = create_language_model_from_collection(collection)

    # res = process_document(f"{ARTICLES_DIR}/art")
    # index_pickle = open(f"{INDEX_DIR}indexPickleAfterDoc{art}", "w")
    # df = df.append(res, ignore_index=True)
    # with open(f"{INDEX_DIR}indexPickleAfterDoc{art}", "w+") as index_pickle:
    # save_to_pickle_file(df, index_pickle)


main()
