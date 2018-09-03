import asyncio
import requests
import sys
import time

WEBHOOK_URL = sys.argv[1]
NO_OF_REQUESTS = 3


async def get_async_http_response(res_no):
    """
    Coroutine used to get HTTP response and print 'Date'
    :param res_no: Response number
    """
    print("Getting date for response # {}".format(res_no+1))
    await asyncio.sleep(1)
    response = requests.get(WEBHOOK_URL)
    print("Date for response #{} :  {}".
          format(res_no+1, response.headers['Date']))


def complete_async_tasks():
    """
    Creates and waits for 'get HTTP response' tasks to
    get completed in an async way
    """
    start_time = time.time()

    # To create 'Get HTTP response tasks from
    # get_async_http_response coroutine'

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(get_async_http_response(res_no))
             for res_no in range(NO_OF_REQUESTS)]

    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

    print("Time required to complete {} HTTP requests "
          "in an async way is: {:.2f} "
          "seconds".format(NO_OF_REQUESTS,
                           time.time() - start_time))


if __name__ == '__main__':
    complete_async_tasks()
