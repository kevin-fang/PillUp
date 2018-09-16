import json

import database

from models import *


def load_patients():

    doc_id = Doctor.objects.first().id
    for item in json.loads(open('patient_data.json').read())['patients']:
        first = item['first']
        last = item['last']
        image = item['image']
        email = '{}@gmail.com'.format(random_str(10))
        phone = '3016669999'

        print(Patient.init(doc_id, first, last, "", image, email, phone).to_json())


if __name__ == '__main__':
    database.init()
    load_patients()