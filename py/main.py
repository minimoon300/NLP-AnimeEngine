import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify
from flask_cors import CORS

cred = credentials.Certificate("hallowed-welder-297014-042131c68dd6.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
     return "AnimEngine root"


@app.route("/animeinfo", methods=["GET"])
def animeinfo():
    anime_id = request.args.get("id")
    all_animes_raw = db.collection(u'animengineDB').stream()
    all_animes = []

    for anime in all_animes_raw:
        all_animes.append({k: v for k, v in anime.to_dict().items() if v})

    for anime in all_animes:
        if anime["id"] == anime_id:
            return jsonify(anime)


@app.route("/login", methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]
    all_users_raw = db.collection(u'AnimEngine').stream()
    all_users = []

    for user in all_users_raw:
        all_users.append({k: v for k, v in user.to_dict().items() if v})

    for user in all_users:
        if user["email"] == email and user["password"] == password:
            return jsonify(user)

    return "User not found", 404


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
