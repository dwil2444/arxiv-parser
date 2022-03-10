#!/Users/danewilliamson/PycharmProjects/arxiv-parser/venv/bin/python
from utils import Paper
import argparse
from utils import load_file


def parse_command_line():
    """
    :param: keyword: the keyword
            you want to search
            the titles for
    :return: the title of the paper
            which has the keyword
            of interest
    """
    parser = argparse.ArgumentParser(description="Get cli info")
    parser.add_argument('--keyword', metavar='K',)
    args = parser.parse_args()
    return args.keyword


def main():
    pub_list = load_file("arxiv.html")
    kw = parse_command_line()
    for pub in pub_list:
        if kw.lower() in pub.title.lower():
            print(pub.abstract)


if __name__ == '__main__':
    main()
