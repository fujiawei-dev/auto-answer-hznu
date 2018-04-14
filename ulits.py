import copy
import json
import os

from PIL import Image, ImageDraw


def fetch_que_ans(file='find-exam.json'):
    content = json.load(open(file, encoding='utf-8'))
    for que_ans in content['body']['examItems']:
        question = que_ans['questionContent']
        if que_ans['jsonData'].get('single'):
            options = filter(lambda x: x['rightAnswers'] == True,
                             que_ans['jsonData']['single']['options']).__next__()
            answer = options['optionsContent']
            option = options['sortIndex']
            print(question, answer, option, file=open(
                'que_ans.md', 'w', encoding='utf-8'), sep='\n', end='\n\n')
            yield (option, )
        if que_ans['jsonData'].get('multiple'):
            options = tuple(filter(
                lambda x: x['rightAnswers'] == True, que_ans['jsonData']['multiple']['options']))
            answer = ' | '.join(map(lambda x: x['optionsContent'], options))
            option = tuple(map(lambda x: x['sortIndex'], options))
            print(question, answer, option, file=open(
                'que_ans.md', 'w', encoding='utf-8'), sep='\n', end='\n\n')
            yield option


def preprocess(png='screenshot.png'):
    img = Image.open(png)
    img_ex = copy.deepcopy(img)
    img_copy = ImageDraw.Draw(img_ex)
    pixels = img.load()
    positions = []
    top, bottom = (650, 1800)
    while top < bottom:
        pixel = pixels[500, top]
        find = True
        if 200 < pixel[0] < 240:
            left, right = (80, 800)
            while left < right:
                if pixels[left, top] != pixel:
                    find = False
                    break
                left += 10
            if find:
                img_copy.line((0, top, 1080, top), fill=(255, 0, 0), width=3)
                positions.append(top)
                top += 10
        top += 1
    img_ex.save('screenshot_dev.png')
    x1, x2, x3, x4, x5 = positions[:5]
    return (x1+x2)/2, (x2+x3)/2, (x3+x4)/2, (x4+x5)/2


def tap_option(y):
    os.popen('adb shell input tap 140 {}'.format(y))


def tap_next():
    os.popen('adb shell input tap 888 1800')


def screenshot():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png ./screenshot.png')


if __name__ == '__main__':
    # fetch_que_ans()
    preprocess()
