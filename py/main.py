import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify

cred = credentials.Certificate("hallowed-welder-297014-042131c68dd6.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


app = Flask(__name__)


@app.route('/')
def index():
     return "AnimEngine root"


@app.route('/users', methods=['POST'])
def add_user_to_firestore():
    doc_ref = db.collection(u'AnimEngine').document()
    doc_ref.set({
        u'email': request.json["email"],
        u'username': request.json["username"],
        u'password': request.json["password"]
    })
    return jsonify(doc_ref.get().to_dict())


@app.route('/animes', methods=['GET'])
def get_all_animes():
    all_animes_raw = db.collection(u'animengineDB').stream()
    all_animes = []

    for anime in all_animes_raw:
        all_animes.append({k: v for k, v in anime.to_dict().items() if v})

    return jsonify(all_animes)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
