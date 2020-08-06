import math
import time
import argparse
import adc


class Thermistor():
    def __init__(self, *args, **kwargs):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument("-c", "--channel", action="store",
                                 help="A/Dコンバータのチャンネル(0～7). Default: 0", default=[0], type=int, choices=[0,1,2,3,4,5,6,7], nargs='*')
        self.parser.add_argument("-v", "--v-ref", action="store",
                                 help="A/Dコンバータの基準電圧の値. Default: 3.3", default=3.3, type=float)
        self.parser.add_argument("-r", "--v-division-resistance", action="store",
                                 help="サーミスタ側の分圧抵抗の値(kΩ). Default: 4.7", default=[4.7]*8, type=float, nargs='*')
        self.parser.add_argument("--verbose",  action='store_true', help="詳細な出力.")

    def measure(self):
        '''サーミスタの温度を測定
        '''

        self.args = self.parser.parse_args()
        vref = self.args.v_ref
        vdrs = self.args.v_division_resistance
        chs = self.args.channel
        verbose = self.args.verbose

        temps = []

        for i in range(len(chs)):
            ch = chs[i]
            vdr = vdrs[i]

            mcp = adc.MCP3208()
            vout = mcp.get(ch)

            try:
                r_ther = (vref * vdr) / vout - vdr  # サーミスタの抵抗値
                var_b = 3452.9 * math.pow(r_ther, -0.012329)  # 可変にしたB定数
                temp = var_b / math.log(r_ther * math.exp(var_b / (25+273.15)) / 10) - 273.15

                temps.append(temp)

            except ZeroDivisionError:
                temps.append("NaN")

        self.__output(chs, temps, verbose)

    def __output(self, chs, temps, verbose):
        for i in range(len(chs)):
            if verbose:
                print(f"ch{chs[i]}: {temps[i]} ℃")
            else:
                print(f"{temps[i]} ", end='')
            
        if not verbose:
            print()


if __name__ == "__main__":
    thermistor = Thermistor()
    thermistor.measure()
