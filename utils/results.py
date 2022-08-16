#TODO: Render results in MarkDown


def renderMarkdownTable(results):
    """

    :param results: the arxiv results
    :return: no value returned, results
    are rendered in README.md
    """
    with open ('./README.md', 'a') as f:
        f.seek(0)
        f.writelines('Title | Author | Conf | Notes | Link  ' + '\n')
        f.writelines('----- | ------ | ---- | ----- | ----' + '\n')
        for result in results:
            title = result.title
            authors = ''.join([auth.name + ', ' for auth in result.authors])
            conf  = 'arxiv'
            notes = result.summary.split('\n')[0]
            link = result.pdf_url
            line = '**' + title + '**' + ' | ' + authors + ' | ' + conf + ' | ' + notes + ' | ' + link + ' | '
            f.writelines(line + '  ' +  '\n')

        f.writelines('\n')
        f.writelines('\n')
        f.close()

