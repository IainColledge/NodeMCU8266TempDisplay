# NodeMCU Temp display

Displays temperature on a .91" OLED display.

Items:

* [HiLetgo New Version ESP8266 NodeMCU](https://www.amazon.co.uk/gp/product/B0791FJB62/ref=ppx_yo_dt_b_asin_title_o08__o00_s00?ie=UTF8&psc=1) Microcontroller board
* [LM35DZ/NOPB](http://www.ti.com/lit/ds/symlink/lm35.pdf) One wire temperature sensor
* [MakerHawk I2C OLED Display Module 0.91 Inch Blue](https://www.amazon.co.uk/gp/product/B076BJZ42H/ref=ppx_yo_dt_b_asin_title_o07__o00_s00?ie=UTF8&psc=1)

## Wiring

Wire up as follows:

Node MCU | LM35 | Display
:---: | :---: | :---:
Vin | +Vs | 
GND | GND | 
A0  | Vout |
3V3 |     | VCC
GND |     | GND
D1  |     | SCL
D2  |     | SDA

A wired up example is shown below.

![Wired Board](https://raw.githubusercontent.com/IainColledge/NodeMCU8266TempDisplay/master/board.jpg)

## Additional libraries and code

Requires:
* lm35.py
* esp8266/adc.py

From the [Micropython devices](https://github.com/IainColledge/uPythonDevices) repository.

If you want to display the IP then have the following in/as your boot.py file.

```python
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Your Wifi name', 'Your Wifi password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    
do_connect()
```