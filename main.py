import writeas


def forkCPost(alias, slug):
    
    # TODO: Find a way to extract arguments from a post url instead of feeding in each argument individually

    c = writeas.NewClient()
    c.setToken('0000-0000-0000-0000-000000000000')
    
    # TODO: Make authentication cleaner/simpler...unique login function? Classes?

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

    # TODO: Redirect to url in web app (Flask)


def forkPost(id):

    c = writeas.NewClient()
    c.setToken('0000-0000-0000-0000-000000000000')
    
    # TODO: Make authentication cleaner/simpler...unique login function? Classes?

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

    # TODO: Redirect to url in web app (Flask)
