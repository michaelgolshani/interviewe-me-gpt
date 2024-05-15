from flask import Blueprint, jsonify, request
import requests
from datetime import datetime
from app.utils.helpers import validate_note_data
from ..models.models import Note
from ..models.models import db


note_routes = Blueprint('/notes', __name__)


@note_routes.route('/', methods=["GET"])
def get_all_notes():
    """This will retrieve all of the notes in our database"""

    notes = Note.query.all()
    all_notes = {}

    for note in notes:
        all_notes[note.id] = note.to_dict()

    return all_notes, 200


# create a route to fetch a note by it's id
@note_routes.route('/<int:id>', methods=["GET"])
def get_note_by_id(id):
    """This will retrieve a note by their id"""

    note = Note.query.get(id)

    if note is None:
        return {"error": "Note not found"}, 404

    note_dict = note.to_dict()
    return note_dict, 200


@note_routes.route('/<date>', methods=["GET"])
def get_notes_by_date(date):
    """This will get specfic notes created on a day"""

    try:

        notes = Note.query.filter_by(date=date).all()
        if not notes:
            return {"error": "Notes not found"}, 400

        specific_notes = []
        print("We are in notes")

        for note in notes:
            specific_notes.append(note.to_dict())

        return specific_notes, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Delete an existing note from the db
# query the note, remove
# /note_id

@note_routes.route('/<int:note_id>', methods=["DELETE"])
def delete_note(note_id):
    """Delete a note by its id in the db"""
    try:
        note_to_delete = Note.query.filter_by(id=note_id).first()
        if not note_to_delete:
            return {"error": "Note not found"}, 404

        db.session.delete(note_to_delete)
        db.session.commit()

        return {"message": "We have successfully deleted the note"}, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@note_routes.route('/new', methods=["POST"])
def create_new_note():
    """This will create a new note
    """

    try:
        new_note_data = request.json

        validate_response, status_code = validate_note_data(
            new_note_data)

        if status_code != 200:
            return validate_response


        new_note = Note(
            description=new_note_data["description"],
            date=datetime.now().strftime("%Y-%m-%d"),
            time=datetime.now().strftime("%H:%M:%S"),
        )

        db.session.add(new_note)
        db.session.commit()

        return {"message": "We have added note successfully"}, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
