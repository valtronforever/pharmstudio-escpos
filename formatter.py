from constants import SYMBOLS_PER_LINE


def split_every(n, s):
    return [s[i:i+n] for i in xrange(0, len(s), n)]


class Formatter(object):
    printer = None
    currency = ""
    count_str = "x"
    price_digits = 6
    space = 2

    def __init__(self, printer, currency=None, price_digits=None, space=None, count_str=None):
        self.printer = printer
        if currency:
            self.currency = currency
        if price_digits:
            self.price_digits = price_digits
        if space:
            self.space = space
        if count_str:
            self.count_str = count_str

    def get_title_length(self, count):
        right_offset = self.price_digits + len(self.currency)
        count_length = len(str(count)) + len(self.count_str) + 1
        if count_length > right_offset:
            right_offset = count_length

        return SYMBOLS_PER_LINE - self.space - right_offset

    def product(self, title, count, price):
        title_length = self.get_title_length(count)
        title_offset = SYMBOLS_PER_LINE - title_length
        title_lines = split_every(title_length, title)
        if len(title_lines) < 2:
            title_lines.append('')

        for index, line in enumerate(title_lines, start=1):
            if index == 1:
                text = line.lstrip(' ').ljust(title_length, ' ') + \
                       ((' '*self.space) + str(count) + self.count_str).rjust(title_offset) + "\n"
            elif index == 2:
                text = line.lstrip(' ').ljust(title_length, ' ') + \
                       ((' '*self.space) + str(price) + self.currency).rjust(title_offset) + "\n"
            else:
                text = line.lstrip(' ') + "\n"
            self.printer.text(text.encode('cp1251'))
        self.printer.text(str(''.ljust(32, '-') + "\n").encode('cp1251'))
