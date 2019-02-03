import writeas


def forkCPost(alias, slug):

    c = writeas.NewClient()
    c.setToken('e88e757a-d2b3-4916-5743-5c7d18ab467d')

    try:
        p = c.retrieveCPost(alias, slug)
        title = p['title']
        body = p['body']

        fp = c.createPost(body, title)
        id = fp['id']

        url = 'https://write.as/' + 'edit/%s' % id

    except Exception as e:
        print('Exception in forkCPost: %s' % e)
        return e

    return url

def forkPost(id):

    c = writeas.NewClient()
    c.setToken('e88e757a-d2b3-4916-5743-5c7d18ab467d')

    try:
        p = c.retrievePost(id)
        title = p['title']
        body = p['body']

        fp = c.createPost(body, title)
        id = fp['id']

        url = 'https://write.as/' + 'edit/%s' % id

    except Exception as e:
        print('Exception in forkCPost: %s' % e)
        return e

    return url
