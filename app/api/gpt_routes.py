from flask import Blueprint, jsonify
from openai import OpenAI  # type: ignore
import os
from ..models.models import db
from ..models.models import Note
from datetime import datetime


gpt_routes = Blueprint('/gpt', __name__)


client = OpenAI()


# fetch to open ai api and send them a request with a message, save the response in your db
@gpt_routes.route('/')
def gpt_hello(data):
    """fetch to open ai api and send them a request with a message, save the response in your db"""

    ##  ask for what type of software engineering role, along with what type of tech stack they want to use.
    ## give one good question that they could work on
    ## ask for niche. healthcare, AI, hvac, construction, cars, etc
    ## as for beginner, medium, or hard
    ## backend, frontend
    ## if backend, what type of backend questions. leetcode? Practicle? fetch a database? Random?
    ## if frontend, what type of frontend questions. leetcode? Practicle? fetch a database and show on the ui? random?

    tech_stack = [""]
    niche = data["niche"]


    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a software engineer manager interviewing a potential employee for a software engineering role. You work at a software company. You have a 1 hour interview with the interviewee. The interviewee has been told to create a folder structure with their programming language and that the interview will be focused on the full stack"},
                {"role": "user", "content": "Create a code practice focused on backend that should take the interviewee about 45 minutes to do."}
            ]
        )

        print(completion.choices[0].message.content)
        response = completion.choices[0].message.content

        cleaned_up_response = response.replace('\n', ' ')

        return {"Response": f'{cleaned_up_response}'}, 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500



# give a summary back with that AI analyzing the response
# save the summary to the ai_summary in the notes

@gpt_routes.route('/notes/<int:note_id>/summarize', methods=["GET"])
def summarize_doctor_notes(note_id):
    """This will summarize a chosen note in the database with GPT 4o"""

    # check to see if the note is in the database

    try:
        # query the note 
        note_from_db = Note.query.get(note_id)

        if note_from_db is None:
            return {"error": "This note is not in the database"}, 400

        # check if note is already summarized with ai
        if note_from_db.ai_summary:
            # print('length of ai summary', len(note_from_db.ai_summary))
            return {"error": "This note is already summarized with AI"}, 400

        # convert note to workable dict
        note = note_from_db.to_dict()

        # get the current date
        current_date = datetime.now().strftime('%Y-%m-%d')

        # get the current time
        current_time = datetime.now().strftime('%H:%M')

        # Construct the prompt with bullet points
        system_message_content = (
            'You are a software engineer manager named {doctor_name}. We need to summarize some notes. '
            'We will supply you with some info on what occurred in the note. '
            'Please give us a detailed response about the note '
            'Please give a response in a proper format with the following details:\n'
            'Interviewr Name: {doctor_name}\n'
            'Interviewee Name: {interviewee_name}\n'
            'Date: {current_date}\n'
            'Time: {current_time}\n'
            'Description: {description}\n'
        ).format(
            doctor_name= "Sensei",
            interviewee_name= "Padawan",
            description=note['description'],  # Placeholder for note content
            current_date=current_date,
            current_time=current_time
        )

        # send the note to the gpt ai
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message_content},
                {"role": "user", "content": f'{note["description"]}'}
            ]
        )

        # print and fine tune the response
        print(completion.choices[0].message.content)
        ai_summary = completion.choices[0].message.content

        # update the note from db to database
        note_from_db.ai_summary = ai_summary
        db.session.commit()

        return {"AI summary": f'{ai_summary}'}, 200

    except Exception as e:
        return jsonify({"error": str(e)})
