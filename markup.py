class Markup(object):
    printer = None

    def __init__(self, printer):
        self.printer = printer

    def read_line(self, line):
        if line.strip().upper().startswith('SET'):
            params = {}
            param_list = line.upper().replace('SET', '').strip().split(',')
            for param in param_list:
                k, v = param.lower().split('=')
                if k in ['align', 'font', 'type']:
                    params[k] = v
                elif k in ['width', 'height']:
                    params[k] = int(v)
            self.printer.set(**params)
        else:
            self.printer.text((line + "\n").encode('cp1251'))

    def read_text(self, text):
        for line in text.split("\n"):
            self.read_line(line)
