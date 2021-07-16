from flask import Flask, request, jsonify
from jinja2.utils import Joiner

app = Flask(__name__)

book_list = [
    {
        'id':0,
        "author":'chinua achebe',
        "language":"things fall apart",
        "title":"English"
    },
    {
        'id':1,
        "author":'Hans christain',
        "language":"danis",
        "title":"Fairy tale"
    }
]

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(book_list)>0:
            return jsonify(book_list)
        else:
             return "Not found", 404

    if request.method == 'POST':
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form['title']
        id = book_list[-1]['id']+1

        new_obj = {
        'id':id,
        "author":new_author,
        "language":new_lang,
        "title":new_title    }
        
        book_list.append(new_obj)

        return jsonify(book_list), 201

@app.route("/book/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == "GET":
        for book in book_list:
            if book['id']==id:
                return jsonify(book), 200
            pass
    
    if request.method == "PUT":
        for book in book_list:
            if book["id"]== id:
                new_author = request.form["author"]
                new_lang = request.form["language"]
                new_title = request.form['title']

                book = {
                'id':id,
                "author":new_author,
                "language":new_lang,
                "title":new_title    }
            
                return jsonify(book)

    if request.method == "DELETE":
        for index, book in enumerate(book_list):
            if book["id"]==id:
                book_list.pop(index)
                return jsonify(book_list)



                
            




if __name__ == "__main__":
    app.run(debug=True)