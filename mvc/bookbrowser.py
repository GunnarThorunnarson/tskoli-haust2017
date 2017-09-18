# coding: utf-8
# Þetta skjal þjónar tilgangi controller
# Sér um routing og að tengja Módelið við View (templates)

from flask import Flask, request, render_template
import Model

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home(search_string=''):
    search_string=request.args.get('search', '')
    books = Model.Filter_Books(search_string)
    return render_template(
        'index.html',
        books=books,
        search_string=search_string )

@app.route('/book', methods=['GET'])
def book():
    author=request.args.get('author', '')
    title=request.args.get('title', '')
    book = Model.Get_Book(author=author, title=title)
    return render_template(
        'book.html',
        book=book )
