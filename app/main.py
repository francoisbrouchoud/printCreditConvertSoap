from spyne import Application, rpc, ServiceBase, \
    Decimal, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from decimal import Decimal as D

class ConverterService(ServiceBase):
    @rpc(Unicode, Decimal, _returns=(Unicode, Integer))
    def convert(ctx, username, chf):
        quota = int(D(chf) / D('0.08'))
        return username, quota

application = Application([ConverterService],
    tns='http://BiztalkProject.WebserviceConversion',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8000, wsgi_application)
    print("SOAP server listening on http://127.0.0.1:8000...")
    server.serve_forever()
