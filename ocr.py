#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/2/22 10:37 下午
# @Author  : Gy
# @Email   : yuanyuan775097261@qq.com
# @File    : ocr.py
# @Software: PyCharm

import sys
from time import sleep
import easygui as g
import pytesseract
from PIL import Image, ImageGrab
import torchvision.transforms as transforms
import pyautogui
import playsound


def play_map3():
    playsound.playsound('waoooo.mp3')


def orc_core(on, tw, thr, times):
    """
    识别核心逻辑
    :param times: 运行次数
    :param on: 第一段名字
    :param tw: 第二段名字
    :param thr: 第三段名字
    """
    td_name = []
    img = ImageGrab.grab(bbox=(1160, 320, 1425, 352))
    # img = Image.open('3.png').crop((1160, 320, 1425, 352))
    image_transforms = transforms.Compose([transforms.Grayscale(1)])
    image = image_transforms(img)
    text = pytesseract.image_to_string(image)
    text = text.replace("\n", "") \
        .replace("\f", "") \
        .replace("\t", "") \
        .replace("\r", "").strip()
    td_name = text.split(' ')
    if len(td_name) < 3:
        return -1
    print('运行了%d次， 识别为%s' % (times, str(td_name)))
    if on == '':
        if thr == '':
            if tw == td_name[1]:
                play_map3()
                return 1
        elif tw == '':
            if thr == td_name[2]:
                play_map3()
                return 1
        elif tw == '' and thr == '':
            return 1
        else:
            if tw == td_name[1] and thr == td_name[2]:
                play_map3()
                return 1
    elif tw == '':
        if on == '':
            if thr == td_name[2]:
                play_map3()
                return 1
        elif thr == '':
            if on == td_name[0]:
                play_map3()
                return 1
        elif on == '' and thr == '':
            return 1
        else:
            if tw == td_name[0] and thr == td_name[2]:
                play_map3()
                return 1
    elif thr == '':
        if on == '':
            if tw == td_name[1]:
                play_map3()
                return 1
        elif tw == '':
            if on == td_name[0]:
                play_map3()
                return 1
        elif on == '' and tw == '':
            return 1
        else:
            if on == td_name[0] and tw == td_name[1]:
                play_map3()
                return 1
    else:
        if on == td_name[0] and tw == td_name[1] and thr == td_name[2]:
            play_map3()
            return 1
    return 2


def setUI():
    msg = "方框里写，别瞎写，写错了电脑死机"
    title = "Fall Guys 专用起名器"
    fieldNames = ["第一段名字", "第二段名字", "第三段名字"]
    fieldValues = []
    fieldValues = g.multenterbox(msg, title, fieldNames)
    while True:
        if fieldValues is None:
            break
        errmsg = ""
        if fieldValues[0].strip() == "" and fieldValues[1].strip() == "" and fieldValues[2].strip() == "":
            errmsg += "啥也不写，你起个几把"
        if errmsg == "":
            break
        fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
    i = 0
    while True:
        status = orc_core(fieldValues[0], fieldValues[1], fieldValues[2], i)
        i = i + 1
        if status == 0:
            continue
        elif status == 1:
            break
        elif status == -1:
            print('图错了，看不清字！【仔细看看那输出都啥几把玩意】')
            continue
        elif status == 2:
            print('一轮识别结束。')
            sleep(3)
            pyautogui.press('p')
            sleep(4)
            continue


if __name__ == '__main__':
    setUI()
