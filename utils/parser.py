import socket

import arxiv

from utils.logger import CustomLogger

logger = CustomLogger(__name__)
ARXIV_QUERY_URL_FORMAT = 'https://export.arxiv.org/api/query?{}'


def verify_taxonomy(result, targ):
    """"
    :param result: the arxiv result returned
    by  arxiv library

    :param targ: the  target category

    :return: TRUE if the result's primary category is
    in the specified taxonomy. FALSE otherwise
    """
    cat = result.primary_category
    pc = cat.split('.')[0]
    if pc.lower() == targ.lower():
        return True
    return False


def make_query(keyword, category, timeout=30):
    """

    :param keyword: the keyword of the arxiv
    paper that you are interested in
    :param category: the relevant category
    :param timeout: number of seconds before the arxiv API request times out

    :return: list of papers which match the
    keyword search in relevant category
    """
    timeout = int(timeout)
    socket.setdefaulttimeout(timeout)
    arxiv.Client.query_url_format = ARXIV_QUERY_URL_FORMAT
    verified = []
    logger.info(f'Querying arXiv for "{keyword}" with timeout={timeout}s')
    search = arxiv.Search(
        query=keyword,
        max_results=10,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )
    client = arxiv.Client(page_size=10)
    for result in client.results(search):
        logger.info(f'Received result: {result.title}')
        if verify_taxonomy(result, category):
            verified.append(result)
    logger.info(f'Found {len(verified)} matching results for "{keyword}"')
    return verified
