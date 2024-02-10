from simple_pid import PID
from stepper import Stepper  # Replace with the actual stepper library
from machine import Pin, ADC
import time

# Define PID parameters
kp = 5.0  # Placeholder values, replace with actual PID parameters
ki = 0.1
kd = 1.05

# Define stepper motor parameters
step_pin = 18  # Replace with the actual GPIO pin for stepper motor step
dir_pin = 19   # Replace with the actual GPIO pin for stepper motor direction
en_pin = None    # Replace with the actual GPIO pin for stepper motor enable (optional)
steps_per_rev = 200  # Replace with the actual steps per revolution of your stepper motor
speed_sps = 50  # Replace with the desired speed in steps per second
current_position=0
# Create instances of PID, stepper motor, and potentiometer
print("Initializing PID...")
pid = PID(kp, ki, kd, setpoint=0)
pid.output_limits = (-360, 360)  # Adjust as needed

print("Initializing Stepper...")
stepper = Stepper(step_pin, dir_pin, en_pin, steps_per_rev, speed_sps)

pot_pin = 2  # Replace with the actual GPIO pin for the potentiometer
pot = ADC(Pin(pot_pin))
pot.atten(ADC.ATTN_11DB)  # Full range: 3.3v
stepper.overwrite_pos_deg(int (0))
# Main loop
while True:
    
    # Read potentiometer value
    setpoint = ((pot.read()/4095)*360)
    if (setpoint == 0):
        invert_dir=False
        output=0
        stepper.target_deg(360)
        time.sleep(0.1)  # Adjust the delay as needed# Print for debugging
    elif (setpoint == 360):
        invert_dir=True
        stepper.target_deg(0)
        time.sleep(0.1)  # Adjust the delay as needed# Print for debugging
    else:
        stepper.target_deg(setpoint)
        output = pid((setpoint))
        current_position = stepper.get_pos()
        time.sleep(0.1)  # Adjust the delay as needed# Print for debugging
        print("Setpoint:", setpoint, "Current Position:", current_position, "PID Output:", output)