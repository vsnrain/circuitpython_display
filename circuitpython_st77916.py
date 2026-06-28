from busdisplay import BusDisplay

# Command Table 1
CMD_NOP         = 0x00
CMD_SWRESET     = 0x01
CMD_RDDID       = 0x04
CMD_RDDST       = 0x09

CMD_SLPIN       = 0x10
CMD_SLPOUT      = 0x11
CMD_PTLON       = 0x12
CMD_NORON       = 0x13
CMD_INVOFF      = 0x20
CMD_INVON       = 0x21
CMD_GAMMASET    = 0x26
CMD_DISPOFF     = 0x28
CMD_DISPON      = 0x29
CMD_CASET       = 0x2A
CMD_RASET       = 0x2B
CMD_PASET       = 0x2B
CMD_RAMWR       = 0x2C
CMD_RAMRD       = 0x2E
CMD_MADCTL      = 0x36
CMD_IDMOFF      = 0x38
CMD_IDMON       = 0x39
CMD_TEON        = 0x35
CMD_COLMOD      = 0x3A
CMD_GETSCANLINE = 0x45

# Command Table 2
CMD_RESSET1     = 0xD0
CMD_RESSET2     = 0xD1
CMD_RESSET3     = 0xD2

CMD_GAMCTRP1    = 0xE0
CMD_GAMCTRN1    = 0xE1

CMD_CSC1        = 0xF0
CMD_CSC2        = 0xF1
CMD_CSC3        = 0xF2
CMD_CSC4        = 0xF3

def cmd_param(cmd, param=b'', delay=None):
    if delay != None:
        return bytes([cmd, len(param) | 0x80]) + param + bytes([delay])
    return bytes([cmd, len(param)]) + param

