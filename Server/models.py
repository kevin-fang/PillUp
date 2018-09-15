from mongoengine import *
from utilities import random_str
from time import time


class Medicine(EmbeddedDocument):

    name = StringField()
    description = StringField()
    side_effects = StringField()
    rx_date = FloatField()
    every = FloatField()
    cartridge = IntField()
    last_dispense = FloatField()
    count = IntField()

    @classmethod
    def init(cls, name, description, side_effects, every, cartridge, count):
        temp = cls()
        temp.name = name
        temp.description = description
        temp.side_effects = side_effects
        temp.every = every
        temp.cartridge = cartridge
        temp.last_dispense = time()
        temp.rx_date = time()
        temp.count = count
        return temp

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "side_effects": self.side_effects,
            "count": self.count,
            "every": self.every,
            "rx_date": self.rx_date,
            "last_dispense": self.last_dispense,
            "cartridge": self.cartridge
        }

    def add_pills(self, count):
        self.count += count

    def should_dispense(self):
        return time() - self.last_dispense > self.every

    def can_dispense(self):
        return self.count >= 1

    def dispensed(self):
        self.last_dispense = time()
        self.count -= 1


class MedicineStatus(EmbeddedDocument):

    user_id = StringField()
    medicine_id = StringField()
    taken_at = ListField(FloatField())

    @classmethod
    def init(cls, user_id, medicine_id):
        temp = cls()
        temp.user_id = user_id
        temp.medicine_id = medicine_id
        temp.taken_at = []
        return temp

    def to_json(self):
        return {
            "user_id": self.user_id,
            "medicine_id": self.medicine_id,
            "taken_at": self.taken_at
        }


class Doctor(Document):

    id = StringField(primary_key=True)
    first_name = StringField()
    last_name = StringField()
    medical_school = StringField()
    specialty = StringField()
    profile_pic = StringField()

    @property
    def patients(self):
        return [Patient.objects.filter(doctor_id=self.id)]

    @classmethod
    def init(cls, first_name, last_name, medical_school,
             specialty, profile_pic):
        temp = cls()
        temp.id = random_str()
        temp.first_name = first_name
        temp.last_name = last_name
        temp.medical_school = medical_school
        temp.specialty = specialty
        temp.profile_pic = profile_pic
        return temp

    def to_json(self, patients=False):
        doc = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "medical_school": self.medical_school,
            "specialty": self.specialty,
            "profile_pic": self.profile_pic
        }

        if patients:
            doc["patients"] = [x.to_json() for x in self.patients]

        return doc


class Patient(Document):

    id = StringField(primary_key=True)
    doctor_id = StringField()
    first_name = StringField()
    last_name = StringField()
    address = StringField()
    profile_pic = StringField()
    email = StringField()
    phone = StringField()

    medicine = EmbeddedDocumentListField(Medicine)
    medicine_status = EmbeddedDocumentField(MedicineStatus)

    @classmethod
    def init(cls, doctor_id, first_name, last_name, address,
             profile_pic, email, phone):
        temp = cls()
        temp.id = random_str()
        temp.doctor_id = doctor_id
        temp.first_name = first_name
        temp.last_name = last_name
        temp.address = address
        temp.profile_pic = profile_pic
        temp.email = email
        temp.phone = phone
        return temp

    @classmethod
    def query(cls, *args, **kwargs):
        return [cls.objects.filter(*args, **kwargs)]

    def to_json(self, medicine=False):
        doc = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "profile_pic": self.profile_pic,
            "email": self.email,
            "phone": self.phone
        }

        if medicine:
            doc["medicine"] = [x.to_json() for x in self.medicine]

        return doc