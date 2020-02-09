# from werkzeug.routing import BaseConverter
# from models import Board
# from database import db_session
# from flask import Flask, url_for
#
# class BoardView(BaseConverter):
#     def to_python(self, value):
#         record = db_session.query(Board).filter(Board.id == value).first()
#         return record
#     def to_url(self, record):
#         return record.id
#
# app = Flask(__name__)
# app.url_map.converters['board'] = BoardView
#
# @app.route("/board/<board:record>", endpoint="view")
# def board_view_route(record):
#     return url_for("view", record=record)
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0")