class ST77916(BusDisplay):
    _INIT_SEQUENCE = b''.join([
        cmd_param(CMD_CSC1,     b'\x01'),  # CSC1: CMD2_EN
        cmd_param(CMD_CSC2,     b'\x01'),  # CSC2: CMD2_PROT1

        b'\xB0\x01\x69',
        b'\xB1\x01\x4A',
        b'\xB2\x01\x2F',
        b'\xB3\x01\x01',
        b'\xB4\x01\x69',
        b'\xB5\x01\x45',
        b'\xB6\x01\xAB',
        b'\xB7\x01\x41',
        b'\xB8\x01\x86',
        b'\xB9\x01\x15',
        b'\xBA\x01\x00',
        b'\xBB\x01\x08',
        b'\xBC\x01\x08',
        b'\xBD\x01\x00',
        b'\xBE\x01\x00',
        b'\xBF\x01\x07',

        b'\xC0\x01\x80',
        b'\xC1\x01\x10',
        b'\xC2\x01\x37',
        b'\xC3\x01\x80',
        b'\xC4\x01\x10',
        b'\xC5\x01\x37',
        b'\xC6\x01\xA9',
        b'\xC7\x01\x41',
        b'\xC8\x01\x01',
        b'\xC9\x01\xA9',
        b'\xCA\x01\x41',
        b'\xCB\x01\x01',
        b'\xCC\x01\x7F',
        b'\xCD\x01\x7F',
        b'\xCE\x01\xFF',

        b'\xD0\x01\x91',
        b'\xD1\x01\x68',
        b'\xD2\x01\x68',

        b'\xF5\x02\x00\xA5',

        cmd_param(CMD_CSC2,     b'\x02'),  # CSC2: CMD2_xPROT2
        cmd_param(CMD_CSC1,     b'\x00'),  # CSC1: disable

        cmd_param(CMD_CSC1,     b'\x02'),  # CSC1: GAM_EN
        cmd_param(CMD_GAMCTRP1, b'\xF0\x10\x18\x0D\x0C\x38\x3E\x44\x51\x39\x15\x15\x30\x34'),
        cmd_param(CMD_GAMCTRN1, b'\xF0\x0F\x17\x0D\x0B\x07\x3E\x33\x51\x39\x15\x15\x30\x34'),

        cmd_param(CMD_CSC1,     b'\x10'), # CSC1: GIP_EN
        cmd_param(CMD_CSC4,     b'\x10'), # CSC4: GIP_PROT2

        b'\xE0\x01\x08',
        b'\xE1\x01\x00',
        b'\xE2\x01\x00',
        b'\xE3\x01\x00',
        b'\xE4\x01\xE0',
        b'\xE5\x01\x06',
        b'\xE6\x01\x21',
        b'\xE7\x01\x03',
        b'\xE8\x01\x05',
        b'\xE9\x01\x02',
        b'\xEA\x01\xE9',
        b'\xEB\x01\x00',
        b'\xEC\x01\x00',
        b'\xED\x01\x14',
        b'\xEE\x01\xFF',
        b'\xEF\x01\x00',

        b'\xF8\x01\xFF',
        b'\xF9\x01\x00',
        b'\xFA\x01\x00',
        b'\xFB\x01\x30',
        b'\xFC\x01\x00',
        b'\xFD\x01\x00',
        b'\xFE\x01\x00',
        b'\xFF\x01\x00',

        b'\x60\x01\x40',
        b'\x61\x01\x05',
        b'\x62\x01\x00',
        b'\x63\x01\x42',
        b'\x64\x01\xDA',
        b'\x65\x01\x00',
        b'\x66\x01\x00',
        b'\x67\x01\x00',
        b'\x68\x01\x00',
        b'\x69\x01\x00',
        b'\x6A\x01\x00',
        b'\x6B\x01\x00',

        b'\x70\x01\x40',
        b'\x71\x01\x04',
        b'\x72\x01\x00',
        b'\x73\x01\x42',
        b'\x74\x01\xD9',
        b'\x75\x01\x00',
        b'\x76\x01\x00',
        b'\x77\x01\x00',
        b'\x78\x01\x00',
        b'\x79\x01\x00',
        b'\x7A\x01\x00',
        b'\x7B\x01\x00',

        b'\x80\x01\x48',
        b'\x81\x01\x00',
        b'\x82\x01\x07',
        b'\x83\x01\x02',
        b'\x84\x01\xD7',
        b'\x85\x01\x04',
        b'\x86\x01\x00',
        b'\x87\x01\x00',
        b'\x88\x01\x48',
        b'\x89\x01\x00',
        b'\x8A\x01\x09',
        b'\x8B\x01\x02',
        b'\x8C\x01\xD9',
        b'\x8D\x01\x04',
        b'\x8E\x01\x00',
        b'\x8F\x01\x00',

        b'\x90\x01\x48',
        b'\x91\x01\x00',
        b'\x92\x01\x0B',
        b'\x93\x01\x02',
        b'\x94\x01\xDB',
        b'\x95\x01\x04',
        b'\x96\x01\x00',
        b'\x97\x01\x00',
        b'\x98\x01\x48',
        b'\x99\x01\x00',
        b'\x9A\x01\x0D',
        b'\x9B\x01\x02',
        b'\x9C\x01\xDD',
        b'\x9D\x01\x04',
        b'\x9E\x01\x00',
        b'\x9F\x01\x00',

        b'\xA0\x01\x48',
        b'\xA1\x01\x00',
        b'\xA2\x01\x06',
        b'\xA3\x01\x02',
        b'\xA4\x01\xD6',
        b'\xA5\x01\x04',
        b'\xA6\x01\x00',
        b'\xA7\x01\x00',
        b'\xA8\x01\x48',
        b'\xA9\x01\x00',
        b'\xAA\x01\x08',
        b'\xAB\x01\x02',
        b'\xAC\x01\xD8',
        b'\xAD\x01\x04',
        b'\xAE\x01\x00',
        b'\xAF\x01\x00',

        b'\xB0\x01\x48',
        b'\xB1\x01\x00',
        b'\xB2\x01\x0A',
        b'\xB3\x01\x02',
        b'\xB4\x01\xDA',
        b'\xB5\x01\x04',
        b'\xB6\x01\x00',
        b'\xB7\x01\x00',
        b'\xB8\x01\x48',
        b'\xB9\x01\x00',
        b'\xBA\x01\x0C',
        b'\xBB\x01\x02',
        b'\xBC\x01\xDC',
        b'\xBD\x01\x04',
        b'\xBE\x01\x00',
        b'\xBF\x01\x00',

        b'\xC0\x01\x10',
        b'\xC1\x01\x47',
        b'\xC2\x01\x56',
        b'\xC3\x01\x65',
        b'\xC4\x01\x74',
        b'\xC5\x01\x88',
        b'\xC6\x01\x99',
        b'\xC7\x01\x01',
        b'\xC8\x01\xBB',
        b'\xC9\x01\xAA',

        b'\xD0\x01\x10',
        b'\xD1\x01\x47',
        b'\xD2\x01\x56',
        b'\xD3\x01\x65',
        b'\xD4\x01\x74',
        b'\xD5\x01\x88',
        b'\xD6\x01\x99',
        b'\xD7\x01\x01',
        b'\xD8\x01\xBB',
        b'\xD9\x01\xAA',

        cmd_param(CMD_CSC4,     b'\x01'),   # CSC4: GIP_xPROT1
        cmd_param(CMD_CSC1,     b'\x00'),   # CSC1: disable

        cmd_param(CMD_COLMOD,   b'\x05'),   # 0x05 = 16-bit/pixel
        cmd_param(CMD_TEON,     b'\x00'),
        cmd_param(CMD_INVON),

        cmd_param(CMD_SLPOUT, delay=120),
        cmd_param(CMD_DISPON),
    ])

    def __init__(self, bus, **kwargs):
        super().__init__(bus, self._INIT_SEQUENCE, **kwargs)

if __name__ == '__main__':
    display = busdisplay.BusDisplay(
        display_bus,
        init_sequence=_INIT_SEQUENCE,
        width=360, height=360,
        colstart=0, rowstart=0,
        rotation=0,
        color_depth=16, grayscale=False,
        pixels_in_byte_share_row=True, bytes_per_cell=1,
        reverse_pixels_in_byte=False,
        set_column_command= 42,
        set_row_command= 43,
        write_ram_command=44,
        backlight_pin=microcontroller.pin.GPIO7,
        backlight_on_high=True,
        #brightness_command=None,
        brightness=0.2,

        single_byte_bounds=False,
        data_as_commands=False, auto_refresh=True, native_frames_per_second=60,
        SH1107_addressing=False
    )
