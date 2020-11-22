import logging
import json

import azure.functions as func

# json con valores
x = '{ "Andalucia":"confinada","Murcia":"confinada","Sevilla":"confinada","Canarias":"no confinada"}'

# transformamos en json
datos = json.loads(x)

def main(req: func.HttpRequest) -> func.HttpResponse:

    ccaa = req.params.get('ccaa')

    if ccaa:
        result = datos[ccaa]
        codigo = 200

        if len(result) <= 1:
            result = "No hay datos con esa comunidad o no existe"
            codigo = 500

    else:
        result = "Nos has puesto bien los atributos, ejemplo: ?ccaa=Andalucia."
        codigo = 404


    return func.HttpResponse(
        result,
        status_code=codigo
    )
