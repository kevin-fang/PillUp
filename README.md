# PillUp

API Docs:

# Get All Patients
Get all of the current patients
**URL**: `216.200.116.146`\
**Route**: `/patient/all`\
**Method** : `GET`\
**Port** : `8080`

# Get Specific Patient
Get a specific patient info using their patient id
**URL**: `216.200.116.146`\
**Route**: `/patient/<id>`\
**Method** : `GET`\
**Port** : `8080`

# Get All Doctors
Get all of the registered doctors
**URL**: `216.200.116.146`\
**Route**: `/doctor/all`\
**Method** : `GET`\
**Port** : `8080`

# Get Specific Doctor
Get a specific doctor info using their doctor id
**URL**: `216.200.116.146`\
**Route**: `/doctor/<id>`\
**Method** : `GET`\
**Port** : `8080`

# Get Specific Doctor's Patients
Get all of the patients who are registered under a doctor.
**URL**: `216.200.116.146`\
**Route**: `/doctor/<id>/patients`\
**Method** : `GET`\
**Port** : `8080`

# Register a New Doctor
Register a new doctor to the database
**URL**: `216.200.116.146`\
**Route**: `/doctor`\
**Method** : `POST`\
**Port** : `8080`

**Data constraints**:
```json
{
    "first_name": "string",
    "last_name": "string",
    "medical_school": "string",
    "speciality": "string",
    "profile_pic": "url",
}
```

# Register a New Patient
Register a new patient to the database
**URL**: `216.200.116.146`\
**Route**: `/patient`\
**Method** : `POST`\
**Port** : `8080`

**Data constraints**:
```json
{
    "first_name": "string",
    "last_name": "string",
    "doctor_id": "string",
    "address": "string",
    "email": "string",
    "phone": "string",
    "profile_pic": "url",
}
```

# Add New Medicine
Add a new medicine for a patient
**URL**: `216.200.116.146`\
**Route**: `/patient/<id>/medicine`\
**Method** : `POST`\
**Port** : `8080`

**Data constraints**:
```json
{
    "name": "string",
    "description": "string",
    "side_effects": "string",
    "every": "seconds",
    "cartridge": "int",
    "count": "int"
}
```

# Refill A Cartridge
Refill a cartridge
**URL**: `216.200.116.146`\
**Route**: `/patient/<id>/medicine/<medicine_id>/refill`\
**Method** : `POST`\
**Port** : `8080`

**Data constraints**:
```json
{
    "count": "int"
}
```

# Dispense a Pill
Dispense a specific pill
**URL**: `216.200.116.146`\
**Route**: `/patient/<id>/medicine/<medicine_id>/dispense`\
**Method** : `POST`\
**Port** : `8080`

# Add Patient Notification Id
Add Onesignal's notification id for a patient
**URL**: `216.200.116.146`\
**Route**: `/patient/<id>/notification`\
**Method** : `POST`\
**Port** : `8080`

**Data constraints**:
```json
{
    "player_id": "string"
}
```

# Add Doctor Notification Id
Add Onesignal's notification id for a doctor
**URL**: `216.200.116.146`\
**Route**: `/doctor/<id>/notification`\
**Method** : `POST`\
**Port** : `8080`

**Data constraints**:
```json
{
    "player_id": "string"
}
```
