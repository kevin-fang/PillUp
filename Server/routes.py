from flask import Blueprint, jsonify, request, abort
from models import *

mod = Blueprint(__name__, 'routes')


@mod.route('/patient/all', methods=['GET'])
def get_patients():
    return jsonify([x.to_json(True) for x in Patient.objects])


@mod.route('/patient/<id>', methods=['GET'])
def get_patient(id):
    return jsonify(Patient.objects.filter(id=id).first().to_json(True))


@mod.route('/doctor/all', methods=['GET'])
def get_doctors():
    return jsonify([x.to_json() for x in Doctor.objects])


@mod.route('/doctor/<id>', methods=['GET'])
def get_doctor(id):
    return jsonify(Doctor.objects.filter(id=id).first().to_json())


@mod.route('/doctor/<id>/patients', methods=['GET'])
def get_doctor_patients(id):

    doc = Doctor.objects.filter(id=id).first()
    if not doc:
        abort(404)

    patients = list(doc.patients)
    return jsonify([x.to_json() for x in patients])


@mod.route('/doctor', methods=['POST'])
def post_doctor():

    json = request.json
    first_name = json['first_name']
    last_name = json['last_name']
    medical_school = json['medical_school']
    specialty = json['specialty']
    profile_pic = json['profile_pic']

    doc = Doctor.init(first_name, last_name,
                      medical_school, specialty, profile_pic)
    doc.save()
    return jsonify(doc.to_json())


@mod.route('/patient', methods=['POST'])
def post_patient():

    json = request.json
    doctor_id = json['doctor_id']
    first_name = json['first_name']
    last_name = json['last_name']
    address = json['address']
    profile_pic = json['profile_pic']
    email = json['email']
    phone = json['phone']

    patient = Patient.init(doctor_id, first_name, last_name, address,
                           profile_pic, email, phone)
    patient.save()
    return jsonify(patient.to_json(False))


@mod.route('/patient/<id>/medicine', methods=['POST'])
def post_medicine(id):

    json = request.json
    name = json['name']
    description = json['description']
    side_effects = json['side_effects']
    every = float(json['every'])
    cartridge = int(json['cartridge'])
    count = int(json['count'])

    patient = Patient.objects.filter(id=id).first()
    medicine = Medicine.init(name, description, side_effects, every, cartridge, count)

    patient.medicine.append(medicine)
    patient.save()

    return jsonify(patient.to_json(True))


@mod.route('/patient/<id>/medicine/<medicine_id>/refill', methods=['POST'])
def refill_medicine(id, medicine_id):

    patient = Patient.objects.filter(id=id).first()
    if not patient:
        abort(404)

    for medicine in patient.medicine:
        if medicine.id == medicine_id:
            medicine.count += int(request.json['count'])
    patient.save()
    return jsonify(patient.to_json(True))


@mod.route('/patient/<id>/medicine/<medicine_id>/dispense', methods=['POST'])
def dispense_medicine(id, medicine_id):

    patient = Patient.objects.filter(id=id).first()
    if not patient:
        abort(404)

    for medicine in patient.medicine:
        if medicine.id == medicine_id:

            if medicine.can_dispense():
                patient.dispense(medicine)
                medicine.dispensed()
            else:
                patient.request_refill(medicine)
            patient.save()
            break

    patient.save()
    return jsonify(patient.to_json(True))


@mod.route('/webhook', methods=['GET', 'POST'])
def webhook():
    print(request.json)


@mod.route('/patient/<id>/notification', methods=['POST'])
def add_patient_notification(id):

    patient = Patient.objects.filter(id=id).first()
    if not patient:
        abort(404)

    patient.notification.append(request.json['player_id'])
    patient.save()

    return jsonify(ok=True)


@mod.route('/doctor/<id>/notification', methods=['POST'])
def add_doctor_notification(id):

    doctor = Doctor.objects.filter(id=id).first()
    if not doctor:
        abort(404)

    doctor.notification.append(request.json['player_id'])
    doctor.save()

    return jsonify(ok=True)

##


@mod.route('/patient/<id>/medicine', methods=['GET'])
def get_patient_medicine(id):

    patient = Patient.objects.filter(id=id).first()
    if not patient:
        abort(404)

    return jsonify([x.to_json() for x in patient.medicine])


@mod.route('/patient/<id>/medicine/<medicine_id>', methods=['DELETE'])
def delete_patient_medicine(id, medicine_id):

    patient = Patient.objects.filter(id=id).first()
    if not patient:
        abort(404)

    patient.medicine = list(filter(lambda x: x.id != medicine_id, patient.medicine))
    patient.save()

    return jsonify([x.to_json() for x in patient.medicine])


@mod.route('/patient/<id>/medicine/<medicine_id>', methods=['GET'])
def get_specific_patient_medicine(id, medicine_id):

    patient = Patient.objects.filter(id=id).first()
    if not patient:
        abort(404)

    for medicine in patient.medicine:
        if medicine.id == medicine_id:
            return jsonify(medicine.to_json())

    abort(404)


@mod.route('/patient/search', methods=['GET'])
def search_patient():

    query = request.args.get('user')
    return jsonify([x.to_json(True) for x in Patient.search(query)])


@mod.route('/patient/<id>/medicine/<medicine_id>/refill', methods=['POST'])
def req_refill_medicine(id, medicine_id):

    patient = Patient.objects.filter(id=id).first()
    if not patient:
        abort(404)

    for medicine in patient.medicine:
        if medicine.id == medicine_id:
            patient.request_refill(medicine)
            break

    patient.save()
    return jsonify(patient.to_json(True))