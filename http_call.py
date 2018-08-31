import requests
import time

url = 'https://webhook.site/15796d3a-0001-40ba-a75b-3adbb4ac3932'
no_of_requests = 3


def call_http_request(url, res_no):
    response = requests.get(url)
    print("Date for response #{}:   {}".format(
        res_no + 1,
        response.headers['Date']))
    time.sleep(5)


if __name__ == '__main__':
    [call_http_request(url, res_no) for res_no in range(no_of_requests)]