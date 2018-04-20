from itertools import islice
from time import sleep

from cerium import AndroidDriver

from ulits import fetch_que_ans, preprocess


driver = AndroidDriver()

num = 0
for i in islice(fetch_que_ans(), num, None):
    driver.pull_screencap()
    positions = preprocess()
    for j in i:
        driver.input_tap(140, positions[j])
        sleep(0.5)
    num += 1
    print(num)
    if num > 60:
        driver.input_tap(888, 1800)
    sleep(3)
