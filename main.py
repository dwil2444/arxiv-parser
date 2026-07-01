#!/usr/bin/env python
import fire

from utils.logger import CustomLogger
from utils.parser import make_query
from utils.results import renderMarkdownTable

logger = CustomLogger(__name__)


def main(keyword=None, cat=None, keywords=None, timeout=30):
    """Search arXiv by keyword(s) and render matching results to README.md."""
    if keyword is not None:
        logger.info(f'Searching arXiv for keyword: {keyword}')
        results = make_query(keyword, cat, timeout)
    elif keywords is not None:
        logger.info(f'Reading keywords from: {keywords}')
        with open(keywords, 'r') as f:
            keyword_list = f.read().splitlines()
        for item in keyword_list:
            logger.info(f'Searching arXiv for keyword: {item}')
            results = make_query(item, cat, timeout)
    else:
        logger.error('Either keyword or keywords must be provided.')
        raise ValueError('Either keyword or keywords must be provided.')
    logger.info(f'Rendering {len(results)} results to README.md')
    renderMarkdownTable(results)


if __name__ == '__main__':
    fire.Fire(main)
