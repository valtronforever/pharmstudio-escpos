# coding=utf-8

from escpos import *
from formatter import Formatter
from decimal import Decimal

p = printer.File("/dev/usb/lp0")

p.charcode('WPC1251')

p.set(align='CENTER', font='a', type='normal', width=1, height=1)
p.image("logo.png")
p.text(u"ФОП Осипенко М.А.\n".encode('cp1251'))
p.set(align='left', font='a', type='normal', width=1, height=1)
p.text(u"Адреса: смт. Каланчак,\n".encode('cp1251'))
p.text(u"        вул. Херсонська 17\n".encode('cp1251'))
p.text(u"Телефон: 0956696783\n".encode('cp1251'))

p.set(align='center', font='a', type='normal', width=1, height=1)
p.text(u"Чек №12352\n".encode('cp1251'))

p.set(align='left', font='a', type='normal', width=1, height=1)
p.text(''.ljust(32, '-') + u"\n".encode('cp1251'))
f = Formatter(p)
f.product(u"Соска Латексная 900, анатомическая, мини", 1, Decimal('17.00'))
f.product(u"Лейкопластир медичний в рулонах Medrull “Transparent”, розмiр 2, 5 см х 500 см.", 3, Decimal('40.00'))
f.product(u"Мелоксан табл. 15 мг №20", 1, Decimal('175.71'))

p.set(align='right', font='a', type='b', width=2, height=2)
p.text(u"Сума: 312.71\n".encode('cp1251'))
p.set(align='center', font='a', type='normal', width=1, height=1)
p.text(u"Дякуємо за покупку!\n".encode('cp1251'))
p.set(align='center', font='a', type='b', width=1, height=1)
p.text(u"\nДолучайся до дисконтної програми\n".encode('cp1251'))
p.set(align='center', font='a', type='normal', width=2, height=1)
p.text(u"Знижки до 5%\n".encode('cp1251'))
p.text(u"\n\n\n".encode('cp1251'))

