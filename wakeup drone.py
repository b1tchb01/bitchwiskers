from djitellopy import tello
from time import sleep
michael = tello.Tello()
michael.connect()
print(michael.get_battery())
