from enum import Enum
import time

class Traffice_light(Enum):
    RED='STOP'
    YELLOW= 'GET READY'
    GREEN= 'GO'

running = True
# Stimulation for traffic signal
def traffic_simulator():
    while True:
        for signal in Traffice_light:
            print(f'{signal.name} - {signal.value}')
            time.sleep(3)
        print('\n Waiting for next \n')
        time.sleep(4)
traffic_simulator()