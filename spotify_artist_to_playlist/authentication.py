import requests


def get_token(sp_dc_cookie) -> dict:
    """Return a dictionary containing the required authorization header."""

    url = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"
    this_req_headers = {"cookie": f"sp_dc={sp_dc_cookie};"}
    r = requests.get(url, headers=this_req_headers)

    return {'authorization': f"Bearer {r.json()['accessToken']}"}