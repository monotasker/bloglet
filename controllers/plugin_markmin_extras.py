if 0:
    from gluon import current
    response, request, db = current.response, current.request, current.db


def download():
    """
    Display media file from upload field.
    """
    return response.download(request, db)
