import spidev


class MCP3208():
    def __init__(self, bus=0, device=0, vref=3.3):
        self.spi = spidev.SpiDev()  # spi初期化
        self.bus = bus
        self.device = device
        self.vref = vref

    def __read(self, ch):
        self.spi.max_speed_hz = 1000000
        v = self.spi.xfer2([4 | 2 | (ch >> 2), (ch & 0x03) << 6, 0])
        value = ((v[1] & 0x0f) << 8) | v[2]
        return value

    def raw(self, ch):
        self.spi.open(self.bus, self.device)    # デバイス使用開始
        value = self.__read(ch)                 # デバイスから値を取得
        self.spi.close()                        # デバイス使用終了
        return value

    def get(self, ch):
        self.spi.open(self.bus, self.device)    # デバイス使用開始
        value = self.__read(ch)                 # デバイスから値を取得
        result = (value * self.vref / 4096.0)
        self.spi.close()                        # デバイス使用終了
        return result
