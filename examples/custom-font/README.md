# Custom Font
Demo program that displays temperature, determined by the built-in temperature sensor on a GC9A01 display through Plus Jakarta Sans font.

### Generating custom fonts
To generate custom fonts you can use `font2bitmap.py`. It requires an additional python library `freetype-py`.

The fonts (`plus_jakarta_sans_32.py`,`plus_jakarta_sans_64.py`) used in this example, are generated with following commands:
```sh
python font2bitmap.py PlusJakartaSans-Light.ttf 64 -c 0x20-0x7f
python font2bitmap.py PlusJakartaSans-SemiBold.ttf 32 -c 0x20-0x7f
```

**Note:** This device is running with a custom firmware. [Download][firmware] it and
[flash][raspb-pico-getting-started] it on your device before trying any examples.

[firmware]: <https://github.com/russhughes/gc9a01_mpy/tree/main/firmware/RP2>
[raspb-pico-getting-started]: <https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3>