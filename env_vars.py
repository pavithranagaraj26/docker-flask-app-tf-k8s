import os
def get_username():
    try:
        ATC_USERNAME = os.environ['ATC_USERNAME']

    except KeyError:
        ATC_USERNAME = 'no username'

    return 'ATC_USERNAME: {0}'.format(ATC_USERNAME)

def get_password():
    try:
        ATC_PASSWORD = os.environ['ATC_PASSWORD']

    except KeyError:
        ATC_PASSWORD = 'no Password'

    return 'ATC_PASSWORD: {0}'.format(ATC_PASSWORD)