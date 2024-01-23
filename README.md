# endianswap.py

Reverses every 4 bytes of a given input file. In other words, reverses file endianness. Does not work correctly on files containing a number of bytes not cleanly divisible by 4.

This was made to convert between N64 emulator save files created by different emulators, as the two in question used opposite endianness when storing save data.
