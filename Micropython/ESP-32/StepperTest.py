from machine import Pin, ADC
from stepper import Stepper
from simple_pid import PID
import time

# Define pin connections for the stepper motor
step_pin = 18
dir_pin = 19
en_pin = None  # Optional, set to None if not connected

# Create a Stepper instance
stepper_motor = Stepper(step_pin, dir_pin, en_pin, steps_per_rev=200, speed_sps=50)

# Define pin connection for the potentiometer
potentiometer_pin = 2  # Change to the appropriate pin on your ESP32
adc = ADC(Pin(potentiometer_pin))

# Create a PID controller
pid = PID(0.001, 0, 0, setpoint=0)

# Set sample time for PID
pid.sample_time = .001  # Update every 0.01 seconds

# Set output limits for the stepper motor
pid.output_limits = (-360, 360)  # Adjust as needed

# Set a threshold for potentiometer signal change
fuzzy_threshold = 45

# Set a deadband to reduce jittering
deadband = 15

# Set precision threshold for PID output
precision_threshold = 25

# Initialize the current angle
current_angle = 0

# Error mapping function (if needed)
def error_map(error):
    # Implement your error mapping logic here
    return error

pid.error_map = error_map

def read_potentiometer():
    # Read analog value from the potentiometer and map it to the range [0, 360]
    pot_value = (adc.read() / 4)
    return int(pot_value)

try:
    while True:
        # Read potentiometer value
        current_position = read_potentiometer()
        print("Current Position:", current_position)

        # Compute new output from the PID according to the system's current value
        control = pid(current_position)
        print("PID Output:", control)

        # Check if the change in potentiometer signal is significant and if PID output is precise enough
        if (
            abs(current_position - current_angle) > fuzzy_threshold
            and abs(current_position - current_angle) > deadband
            and abs(control) <= precision_threshold
        ):
            # Update the current angle
            current_angle = current_position

            # Set the target position for the stepper motor
            stepper_motor.target_deg(int(current_angle))
        
        # Wait for a short duration to avoid rapid changes
        time.sleep(0.01)

except KeyboardInterrupt:
    # Stop the stepper motor and clean up GPIO
    stepper_motor.stop()
    print("Stepper motor stopped.")
