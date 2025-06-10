import RPi.GPIO as GPIO
import time
import serial

# ----- GPIO Setup -----
RELAY_PINS = {
    "power": 4,
    "reset": 17,
    "cooling": 27,
    "test": 22
}

GPIO.setmode(GPIO.BCM)
for pin in RELAY_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# ----- Serial Config -----
SERIAL_PORT = '/dev/ttyS0'
BAUD_RATE = 9600

# ----- Simple Helper Functions -----
def blink(pin, delay=2.5):
    GPIO.output(pin, GPIO.HIGH)
    print(f"Relay {pin} ON")
    time.sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    print(f"Relay {pin} OFF")

def send_serial_message(message):
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            ser.write(message.encode())
            print(f"📤 Sent: {message}")
    except Exception as e:
        print("⚠️ Serial error:", e)

# ----- Trigger Actions -----
def activate_power():
    blink(RELAY_PINS["power"])

def reset_server():
    blink(RELAY_PINS["reset"])

def toggle_cooling():
    blink(RELAY_PINS["cooling"])

def send_test():
    send_serial_message("Hello from Tenmei! 💻🚀")

# ----- Example Control Loop (Simulated) -----
try:
    while True:
        cmd = input("Enter command (power/reset/cooling/test/exit): ").strip().lower()
        if cmd == "power":
            activate_power()
        elif cmd == "reset":
            reset_server()
        elif cmd == "cooling":
            toggle_cooling()
        elif cmd == "test":
            send_test()
        elif cmd == "exit":
            break
        else:
            print("Unknown command.")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up.")
