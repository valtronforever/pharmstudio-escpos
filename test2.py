# coding=utf-8

from escpos import *
from markup import Markup


p = printer.File("/dev/usb/lp0")
p.charcode('WPC1251')
p.set(align='CENTER', font='a', type='normal', width=1, height=1)
p.image("logo.png")

m = Markup(p)
with open('test.txt', 'r') as textfile:
    text = textfile.read().decode('utf8')
m.read_text(text)
