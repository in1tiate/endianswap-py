import os
import sys

#
# endianswap.py - for swapping endianness of a given file
# WARNING: Does not account for files of byte sizes not cleanly divisible by 4, will not swap the last few bytes of such files
#

filename = sys.argv[1]
outfile = filename + ".converted"

final_array = bytearray()

print("Working on file: " + filename + "...")
with open(filename, "rb") as file:
    data = file.read(4) # Read first 4 bytes
    while data:
        ba_data = bytearray(data) # convert data to byte array
        ba_data.reverse()
        final_array.extend(ba_data) # append reversed bytes to final file
        data = file.read(4) # read next four bytes, then loop

with open(outfile, "wb") as out_file:
    out_file.write(final_array) # write final file to disk
        



        
    
