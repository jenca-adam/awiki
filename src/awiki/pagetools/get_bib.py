import requests


def get_bib_doi(doi):
    if not doi:
        return None
    url = f"http://doi.org/{doi}"
    resp = requests.get(url, headers={"Accept": "application/x-bibtex"})
    if resp.ok and resp.headers["content-type"] == "application/x-bibtex":
        return resp.content
    return None


def get_bib_arxiv(arxiv_id):
    url = f"http://arxiv.org/bibtex/{arxiv_id}"
    resp = requests.get(url, headers={"Accept": "application/x-bibtex"})
    if resp.ok:  # lmaoo arxiv sucks
        return resp.content
    return None
