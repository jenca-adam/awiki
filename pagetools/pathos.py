def make_authors(authors):
    result=[]
    for author in authors:
        result.append(f'<a style="color:red;" href="/search?query={author}&fields=author" title="View all articles by {author}">{author}</a>&comma;&nbsp;')
    return ''.join(result)
