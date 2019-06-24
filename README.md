# Programmable_LED
Python-Script um LED-Streifen zu Programmieren

Basierend auf der Anleitung von:
https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/

# LED-Streifen mit Raspberry verbinden
Der Raspberry Pi wird wie folgt mit dem LED-Streifen verbunden. 

## Ground
Wird mit einem Ground-Port auf dem Pi und mit Ground am 5V-Netzteil verbunden.
## Data 
Das Datenkabel wird mit dem GPIO-Pin 18 des Raspberry Verbunden

## 5V
Die 5V Leitung wird mit dem Positiv-pol des Netzteils verbunden. 


![alt text][logo]

[logo]: https://tutorials-raspberrypi.de/wp-content/uploads/Raspberry-Pi-WS2812-Steckplatine-600x361.png "Schema"

# Installation
Bevor wir dir Raspberry Pi Bibliothek für die LEDs installieren, müssen einige Vorbereitungen getroffen werden:

Die Paketquellen werden aktualisiert:
```sh
sudo apt-get update
sudo apt-get upgrade
```

Wir installieren die benötigten Pakete (mit Y bestötigen):

```sh
sudo apt-get install gcc make build-essential python-dev git scons swig
```

Die Audioausgabe muss deaktiviert werden. Ansonsten kann es Probleme mit den LED's geben. Dazu bearbeiten wir die Datei:
```
sudo nano /etc/modprobe.d/snd-blacklist.conf
```
Hier fügen wir folgende Zeile hinzu:
```
blacklist snd_bcm2835
```
Anschließend wird die Datei durch Drücken von STRG+O gespeichert und mit STRG+X wird der Editor geschlossen.

Außerdem müssen wir die Konfigurationsdatei bearbeiten:
```
sudo nano /boot/config.txt
```
Unten befindet sich Zeilen mit folgendem Inhalt (mit STRG+W kann durchsucht werden):
```
# Enable audio (loads snd_bcm2835)
dtparam=audio=on
```
Diese untere Zeile wird mit einer Raute/Hashtag # am Zeilenanfang auskommentiert: 
``` 
# dtparam=audio=on
```


Damit alle änderungen übernommen werden, muss der Pi neugestartet werden.
``` 
sudo reboot
```
## Installation
Nun müssen einige Dinge installiert werden. 

Die Bibliothek mit Informationen Herunterladen.
```sh
git clone https://github.com/jgarff/rpi_ws281x
```
In diesem Verzeichnis sind nun einerseits einige C Dateien enthalten, welche einfach kompiliert werden können. Der Beispielcode dafür ist gut verständlich. Damit wir diese in Python verwenden können, müssen wir sie kompilieren:
```sh
cd rpi_ws281x/
sudo scons
```
Da das ganze mit Python laufen soll, wechseln wir in den Python Ordner.
```sh
cd python
```
Hier führen wir nun noch die Installation aus:
```sh
sudo python setup.py build
sudo python setup.py install
```
## Erste Tests

Im Example-Ordner sind einige Beispieldateien, womit die LED Streifen getestet werden können.

Wir verwenden zu Testzwecken die ``` strandtest.py``` Datei. In dieser werden verscheidene Farbmodis gezeigt.

Die Datei ``` strandtest.py``` muss noch angepasst werden. 

Bei ```LED_COUNT``` muss die Anzahl der LED's am streifen angegeben werden. 

Ansonsten muss nichts angepasst werden. 

```python
# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
```

Über diesen Befehl kann das Programm gestartet werden. 
```sh
sudo python examples/strandtest.py
````

# Eigene Abfolge
Nachfolgend wird erklärt was befolgt werden muss um eine eigene Abfolge zu Programmieren.

## Einzelne LED ansprechen
Als erstes müssen alle Module importiert werden.

```python
import time
import board
import neopixel
```

Danach muss die Anzahl der LED's definiert werden. Dies kann wie folgt gelöst werden. In diesem falle sind es 144 LED's.
```python
# The number of NeoPixels
num_pixels = 144
```
Zuletzt muss noch der GPIO Pin definiert werden. 

```py
# Pin the LED_Strip is connected
pixel_pin = board.D18
```
Zuletzt wird noch der Befehl ``` pixel``` definiert.

```py
pixels = neopixel.NeoPixel(pixel_pin, num_pixels)
```

Optional kann noch über ```brightness  = 255``` die Helligkeit angepasst werden.

Die Zahl kann zwischen 0 und 255 angepasst werden. 

Nun kann ein Pixel angesprochen werden. Dies ist wie folgt möglich:
```py
pixels[0] = (255, 0, 0) # Pixel1 Red
```
Somit wird der Pixel 1 Rot. 

## Beispiel
```py
# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# The number of NeoPixels
num_pixels = 144
# Pin the LED_Strip is connected
pixel_pin = board.D18

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)

# Code
brightness  = 255
pixels[0] = (255, 0, 0) #Red
time.sleep(2)
pixels[2] = (0, 255, 0) #Green

time.sleep(5)
	
pixels[2] = (0, 0, 0)
time.sleep(1)
pixels[0] = (0, 0, 0)

time.sleep(5)
```

In diesem Beispiel wird einfach der Pixle 1&3 ein und dann wieder ausgeschaltet.

Über ```time.sleep(1)``` wird eine Sekunde gewartet bis der LED angeschaltet wird. 

### Loop
Falls der ganze Script unendlich laufen soll, kann das Ganze über ein ```While True``` gelöst werden.

Das muss dann wie folgt gelöst werden:

```py
while True:

	# Code
	brightness  = 255

	pixels[0] = (255, 0, 0) # Red
	time.sleep(2)
	pixels[2] = (0, 255, 0) # Green

	time.sleep(5)

	pixels[2] = (0, 0, 0)
	time.sleep(1)
	pixels[0] = (0, 0, 0)

	time.sleep(5)
```

