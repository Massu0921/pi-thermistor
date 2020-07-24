# pi-thermistor
## Usage
```
$ sudo python3 measure.py -h
usage: measure.py [-h] [-c CHANNEL] [-vr V_REF] [-vd V_DIVISION_RESISTANCE]

optional arguments:
  -h, --help            show this help message and exit
  -c CHANNEL, --channel CHANNEL
                        A/Dコンバータのチャンネル(0～7). Default: 0
  -vr V_REF, --v-ref V_REF
                        A/Dコンバータの基準電圧の値. Default: 3.3
  -vd V_DIVISION_RESISTANCE, --v-division-resistance V_DIVISION_RESISTANCE
                        サーミスタ側の分圧抵抗の値(kΩ). Default: 4.7
```
