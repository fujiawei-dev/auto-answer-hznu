from itertools import islice
from time import sleep

from ulits import fetch_que_ans, preprocess, screenshot, tap_option, tap_next

num = 0
for i in islice(fetch_que_ans(), num, None):
    screenshot()
    positions = preprocess()
    for j in i:
        tap_option(positions[j])
        sleep(0.5)
    num += 1
    print(num)
    if num > 60:
        tap_next()
    sleep(1)