import requests


def get_token(sp_dc_cookie) -> dict:
    """Return a dictionary containing the required authorization header."""

    url = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"
    this_req_headers = {"cookie": f"sp_dc={sp_dc_cookie};"}
    r = requests.get(url, headers=this_req_headers)

    return {'authorization': f"Bearer {r.json()['accessToken']}"}

def get_user_id(headers: dict) -> str:
    """Return the user_id of the user with the authorization header in headers."""

    url = "https://api.spotify.com/v1/me"
    r = requests.get(url, headers=headers)
    data = r.json()

    try:
        return data['id']
    except KeyError:
        raise ValueError('Unable to find the user with given sp_dc cookie, please check you have provided the correct value.')