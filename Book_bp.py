
from flask import Blueprint
from controllers.BookController import get_books, get_book, update_book, patch_book, delete_book

book_bp = Blueprint('Book_bp', __name___)

book_bp.route('/api/books', methods=['GET']) (get_books)

book_bp.route('/api/books/<int:book_id>', methods=['GET'])(get_book)

book_bp.route('/api/books/<int:book_id>', methods=['PATCH'])(update_book)

book_bp.route('/api/books/<int:book_id>', methods=['PUT'])(patch_book)

book_bp.route('/api/books/<int:book_id>', methods=['DELETE']) (delete_book)