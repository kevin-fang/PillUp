from flask import Blueprint, jsonify, request
from models import *

mod = Blueprint(__name__, 'routes')


@mod.route('/patient/all', methods=['GET'])
def get_patients():
    return jsonify([x.to_json() for x in Patient.objects])


@mod.route('/patient/<id>', methods=['GET'])
def get_patient(id):
    return jsonify(Patient.objects.filter(id=id).first().to_json(True))


@mod.route('/patient', methods=['POST'])
def post_patient():

    json = request.json()
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
def post_medicine():

    json = request.json()
    name = json['name']
    description = json['description']
    side_effects = json['side_effects']
    every = json['every']
    cartridge = json['cartridge']







