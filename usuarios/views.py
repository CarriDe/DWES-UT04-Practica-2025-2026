from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def usuario_view(request):
    datos = {
        "nombre": "Laura",
        "apellidos": "Gómez Pérez",
        "dni": "12345678A",
        "email": "laura.gomez@example.com",
        "telefono": "654321987",
        "pagos": {
            "enero": 20,
            "febrero": 20,
            "marzo": 20,
            "abril": 0,
            "mayo": 20,
            "junio": 20,
            "julio": 20,
            "agosto": 0,
            "septiembre": 20,
            "octubre": 20,
            "noviembre": 20,
            "diciembre": 20
        }
    }

    # Generar la lista de pagos mensuales en HTML
    pagos = "<ul>"
    for mes, cantidad in datos["pagos"].items():
        pagos += f"<li><strong>{mes.capitalize()}:</strong> {cantidad}€</li>"
    pagos += "</ul>"

    html = f"""
    <html>
        <head><title>Datos de un Usuario</title></head>
        <body>
            <h1>Información personal</h1>
            <!--Para incluir datos que se encuentran en la vista, usamos llaves como se ve a continuación -->
            <h3>{datos['nombre']} {datos['apellidos']}</h3>
            <p><strong>DNI:</strong> {datos['dni']}</p>
            <p><strong>Teléfono:</strong> {datos['telefono']}</p>
            <p><strong>Email:</strong> {datos['email']}</p>

            <h1>Pagos mensuales</h1>
            {pagos}
        </body>
    </html>
    """

    return HttpResponse(html)
