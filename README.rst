Introduction
============

CircuitPython libraries for various displays

NV3007

- 1.68" 428x142 SPI

GC9D01

- 0.71" 160x160 SPI

ST77916

- 1.5" 360x360 QSPI

Usage Example
=============

.. code-block:: python

    import board
    import busio
    import displayio
    import fourwire
    from circuitpython_nv3007 import NV3007

    displayio.release_displays()

    spi = busio.SPI(clock=board.IO1, MOSI=board.IO2)
    while not spi.try_lock():
        pass
    spi.configure(baudrate=80_000_000)
    spi.unlock()

    display_bus = fourwire.FourWire(
        spi,
        command=board.IO10,
        chip_select=board.IO11,
        reset=board.IO3
    )
    display = NV3007(
        display_bus,
        width=428, height=142,
        rowstart=0, colstart=12,
        rotation=90, backlight_pin=board.IO12
    )
    display.brightness = 0.2


