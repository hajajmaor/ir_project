"""
    create indes for the project
"""

from os import listdir
from pickle import dump as save_to_pickle_file
from pandas import DataFrame
from methods import process_document, INDEX_DIR, ARTICLES_DIR

df = DataFrame()
articels = listdir(ARTICLES_DIR)

for art in articels[:5]:
    res = process_document(f"{ARTICLES_DIR}/art")
    index_pickle = open(f"{INDEX_DIR}indexPickleAfterDoc{art}", "w")
    df = df.append(res, ignore_index=True)
    with open(f"{INDEX_DIR}indexPickleAfterDoc{art}", "w+") as index_pickle:
        save_to_pickle_file(df, index_pickle)
