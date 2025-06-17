from machine import Pin
import time

# GPIO LED IO2
def blink():
    
    led = machine.Pin(2, machine.Pin.OUT)     # Pin 2 ,Output mode
    
    while(True):			# loop
        led.on()			# light on LED
        time.sleep(1)		# delay 1s
        led.off()			# light off LED
        time.sleep(1)		# delay 1s

if __name__ == "__main__":
    blink()