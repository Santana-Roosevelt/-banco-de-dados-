from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def insert_user(equipamentos, veiculos, dispositivo_seguranca):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users (equipamentos, veiculos, dispositivo_seguranca)
                 VALUES (?, ?, ?)''', (equipamentos, veiculos, dispositivo_seguranca))
    conn.commit()
    conn.close()

def list_user():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return users

def inserir_veiculo_db(modelo, placa, status):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''INSERT INTO veiculos (modelo, placa, status)
                 VALUES (?, ?, ?)''', (modelo, placa, status))
    conn.commit()
    conn.close()

def inserir_equipamentos_db(nome, tipo, status):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''INSERT INTO equipamentos (nome, tipo, status)
                 VALUES (?, ?, ?)''', (nome, tipo, status))
    conn.commit()
    conn.close()    

def inserir_dispositivo_db(tipo, localizacao, status):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''INSERT INTO dispositivo (tipo, localizacao, status)
                 VALUES (?, ?, ?)''', (tipo, localizacao, status))
    conn.commit()
    conn.close()

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    
    try:
        equipamentos = data['equipamentos']
        veiculos = data['veiculos']
        dispositivo_seguranca = data.get('dispositivo_seguranca', '')
        
        insert_user(equipamentos, veiculos, dispositivo_seguranca)
        return jsonify({"message": "User added successfully!"}), 201
    
    except KeyError as e:
        return jsonify({"error": f"Missing key: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/list_user', methods=['GET'])
def lits_user():
    try:
        users = list_user()
        users_list = []
        for row in users:
            users_list.append({
                'id': row['id'],
                'equipamentos': row['equipamentos'],
                'veiculos': row['veiculos'],
                'dispositivo_seguranca': row['dispositivo_seguranca']
            })

        return jsonify(users_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/inserir_veiculo', methods=['POST'])
def inserir_veiculo():
    data = request.get_json()
    try:
        modelo = data['modelo']
        placa = data['placa']
        status = data['status']

        inserir_veiculo_db(modelo, placa, status)
        return jsonify({"message": "Veiculo adicionado com sucesso"}), 201
    
    except KeyError as e:
        return jsonify({"error": "Missing key: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/listar_veiculos', methods=['GET'])
def listar_veiculos():  
    try:
        conn = sqlite3.connect('example.db')
        conn.row_factory = sqlite3.Row
        c = conn.cursor()
        c.execute('SELECT * FROM veiculos')
        veiculos = c.fetchall()
        conn.close()

        veiculos_list = [dict(row) for row in veiculos]

        return jsonify(veiculos_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@app.route('/inserir_equipamentos', methods=['POST'])
def inserir_equipamentos():
    data = request.get_json()
    try:
        nome = data['nome']
        tipo = data['tipo']
        status = data['status']

        inserir_equipamentos_db(nome, tipo, status)
        return jsonify({"message": "Equipamento adicionado com sucesso!"}), 201

    except KeyError as e:
        return jsonify({"error": f"Chave ausente: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/listar_equipamentos', methods=['GET'])
def listar_equipamento():
    try:
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('SELECT * FROM equipamentos')
        equipamentos = c.fetchall()
        conn.close()

        equipamentos_list = [dict(row) for row in equipamentos]
        return jsonify(equipamentos_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/inserir_dispositivo', methods=['POST'])
def inserir_dispositivo():
    data = request.get_json()
    try:
        tipo = data['tipo']
        localizacao = data['localizacao']
        status = data['status']

        inserir_dispositivo_db(tipo, localizacao, status)
        return jsonify({"message": "dispositivo adicionado com sucesso"}), 201
    
    except KeyError as e:
        return jsonify({"error": "Missing key: {str(e)}"}), 400
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/listar_dispositivo', methods=['GET'])
def listar_dispositivo():
    try:
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('SELECT * FROM equipamentos')
        equipamentos = c.fetchall()
        conn.close()

        equipamentos_list = [dict(row) for row in equipamentos]
        return jsonify(equipamentos_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
