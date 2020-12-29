while True:
    basic.show_icon(IconNames.HAPPY)
    pins.servo_write_pin(AnalogPin.P1, 0)
    pins.servo_write_pin(AnalogPin.P2, 0)
    pins.servo_write_pin(AnalogPin.P1, 180)
    pins.servo_write_pin(AnalogPin.P2, 180)

def on_forever():
    while True:
        basic.show_icon(IconNames.HAPPY)
        pins.servo_write_pin(AnalogPin.P1, 0)
        pins.servo_write_pin(AnalogPin.P2, 0)
        pins.servo_write_pin(AnalogPin.P1, 180)
        pins.servo_write_pin(AnalogPin.P2, 180)
basic.forever(on_forever)
