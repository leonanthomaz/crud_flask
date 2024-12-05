from flask import Flask, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:leonan2knet@localhost:3306/treinamento'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Medicos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))

# Listar médicos
@app.route("/medicos", methods=['GET'])
def listar_medicos():
    usuarios_objetos = Medicos.query.all()
    medicos = [{"id": medico.id, "nome": medico.nome, "email": medico.email} for medico in usuarios_objetos]
    return jsonify(medicos)

# Cadastrar médico (exemplo)
@app.route("/medicos", methods=['POST'])
def cadastrar_medico():
    data = request.get_json()
    novo_medico = Medicos(nome=data['nome'], email=data['email'])
    db.session.add(novo_medico)
    db.session.commit()
    return jsonify({"message": "Médico cadastrado com sucesso!"}), 201

# Atualizar médico (exemplo)
@app.route("/medicos/<int:id>", methods=['PUT'])
def atualizar_medico(id):
    data = request.get_json()
    medico = Medicos.query.get(id)
    if medico:
        medico.nome = data['nome']
        medico.email = data['email']
        db.session.commit()
        return jsonify({"message": "Médico atualizado com sucesso!"})
    else:
        return jsonify({"message": "Médico não encontrado!"}), 404

# Deletar médico (exemplo)
@app.route("/medicos/<int:id>", methods=['DELETE'])
def deletar_medico(id):
    medico = Medicos.query.get(id)
    if medico:
        db.session.delete(medico)
        db.session.commit()
        return jsonify({"message": "Médico deletado com sucesso!"})
    else:
        return jsonify({"message": "Médico não encontrado!"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5000)
