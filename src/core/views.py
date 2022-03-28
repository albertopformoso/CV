from flask import render_template, request, Blueprint
import requests
import re

core = Blueprint('core', __name__)

@core.route('/')
def index():
    url = 'https://api.github.com/users/albertopformoso/starred'
    response = requests.get(url)
    response = response.json()

    repos = []
    for i in range(len(response)):
        # Getting only the date
        created_at = re.findall(
            r'^\d+-\d+-\d+',
            str(response[i].get('created_at'))
        )[0]

        repos.append({
            'name': response[i].get('name'),
            'html_url': response[i].get('html_url'),
            'description': response[i].get('description'),
            'created_at': created_at,
            'homepage': response[i].get('homepage'),
            'language': response[i].get('language')
        })

    return render_template('index.html', repos=repos)