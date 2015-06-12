import numpy as np
import gdal
import sys
import matplotlib.pyplot as plt
import pandas as pd
import sys                       # platform, args, run tools
import os                        # platform, args, run tools
import glob


# Going through files in a directory
glob2.glob('./*.tif')
# ['./outline.txt', './pip-log.txt', './test.txt', './testingvim.txt']


# Loop through raster bands

# Band 1
src_ds = gdal.Open("LS081410412015060100000000MS00_B01.tif")
if src_ds is None:
    print ("Unable to open INPUT.tiff")
    sys.exit(1)

print ("[ RASTER BAND COUNT ]:", src_ds.RasterCount)
for band in range( src_ds.RasterCount ):
    band += 1
    print ("[ GETTING BAND ]:", band)
    srcband = src_ds.GetRasterBand(band)
    if srcband is None:
        continue

    stats = srcband.GetStatistics( True, True )
    if stats is None:
        continue

    print ("[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % ( \
                stats[0], stats[1], stats[2], stats[3] ))

# To get actual band raw values as matrix
print (srcband.GetDataSet())
