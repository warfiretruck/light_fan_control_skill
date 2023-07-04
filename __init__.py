import mycroft.audio
from mycroft import MycroftSkill, intent_file_handler
import RPi.GPIO as GPIO


class LightFanControlSkill(MycroftSkill):
    def __init__(self):
        super().__init__()

    def initialize(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)

    @intent_file_handler('turn.light.on.intent')
    def handle_turn_light_on(self, message):
        self.speak_dialog('light.on')
        GPIO.output(27, GPIO.HIGH)

    @intent_file_handler('turn.light.off.intent')
    def handle_turn_light_off(self, message):
        self.speak_dialog('light.off')
        GPIO.output(27, GPIO.LOW)

    @intent_file_handler('turn.fan.on.intent')
    def handle_turn_fan_on(self, message):
        self.speak_dialog('fan.on')
        GPIO.output(22, GPIO.HIGH)

    @intent_file_handler('turn.fan.off.intent')
    def handle_turn_fan_off(self, message):
        self.speak_dialog('fan.off')
        GPIO.output(22, GPIO.LOW)


def create_skill():
    return LightFanControlSkill()
