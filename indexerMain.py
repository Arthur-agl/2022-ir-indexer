from os import listdir, path
from warcio.archiveiterator import ArchiveIterator
from nltk.stem import RSLPStemmer
from indexManager import IndexManager

from textAnalyze import reduce_analyze_text

THREADS = 1

im = IndexManager()


def indexerMain(mem_limit, corpus_input, index_output):
    corpus_files = listdir(corpus_input)
    file_total = len(corpus_files)

    warc_filename = corpus_files[0]

    ps = RSLPStemmer()

    with open(path.join(corpus_input, warc_filename), 'rb') as stream:
        for idx, record in enumerate(ArchiveIterator(stream)):

            if idx == 22:
                # Get text
                content = record.raw_stream.read().decode(encoding='UTF-8', errors='ignore')

                # Get term and tf pair
                index_entries = reduce_analyze_text(content)

                im.add_entries(index_entries)

                the_index = im.get_index()
                print(the_index)

            if idx > 22:
                break


def index_insert(index, element):
    if element not in index:
        index[element] = []
    index[element].append(element)


def parse_content(): pass
