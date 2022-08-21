from datetime import date
today = date.today()

def renderMarkdownTable(results):
    """

    :param results: the arxiv results
    :return: no value returned, results
    are rendered in README.md
    """
    with open ('./README.md', 'w', encoding='utf-8') as f:
        f.seek(0)
        date = today.strftime("%B %d, %Y")
        f.writelines('Updated on: ' + date + '\n')
        f.writelines('\n')
        f.writelines('Title | Author | Date Published | Notes | Link  ' + '\n')
        f.writelines('----- | ------ | ---- | ----- | ----' + '\n')
        for result in results:
            title = result.title
            authors = ''.join([auth.name + ', ' for auth in result.authors])
            dp = result.published
            dp = dp.strftime("%B %d, %Y")
            notes = result.summary.split('\n')[0]
            link = result.pdf_url
            line = '**' + title + '**' + ' | ' + authors + ' | ' + dp + ' | ' + notes + ' | ' + link + ' | '
            f.writelines(line + '  ' +  '\n')

        f.writelines('\n')
        f.writelines('\n')
        f.close()

