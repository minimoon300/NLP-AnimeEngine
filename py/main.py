import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify
from flask_cors import CORS
import math

from collections import Counter
import sys

cred = credentials.Certificate("hallowed-welder-297014-042131c68dd6.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


app = Flask(__name__)
CORS(app)

stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all",
                      "almost", "alone", "along", "already", "also", "although", "always", "am", "among", "amongst",
                      "amoungst", "amount", "an", "and", "another", "any", "anyhow", "anyone", "anything", "anyway",
                      "anywhere", "are", "around", "as", "at", "back", "be", "became", "because", "become", "becomes",
                      "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides",
                      "between", "beyond", "bill", "both", "bottom", "but", "by", "call", "can", "cannot", "cant", "co",
                      "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due",
                      "during", "each", "eg", "eight", "either", "eleven", "else", "elsewhere", "empty", "enough",
                      "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few",
                      "fifteen", "fifty", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty",
                      "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt",
                      "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers",
                      "herself", "him", "himself", "his", "how", "however", "hundred", "i", "if", "in", "inc",
                      "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly",
                      "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more",
                      "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither",
                      "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing",
                      "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other",
                      "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own", "part", "per", "perhaps",
                      "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious",
                      "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some",
                      "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such",
                      "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence",
                      "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick",
                      "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus",
                      "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under",
                      "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever",
                      "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon",
                      "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose",
                      "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself",
                      "yourselves", "the", "it's", "can't", "i'm"]

@app.route('/')
def index():
     return "AnimEngine root"


@app.route("/animeinfo", methods=["GET"])
def animeinfo():
    doc_ref = db.collection(u'animengineDB').document(request.args.get("id"))
    doc = doc_ref.get()

    if doc.exists:
        return jsonify(doc.to_dict())
    else:
        return "Anime not found", 404


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
    fileID = 1
    i = 0
    resultDictList = [{
        "title" : "",
        "result" : 0
    }]
    outputTab = []
    tmpVector = [0, 0, 0]
    for anime in all_animes:
        if 'synopsis' in anime:
            if (indexModel):
                for line in anime['synopsis']:
                    for keyword in range(0, len(keywordsList)):
                        if ' ' + keywordsList[keyword].lower() + ' ' in line.lower() and verificationList[keyword] == 0:
                            keywordsParsingLists[keyword].append(fileID)
                            verificationList[keyword] = 1
                    if sum(verificationList) == len(verificationList):
                        break
                i += 1
                fileID += 1
                for i in range(0, len(verificationList)):
                    verificationList[i] = 0
                # print(verificationList)
                # print("file done")
            if (vectorSpaceModel):
                tmpString = anime['synopsis'].split(' ')
                for keyword in range(0, len(indexOfKeywordList)):
                    # index = 0
                    # modify so it get all the number of appearance in the line
                    for word in tmpString:
                        if indexOfKeywordList[keyword].lower() == word.lower():
                            tmpVector[keyword] += 1
                # print(tmpVector)
                # print(queryVector)
                # print(indexOfKeywordList)
                if (sum(tmpVector) != 0):
                    result = (tmpVector[0] * queryVector[0] + tmpVector[1] * queryVector[1] + tmpVector[2] * queryVector[2]) / (math.sqrt(math.pow(tmpVector[0], 2) + math.pow(tmpVector[1], 2) + math.pow(tmpVector[2],2)) * math.sqrt(math.pow(queryVector[0], 2) + math.pow(queryVector[1], 2) + math.pow(queryVector[2],2)))
                    if result > 0.5:
                        if 'title' in anime:
                            print(anime['title'])
                        print(result)
                        resultDictList.append({'title': anime['title'], 'result': result})
                tmpVector = [0, 0, 0]
                i += 1

    if indexModel:
        j = 0
        tmpList = keywordsParsingLists[0]
        while j < len(keywordsParsingLists):
            if (j + 1) < len(keywordsParsingLists):
                tmpList = list(set(tmpList).intersection(keywordsParsingLists[j + 1]))
            j += 1
        print(tmpList)
    print(indexOfKeywordList)
    # print(keywordsParsingLists)
    # do your stuff
    newlist = sorted(resultDictList, key=lambda d: d['result'])
    newlist.reverse()
    print(newlist)
    newAnimeList = []
    for result in newlist:
        for anime in all_animes:
            if anime['title'] == result['title']:
                newAnimeList.append(anime.copy())
                break
    print(newAnimeList)
    return(newAnimeList)

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
