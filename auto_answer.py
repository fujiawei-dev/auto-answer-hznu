from itertools import islice
from time import sleep

from cerium import AndroidDriver

from ulits import fetch_que_ans, preprocess


driver = AndroidDriver()

num = 1   # answer from the first question or you decide.

for i in islice(fetch_que_ans(), num - 1, None):
    print(f'You are doing question {num}.')
    driver.screencap_exec()
    positions = preprocess()
    for j in i:
        driver.click(140, positions[j])
        sleep(0.5)
    if num > 60:
        driver.click(888, 1800)
    num += 1
    sleep(3)
