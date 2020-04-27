import requests

resp = requests.get('https://xkcd.com/353/')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
else:
    print(resp.status_code)
