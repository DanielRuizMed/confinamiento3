import logging
import json, sys

import azure.functions as func

# json con valores
x = '{ "Andalucia":"confinada","Murcia":"confinada","Sevilla":"confinada","Canarias":"no confinada"}'

# transformamos en json
datos = json.loads(x)

def main(req: func.HttpRequest) -> func.HttpResponse:

    ccaa = req.params.get('ccaa')

    if ccaa:
        result = datos.get(ccaa, 'No hay datos con esa comunidad o no existe')
        codigo = 200

    else:
        result = "Nos has puesto bien los atributos, ejemplo: ?ccaa=Andalucia."
        codigo = 404

    
    return func.HttpResponse(
        response,
        mimetype="application/json",
        status_code=codigo
    )
