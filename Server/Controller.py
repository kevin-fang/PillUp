from models import *
from SignalPy import *

one_signal = OneSignal(app_id=None, api_key=None)


def process_medicine(patient):

    for medicine in patient.medicine:
        if medicine.can_dispense() and medicine.should_dispense():
            patient.dispense(medicine)
            medicine.dispensed()
            patient.save()
        if not medicine.can_dispense():
            patient.request_refill(medicine)
            patient.save()


def load_and_dispense():

    for patient in Patient.objects:
        process_medicine(patient)


@NC.notify_on('refill')
def refill_broadcast(user, medicine):

    content = f'Please make sure to refill cartridge #{medicine.cartridge} as soon as you can'
    notification = Notification().add_content('en', content)
    notification.add_heading('en', f'You are out of {name}')

    target = TargetDevice().include_player_ids(user.notification_tokens)
    notification.set_target_device(target)

    one_signal.post(notification)