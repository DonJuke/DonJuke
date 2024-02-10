from simple_pid import PID
from stepper import Stepper  # Replace with the actual stepper library
from machine import Pin, ADC
import time

# Define PID parameters
kp = 1.0  # Placeholder values, replace with actual PID parameters
ki = 0.1
kd = 0.05

# Define stepper motor parameters
step_pin = 18  # Replace with the actual GPIO pin for stepper motor step
dir_pin = 19   # Replace with the actual GPIO pin for stepper motor direction
en_pin = None    # Replace with the actual GPIO pin for stepper motor enable (optional)
steps_per_rev = 200  # Replace with the actual steps per revolution of your stepper motor
speed_sps = 50  # Replace with the desired speed in steps per second

# Create instances of PID, stepper motor, and potentiometer
print("Initializing PID...")
pid = PID(kp, ki, kd, setpoint=0)
print("Initializing Stepper...")
stepper = Stepper(step_pin, dir_pin, en_pin, steps_per_rev, speed_sps)

pot_pin = 2  # Replace with the actual GPIO pin for the potentiometer
pot = ADC(Pin(pot_pin))
pot.atten(ADC.ATTN_11DB)  # Full range: 3.3v

# Main loop
while True:
    # Read potentiometer value
    setpoint = (pot.read()/4095*360)

    # Read current position from the stepper
    current_position = stepper.get_pos()

    # Calculate PID output
    output = pid(setpoint-current_position)

    # Move the stepper motor based on the PID output
    stepper.target_deg(setpoint)

    # Add a delay to control the update rate
    time.sleep(0.1)  # Adjust the delay as needed

    # Print for debugging
    print("Setpoint:", setpoint, "Current Position:", current_position, "PID Output:", output)