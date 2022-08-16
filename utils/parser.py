import arxiv


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


def make_query(keyword, category):
    """

    :param keyword: the keyword of the arxiv
    paper that you are interested in
    :param category: the relevant category

    :return: list of papers which match the
    keyword search in relevant category
    """
    verified = []
    search = arxiv.Search(
        query=keyword,
        max_results=10,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending
    )
    for result in search.results():
        if verify_taxonomy(result, category):
            verified.append(result)
    return verified

