from datetime import datetime


def validate_note_data(new_note_data):
    data = new_note_data

    print("missing field")

    required_fields = [ "date", "time"]

    # [doctorid, date, kind]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return {"error": f'You are missing the fields: {", ".join(missing_fields)}'}, 400


    return {'success': "json object is correct"}, 200
