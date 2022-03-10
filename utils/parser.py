from bs4 import BeautifulSoup
from .paper import Paper
import re


def find_indices(str, sub):
    """
    :param str: the string containing
                publication information
    :param sub: the delimiter separating
                the string
    :return: the indices of all occurrences
            of the delimiter
    """
    indices = [m.start() for m in re.finditer(sub, str)]
    if len(indices) < 6:
        return - 1
    else:
        return [indices[3] + 1, indices[4]]


def find_title(textBlock):
    """
    :param textBlock: the block of
            text corresponding to a
            single publication

    :return: the title of the publication
    """
    prefix = len("Title: ")
    start = textBlock.index('Title')
    end  = textBlock.index('Authors')
    return textBlock[start:end][prefix:].strip("\n")


def find_abstract(textBlock):
    """
    :param textBlock: the block of
            text corresponding to a
            single publication

    :return: the publication abstract
    """
    # find all instances of \\
    delim = find_indices(textBlock, "\\\\")
    if delim == -1:
        return "No Abstract"
    else:
        return textBlock[delim[0]: delim[1]].strip("\n")


def index_of_first(arxiv_str):
    """
    :param arxiv_str: the full
           string of arxiv papers

    :return: the index of the first
          publication, i.e. after
          all the preambles and headers,
          delimited by the first \\
    """
    count = 0
    i = 0
    while (count == 0):
        if(("\\") in arxiv_str[i]):
            count += 1
            return i
        i += 1
    return i


def load_file(file):
    """

    :param file: the name of the
            file to be opened

    :return: the html contents of
            the file
    """
    with open(file, "r") as f:
        text = f.read()
        soup = BeautifulSoup(text, 'html.parser')
        tags = soup.tagStack[0].text.split(
            "------------------------------------------------------------------------------")
        p_list = []
        j = index_of_first(tags)
        sub = tags[j:]
        for tag in tags[j:]:
            title = find_title(tag)
            abstract = find_abstract(tag)
            pub = Paper(title=title, abstract=abstract)
            p_list.append(pub)
    return p_list


__all__ = ["load_file", "index_of_first",
           "find_title"]