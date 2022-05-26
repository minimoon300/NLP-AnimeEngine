import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("hallowed-welder-297014-042131c68dd6.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_user_to_firestore(username, password, email):
    doc_ref = db.collection(u'AnimEngine').document()
    doc_ref.set({
        u'email': email,
        u'username': username,
        u'password': password
    })

if __name__ == '__main__':
    email = input("Enter email: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    add_user_to_firestore(username, password, email)
