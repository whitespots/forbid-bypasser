import requests
import os
import json
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

ports = os.environ.get('PORTS')
urls = ['https://{0}/'.format(os.environ.get('DOMAIN'))]
try:
    ports = ports.strip(' ').split(',')
    for port in ports:
        urls.append('http://{0}:{1}/'.format(os.environ.get('DOMAIN'), port))
except:
    pass
vuln_id = os.environ.get('VULN_ID')


def resp(state=False, url=urls[0]):
    if state:
        return json.dumps({"vulnerable": "True", "vuln_id": vuln_id, "description": url})
    else:
        return json.dumps({"vulnerable": "False", "vuln_id": vuln_id, "description": url})


def check():
    for url in urls:
        try:
            dirty_response = requests.get(url, timeout=4, verify=False)
            if dirty_response.status_code == 403 or \
                    '403' in dirty_response.content or \
                    'forbidden' in dirty_response.content.lower():
                response = requests.get(
                    url,
                    verify=False,
                    headers={
                        'X-Forwarded-For': '127.0.0.1',
                        'X-Forwarded-Host': '127.0.0.1',
                        'X-Real-IP': '127.0.0.1',
                        'X-Client-IP': '127.0.0.1',
                        # according to https://tools.ietf.org/html/rfc7239#section-7.4
                        'Forwarded': 'for=127.0.0.1;host=127.0.0.1'
                    },
                    timeout=4
                )
                if response.status_code != 403 and \
                        '403' not in response.content and \
                        'forbidden' not in response.content.lower():
                    return resp(True, url)
        except:
            pass
    return resp(False)


if __name__ == '__main__':
    print(check())
