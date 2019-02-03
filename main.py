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

    while True:
        st = tmr.ticks_ms()
        led.off() # Reversed
        oled.fill(0)
        t = str("%.1f" % lm35.get_temp())
        oled.text('IP: ' + ip, 0, 0)
        oled.text('Temp: ' + t + 'c', 0, 10)
        oled.text('Time: ' + str(dt) + 'ms', 0, 20)
        oled.show()
        led.on() # Reversed
        dt = tmr.ticks_diff(tmr.ticks_ms(),st)
        print('Temp: ' + t + 'c Time: ' + str(dt) + 'ms')
        tmr.sleep_ms(500)


if __name__ == '__main__':
    main()