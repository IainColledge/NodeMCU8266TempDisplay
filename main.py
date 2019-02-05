#
# Read temperature and display it
#

import utime, ssd1306
from machine import I2C, Pin
from esp8266 import lm35
import network


def main():
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    oled = ssd1306.SSD1306_I2C(128, 32, i2c)
    tmr = utime
    led = Pin(2, Pin.OUT)
    dt = 0
    ip = network.WLAN(network.STA_IF).ifconfig()[0]
    dx = 0  # Dot position on the bottom of the screen
    tc = 0  # Timer counts
    t = 0  # Temp
    at = 0  # ADC time

    while True:
        st = tmr.ticks_ms()

        if tc == 0:
            led.off()  # Reversed
            t = str("%.1f" % lm35.get_temp())
            print('Temp: ' + t + 'c Time: ' + str(dt) + 'ms')
            led.on()  # Reversed
            at = tmr.ticks_diff(tmr.ticks_ms(), st)

        tc += 1
        if tc == 19:
            tc = 0

        tmr.sleep_ms(8 - at)  # Roughly 50ms a tick

        oled.fill(0)
        oled.text('IP: ' + ip, 0, 0)
        oled.text('Temp: ' + t + 'c', 0, 10)
        oled.text('at: ' + str (at) + 'ms dt: ' + str(dt) + 'ms', 0, 20)
        oled.pixel(dx,31,1)
        oled.show()

        dx += 1
        if dx == 127:
            dx = 0

        dt = tmr.ticks_diff(tmr.ticks_ms(), st)


if __name__ == '__main__':
    main()