import requests
from requests.exceptions import HTTPError
import json

def raise_detailed_error(request_object):
    try:
        request_object.raise_for_status()
    except HTTPError as e:
        raise HTTPError(e, request_object.text)

class FirebaseAuthWrapper():
    apikey = ""

    def get_account_info(uid):
        url = 'https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=' + apikey
        body = {'idToken': uid}

        request_object = requests.post(url, data = body)
        raise_detailed_error(request_object)
        return request_object.json()

    def sign_in_with_email_and_password(email, password):
        url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=' + apikey
        body = {'email': email, 'password': password, 'returnSecureToken': True}

        request_object = requests.post(url, data = body)
        raise_detailed_error(request_object)
        return request_object.json()

    def create_user_with_email_and_password(email, password):
        url = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=' + apikey
        body = {'email': email, 'password': password, 'returnSecureToken': True}

        request_object = requests.post(url, data = body)
        raise_detailed_error(request_object)
        return request_object.json()
