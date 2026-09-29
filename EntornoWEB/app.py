from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/expedientes")
def expedientes():
    empleados = ["ana", "carlos", "marta", "luis"]
    nombres = ["Ana Lopez", "Carlos Ruiz", "Marta Diaz", "Luis Perez"]
    claves = ["dui", "antecedentes", "carnet"]
    documentos = ["DUI", "Antecedentes", "Carnet de junta"]

    matriz = [
        [True, True, True],
        [True, False, True],
        [False, False, True],
        [True, True, True],
    ]

    # La URL puede cambiar cualquier casilla: ?ana_dui=no&marta_dui=si
    for i in range(len(empleados)):
        for j in range(len(claves)):
            valor = request.args.get(empleados[i] + "_" + claves[j])
            if valor == "si":
                matriz[i][j] = True
            elif valor == "no":
                matriz[i][j] = False

    expedientes_completos = 0
    documentos_faltantes = 0
    for fila in matriz:
        completo = True
        for estado in fila:
            if not estado:
                documentos_faltantes += 1
                completo = False
        if completo:
            expedientes_completos += 1

    return render_template(
        "expedientes.html",
        documentos=documentos,
        nombres=nombres,
        matriz=matriz,
        expedientes_completos=expedientes_completos,
        documentos_faltantes=documentos_faltantes,
    )


@app.route("/instrucciones")
def instrucciones():
    claves = ["empacar", "embalar", "ajustar"]
    nombres = ["Empacar producto", "Embalar caja", "Ajustar maquina"]

    # Cada instruccion tiene 4 espacios de version (0 = espacio vacio)
    historiales = [
        [1, 2, 3, 0],
        [2, 5, 1, 3],
        [1, 4, 0, 0],
    ]

    # La URL puede cambiar cualquier version: ?empacar_v4=7
    for i in range(len(claves)):
        for j in range(len(historiales[i])):
            clave = claves[i] + "_v" + str(j + 1)
            historiales[i][j] = request.args.get(clave, historiales[i][j], type=int)

    mayor_version = 0
    for historial in historiales:
        i = 0
        while i < len(historial):
            if historial[i] > mayor_version:
                mayor_version = historial[i]
            i += 1

    return render_template(
        "instrucciones.html",
        nombres=nombres,
        historiales=historiales,
        mayor_version=mayor_version,
    )


if __name__ == "__main__":
    app.run(debug=True)
