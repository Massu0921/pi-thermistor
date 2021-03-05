# pi-thermistor
サーミスタによる温度測定プログラム  
A/Dコンバータは12bit 8ch [MCP3208](https://akizukidenshi.com/catalog/g/gI-00238/)を使用．  
サーミスタはJT Thermistor [103JT](http://akizukidenshi.com/download/ds/semitec/jt_thermistor.pdf)を使用．  
プログラム`measure.py`内のB定数は，上記の資料より各温度区間でのB定数を算出し，得られた点から求めた近似曲線で最適化したものを設定している．  
また，次のパラメータはコマンドライン引数で変更可能である．  
- A/Dコンバータの基準電圧：3.3v
- 分圧回路の抵抗値：4.7kΩ  

## Usage
```
$ sudo python3 measure.py -h
usage: measure.py [-h] [-c [{0,1,2,3,4,5,6,7} [{0,1,2,3,4,5,6,7} ...]]]
                  [-v V_REF]
                  [-r [V_DIVISION_RESISTANCE [V_DIVISION_RESISTANCE ...]]]
                  [--verbose]

optional arguments:
  -h, --help            show this help message and exit
  -c [{0,1,2,3,4,5,6,7} [{0,1,2,3,4,5,6,7} ...]], --channel [{0,1,2,3,4,5,6,7} [{0,1,2,3,4,5,6,7} ...]]
                        A/Dコンバータのチャンネル(0～7). Default: 0
  -v V_REF, --v-ref V_REF
                        A/Dコンバータの基準電圧の値. Default: 3.3
  -r [V_DIVISION_RESISTANCE [V_DIVISION_RESISTANCE ...]], --v-division-resistance [V_DIVISION_RESISTANCE [V_DIVISION_RESISTANCE ...]]
                        サーミスタ側の分圧抵抗の値(kΩ). Default: 4.7
  --verbose             詳細な出力.
```
