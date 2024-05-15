from ..models.models import db
from ..models.models import Note


def seed_note_data():
    notes_list = [
        {
            "doctor_id": 1,
            "patient_id": 1,
            "description": "Patient had a slight bruise on the left hip, took 1 mg of benadryl to calm down and will take rest for the rest of the day",
            'date': "2024-05-09",
            'time': "19:23:00"
        },
        {
            "doctor_id": 2,
            "patient_id": 1,
            "description": "Patient had a slight bruise on the left hip, took 1 mg of benadryl to calm down and will take rest for the rest of the day",
            'date': "2024-05-09",
            'time': "19:23:00"
        },
        {
            "doctor_id": 3,
            "patient_id": 2,
            "description": "Patient has been experiencing headaches, prescribed ibuprofen for relief",
            "date": "2024-05-10",
            "time": "10:00:00"
        },
        {
            "doctor_id": 4,
            "patient_id": 2,
            "description": "Patient has a history of allergies, advised to avoid triggers and carry an epinephrine auto-injector",
            "date": "2024-05-10",
            "time": "11:30:00"
        },
        {
            "doctor_id": 5,
            "patient_id": 3,
            "description": "Patient has been feeling fatigued, recommended increasing water intake and getting regular exercise",
            "date": "2024-05-11",
            "time": "09:15:00"
        },
        {
            "doctor_id": 6,
            "patient_id": 3,
            "description": "Patient has been experiencing back pain, referred for physical therapy",
            "date": "2024-05-11",
            "time": "14:45:00"
        },
        {
            "doctor_id": 7,
            "patient_id": 4,
            "description": "Patient has a family history of heart disease, advised to maintain a healthy diet and exercise regularly",
            "date": "2024-05-12",
            "time": "10:30:00"
        },
        {
            "doctor_id": 1,
            "patient_id": 4,
            "description": "Patient has been experiencing difficulty sleeping, recommended practicing good sleep hygiene and avoiding caffeine",
            "date": "2024-05-12",
            "time": "13:00:00"
        },
        {
            "doctor_id": 2,
            "patient_id": 5,
            "description": "Patient has a history of migraines, prescribed a migraine medication for relief",
            "date": "2024-05-13",
            "time": "11:00:00"
        },
        {
            "doctor_id": 3,
            "patient_id": 5,
            "description": "Patient has been experiencing stomach pain, advised to keep a food diary and avoid trigger foods",
            "date": "2024-05-13",
            "time": "14:30:00"
        },
        {
            "doctor_id": 4,
            "patient_id": 6,
            "description": "Patient has a history of asthma, prescribed an inhaler for symptom management",
            "date": "2024-05-14",
            "time": "09:45:00"
        },
        {
            "doctor_id": 5,
            "patient_id": 6,
            "description": "Patient has been experiencing joint pain, referred to a rheumatologist for further evaluation",
            "date": "2024-05-14",
            "time": "12:15:00"
        }]

    for note in notes_list:
        new_note = Note(
            doctor_id=note["doctor_id"],
            patient_id=note["patient_id"],
            description=note["description"],
            date=note["date"],
            time=note["time"]
        )
        db.session.add(new_note)

    db.session.commit()
    print('we have successfully added notes')
