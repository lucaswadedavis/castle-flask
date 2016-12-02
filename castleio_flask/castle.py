import json
import requests

class Castle(object):

    def __init__(self, request, api_secret=None, api_url='https://api.castle.io/v1/'):
        self.headers = self.set_headers(request)
        self.api_secret = api_secret
        self.api_url = api_url
        self.timeout = 3000

    def set_headers(self, request):
        return {
            'X-Castle-Ip': request.remote_addr,
            'X-Castle-Cookie-Id': request.cookies.get('__cid'),
            'X-Castle-Headers': json.dumps({
                'Accept': request.headers.get('ACCEPT'),
                'Accept-Encoding': request.headers.get('ACCEPT_ENCODING'),
                'Accept-Language': request.headers.get('ACCEPT_LANGUAGE'),
                'User-Agent': request.headers.get('USER_AGENT'),
            })
        }

    def track(self, name='', user_id='', details={}):
        url = '%s/events' % (self.api_url)
        data = {'name': name, 'user_id': str(user_id), 'details': details}
        requests.post(url=url, data=data, headers=self.headers, auth=('', self.api_secret), timeout=self.timeout)
