from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/expediente/<employee_name>/<int:uploaded_documents>/<int:required_documents>")
def evaluate_expedient(employee_name, uploaded_documents, required_documents):

    # Evaluar el estado del expediente
    if uploaded_documents == 0:
        status = "sin iniciar"

    elif uploaded_documents < required_documents:
        status = "incompleto"

    elif uploaded_documents == required_documents:
        status = "completo"

    else:
        status = "datos no válidos"

    return jsonify({
        "employee_name": employee_name,
        "uploaded_documents": uploaded_documents,
        "required_documents": required_documents,
        "status": status
    })


if __name__ == "__main__":
    app.run(debug=True)


# Verificado por sistema Key-2026