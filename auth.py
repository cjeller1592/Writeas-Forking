import writeas


def loginUser(username, password):
    c = writeas.NewClient()

    try:

        u = c.login(username, password)
        access_token = u['access_token']

        c.setToken(access_token)

    except KeyError:
        return None

    return access_token
