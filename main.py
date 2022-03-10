#!/Users/danewilliamson/PycharmProjects/arxiv-parser/venv/bin/python
from utils import Paper
import argparse
from utils import load_file, find_title, index_of_first


def main():
    pub_list = load_file("arxiv_file.html")
    print(pub_list[10].abstract)


if __name__ == '__main__':
    main()
