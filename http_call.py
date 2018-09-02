import requests
import sys
import time

WEBHOOK_URL = sys.argv[1]
NO_OF_REQUESTS = 3


def make_http_request(url, req_no):
    """
    Makes HTTP request and prints date for its response
    :param url:
    :param req_no:
    """
    response = requests.get(url)
    print("Getting date for response #"
          " {}".format(req_no + 1))
    print("Date for response #{}:   {}".format(
        req_no + 1,
        response.headers['Date']))
    time.sleep(1)


def complete_sync_tasks():
    """
    Complete 'make HTTP requests' in a sync way
    """
    start_time = time.time()

    [make_http_request(WEBHOOK_URL, res_no) for res_no
     in range(NO_OF_REQUESTS)]

    print("Time required to complete {} HTTP requests "
          "in a sync way is: {:.2f} "
          "seconds".format(NO_OF_REQUESTS,
                           time.time() - start_time))


if __name__ == '__main__':
    complete_sync_tasks()





