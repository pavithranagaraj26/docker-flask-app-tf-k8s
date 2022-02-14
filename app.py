from flask import Flask
from env_vars import get_username, get_password

app = Flask(__name__)

#owner_name = get_owner()

@app.route('/')
def index():
    ATC_USERNAME = get_username()
    ATC_PASSWORD = get_password()
    return '{} \n {}'.format(ATC_USERNAME, ATC_PASSWORD)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)