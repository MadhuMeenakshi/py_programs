def led_status(led1, led2, led3):
    on_leds = []
    if led1:
        on_leds.append("LED1 ON")
    if led2:
        on_leds.append("LED2 ON")
    if led3:
        on_leds.append("LED3 ON")
    return ", ".join(on_leds) if on_leds else "All LEDs off"

result = led_status(0, 1, 0)  # LED2 ON
