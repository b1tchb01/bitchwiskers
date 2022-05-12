from djitellopy import tello
from time import sleep

michael = tello.Tello()
michael.connect()
print(michael.get_battery())

michael.takeoff()
michael.move_up(110)
# Drone will take off to a height of 80cm then rise 110cm
michael.move_forward(500)
michael.move_forward(300)
# Drone will move forward 500cm then 300cm
sleep(.5)
# Drone will sleep for .5sec
michael.move_left(400)
# Drone will move left 400cm
michael.flip_back()
# Drone will do a back flip
michael.move_right(400)
sleep(.5)
michael.move_back(300)
michael.move_back(500)
# Drone will do all of the above in reverse
michael.land()
# Drone will land
