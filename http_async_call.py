import requests
import threading

url = 'https://webhook.site/15796d3a-0001-40ba-a75b-3adbb4ac3932'


def call_http(url, req_no):
    response = requests.get(url)
    print("Date for response #{}:   {}".format(
        req_no + 1,
        response.headers['Date']))


if __name__ == '__main__':
    request_arr = []
    for req_no in range(10):
        request = threading.Thread(target=call_http,
                                   args=(url, req_no))
        request_arr.append(request)
        request.start()