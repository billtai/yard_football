import requests
import json


class RequestHelper:
    HEADER_JSON = {
        'Content-type': 'application/json', 'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    HEADER_XML = {'Content-type': 'text/xml', 'Accept': '*/*'}
    TIME_OUT = 5*60 # s
    NUM_RETRIES = 3

    @classmethod
    def get_header(self, send_headers=None, is_xml=False):
        if is_xml:
            return self.HEADER_XML if send_headers is None else {
                **self.HEADER_XML, **send_headers}
        return self.HEADER_JSON if send_headers is None else {
            **self.HEADER_JSON, **send_headers}

    @classmethod
    def post(self, base_url, payload={}, send_headers=None, is_xml=False):
        headers = self.get_header(send_headers, is_xml)

        if is_xml:
            for _ in range(self.NUM_RETRIES):
                try:
                    response = requests.post(base_url, data=payload, headers=headers, timeout=self.TIME_OUT)
                    if response is not None:
                        return response
                except:
                    pass
            return None
        
        for _ in range(self.NUM_RETRIES):
            try:
                response = requests.post(base_url, json=payload, headers=headers, timeout=self.TIME_OUT)
                if response is not None:
                    return response
            except:
                pass
        return None

    @classmethod
    def get(self, base_url, payload={}, send_headers=None, is_xml=False):
        headers = headers = self.get_header(send_headers, is_xml)
        if not bool(payload):
            return requests.get(base_url, headers=headers, timeout=self.TIME_OUT)
        return requests.get(base_url, params=payload, headers=headers, timeout=self.TIME_OUT)

    @classmethod
    def put(self, base_url, payload={}, send_headers=None, is_xml=False):
        headers = self.get_header(send_headers, is_xml)
        if is_xml:
            return requests.put(base_url, data=payload, headers=headers, timeout=self.TIME_OUT)
        return requests.put(base_url, json=payload, headers=headers, timeout=self.TIME_OUT)
