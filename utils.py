import writeas
# TODO: Make exception handling more robust other than returning None

# Fork over as an annonymous post
def forkPost(alias, slug, token):

    c = writeas.NewClient()
    c.setToken(token)

    try:
        p = c.retrieveCPost(alias, slug)
        title = p['title']
        body = p['body']

        fp = c.createPost(body, title)
        id = fp['id']

        url = 'https://write.as/' + 'edit/%s' % id

# If run into an error, like the post not existing, we return None
# This None will be handled on the app level

    except Exception as e:
        return None
  

    return url

# Fork over as a collection post
def forkCPost(alias, slug, collection, token):

    c = writeas.NewClient()
    c.setToken(token)

    try:
        p = c.retrieveCPost(alias, slug)
        title = p['title']
        body = p['body']

        fp = c.createCPost(collection, body, title)
        title = p['title']
        body = p['body']

        slug = fp['slug']

        url = 'https://write.as/' + '%s/%s/edit' % (collection, slug)

    except Exception as e:
        return None

    return url

