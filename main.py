#!./venv/bin/python
from utils.parser import make_query
from utils.results import renderMarkdownTable
import argparse
import arxiv


def main():
    parser = argparse.ArgumentParser(description="Get cli info")
    parser.add_argument('--keyword', metavar='K', type=str )
    parser.add_argument('--cat', metavar='C', type=str,)
    parser.add_argument('--keywords', metavar='KS', type=str)
    args = parser.parse_args()
    kw = args.keyword
    kws = args.keywords
    cat = args.cat
    if kw is not None:
        results = make_query(kw, cat)
    else:
        with open(kws, 'r') as f:
            kws_ = f.read().splitlines()
        for keyword in kws_:
            results = make_query(keyword, cat)
    renderMarkdownTable(results)


if __name__ == '__main__':
    main()
