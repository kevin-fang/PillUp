from models import *
from SignalPy import *
from threading import Thread
from time import sleep
from OpenSSL import SSL

one_signal = OneSignal(app_id="1ea6fd61-7824-49ef-9018-96b51491a914", api_key=None)


def dispense_loop():

    while True:
        try:
            load_and_dispense()
            sleep(10)
        except:
            pass


def main_controller():

    Thread(target=dispense_loop).start()


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

    content = 'Please make sure to refill cartridge #{} as soon as you can'.format(medicine.cartridge)
    notification = Notification().add_content('en', content)
    notification.add_heading('en', 'You are out of {}'.format(medicine.name.capitalize()))

    target = TargetDevice().include_player_ids(user.notification_tokens)
    notification.set_target_device(target)

    one_signal.post(notification)