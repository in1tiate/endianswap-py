import os
import sys

filename = sys.argv[1]
outfile = filename + ".converted.flash"

final_array = bytearray()

print("Working on file: " + filename + "...")
with open(filename, "rb") as file:
    data = file.read(4)
    while data:
        ba_data = bytearray(data)
        ba_data.reverse()
        final_array.extend(ba_data)
        data = file.read(4)

with open(outfile, "wb") as out_file:
    out_file.write(final_array)
        



        
    