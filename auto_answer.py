from itertools import islice
from time import sleep

from cerium import AndroidDriver

from ulits import fetch_que_ans, preprocess


driver = AndroidDriver()

num = 1

for i in islice(fetch_que_ans(), num - 1, None):
    print(num)
    driver.pull_screencap()
    positions = preprocess()
    for j in i:
        driver.input_tap(140, positions[j])
        # sleep(0.5)
    if num > 60:
        driver.input_tap(888, 1800)
    num += 1
    sleep(0.5)
