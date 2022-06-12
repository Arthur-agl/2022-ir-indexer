import sys
#import resource
import argparse
from pathlib import Path
from indexerMain import indexerMain

MEGABYTE = 1024 * 1024
def memory_limit(value):
    limit = value * MEGABYTE
#   resource.setrlimit(resource.RLIMIT_AS, (limit, limit))

def main(memory_limit, corpus_directory, index_file):
  indexerMain(memory_limit, corpus_directory, index_file)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Process some integers.')
  parser.add_argument(
        '-m',
        dest='memory_limit',
        action='store',
        required=True,
        type=int,
        help='memory available'
    )

  parser.add_argument(
        '-c',
        dest='corpus_directory',
        action='store',
        required=True,
        type=Path,
        help='directory containing the corpus WARC files'
    )

  parser.add_argument(
        '-i',
        dest='index_file',
        action='store',
        required=True,
        # type=open,
        help='output file name'

    )
  
  args = parser.parse_args()
  memory_limit(args.memory_limit)

  try:
      main(args.memory_limit, args.corpus_directory, args.index_file)
  except MemoryError:
      sys.stderr.write('\n\nERROR: Memory Exception\n')
      sys.exit(1)


# You CAN (and MUST) FREELY EDIT this file (add libraries, arguments, functions and calls) to implement your indexer
# However, you should respect the memory limitation mechanism and guarantee
# it works correctly with your implementation