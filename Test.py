import datetime
import threading
import time

threads = ["url1", "url2", "url3", "url4", "url5"]

variables_g = 0

filename = 'test.txt'

check_lock = threading.Lock()

def my_function():
    # global variables_g with check_lock:
    print('Starting -', datetime.datetime.now())
    global variables_g
    time.sleep(2)
    variables_g += 1
    print('Total number of download till now - ', variables_g)
    print('Ending -', datetime.datetime.now())


thread1 = threading.Thread(target=my_function(), name='one')
thread2 = threading.Thread(target=my_function(), name='two')
thread3 = threading.Thread(target=my_function(), name='three')
thread4 = threading.Thread(target=my_function(), name='four')
thread5 = threading.Thread(target=my_function(), name='five')

thread1.start()
thread2.start()
thread3.start()


thread1.join()
thread2.join()
thread3.join()


