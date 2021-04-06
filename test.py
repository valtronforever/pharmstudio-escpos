from escpos import *
from formatter import Formatter
from decimal import Decimal

def tp(pp, raw, code):
    pp._raw(raw)
    pp.text(str(str(code) + ' ' + "тест\n").encode('cp1251'))

#p = printer.File("/dev/usb/lp0")
p = printer.Usb(0x0416, 0x5011, out_ep=0x03)
p._raw('\x1c\x2e')
p.set(align='CENTER', font='a', type='normal', width=1, height=1)
tp(p, '\x1b\x74\x00', '00')
tp(p, '\x1b\x74\x01', '01')
tp(p, '\x1b\x74\x02', '02')
tp(p, '\x1b\x74\x03', '03')
tp(p, '\x1b\x74\x04', '04')
tp(p, '\x1b\x74\x05', '05')
tp(p, '\x1b\x74\x06', '06')
tp(p, '\x1b\x74\x07', '07')
tp(p, '\x1b\x74\x08', '08')
tp(p, '\x1b\x74\x09', '09')
tp(p, '\x1b\x74\x0a', '0a')
tp(p, '\x1b\x74\x0b', '0b')
tp(p, '\x1b\x74\x0c', '0c')
tp(p, '\x1b\x74\x0d', '0d')
tp(p, '\x1b\x74\x0e', '0e')
tp(p, '\x1b\x74\x0f', '0f')
tp(p, '\x1b\x74\x10', '10')
tp(p, '\x1b\x74\x11', '11')
tp(p, '\x1b\x74\x12', '12')
tp(p, '\x1b\x74\x13', '13')
tp(p, '\x1b\x74\x14', '14')
tp(p, '\x1b\x74\x15', '15')
tp(p, '\x1b\x74\x16', '16')
tp(p, '\x1b\x74\x17', '17')
tp(p, '\x1b\x74\x18', '18')
tp(p, '\x1b\x74\x19', '19')
tp(p, '\x1b\x74\x1a', '1a')
tp(p, '\x1b\x74\x1b', '1b')
tp(p, '\x1b\x74\x1c', '1c')
tp(p, '\x1b\x74\x1d', '1d')
tp(p, '\x1b\x74\x1e', '1e')
tp(p, '\x1b\x74\x1f', '1f')
