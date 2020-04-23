from flask import Flask, request, render_template
from flask_cors import CORS
from escpos import *
from markup import Markup

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Pharmstudio receipt print service"


@app.route("/print/", methods=['GET', 'POST'])
def receipt():
    if request.method == 'POST':
        #p = printer.Usb(0x0483, 0x070b)
        p = printer.File("/dev/usb/lp0")
        # p.charcode('WPC1251')
        p._raw('\x1c\x2e')
        p._raw('\x1b\x74\x17')
        p.set(align='CENTER', font='a', type='normal', width=1, height=1)
        p.image("logo.png")
        m = Markup(p)
        m.read_text(request.form['data'])
        return 'Ok'
    else:
        return render_template('receipt.html')

if __name__ == "__main__":
    reactor_args = {}
    
    def run_twisted_wsgi():
        from twisted.internet import reactor
        from twisted.web.server import Site
        from twisted.web.wsgi import WSGIResource

        resource = WSGIResource(reactor, reactor.getThreadPool(), app)
        site = Site(resource)
        reactor.listenTCP(8766, site)
        reactor.run(**reactor_args)
        
    if app.debug:
        # Disable twisted signal handlers in development only.
        reactor_args['installSignalHandlers'] = 0
        # Turn on auto reload.
        import werkzeug.serving
        run_twisted_wsgi = werkzeug.serving.run_with_reloader(run_twisted_wsgi)

    run_twisted_wsgi()
