import os
import sys

# os.system('heainit') 
sys.path.insert(0,'/home/ankit/heasoft-6.35src/heasoft-6.35/x86_64-pc-linux-gnu-libc2.39/lib/python')
import heasoftpy as hsp


os.chdir('/home/ankit/Development/Heasarc/nicer/Cas_A')

print(os.getcwd())
print(os.listdir())
# nicerl2 = hsp.HSPTask('nicerl2')
# nicerl2.clobber="yes"
# if not os.path.exists('7010080341-output/'):
#     os.makedirs('7010080341-output/')
# if os.path.exists('7010080341-output/'):
#     os.system('cp 7010080341/auxil/ni*.mkf 7010080341-output')
# result = nicerl2(indir='7010080341', cldir='7010080341-output', mkfile='$CLDIR/ni$OBSID.mkf')
# print(result)


# # spectra
# nicerl3 = hsp.HSPTask('nicerl3-spect')
# # nicerl3.CLDIR = '7010080341-output/spectra'
# nicerl3.outlang = 'PYTHON'
# result = nicerl3(indir = '7010080341-output', )
# print(result)

print(os.path.exists('5010080245/xti/event_cl/ni5010080245mpu7_sr.pha'))

from xspec import *
s = Spectrum("5010080245/xti/event_cl/ni5010080245mpu7_sr.pha")
# Model("phabs*pow")
# Fit.perform()
# Plot.device = "/xs"
# Plot("ratio")


print(AllModels.show())


# Plot.device = "/xs"
# Plot.xAxis = "channel"
# Plot.xAxis = "MeV"
# Plot.xAxis = "Hz"
# Plot.xAxis = "angstrom"
# # Plot(s)
# Plot("energy")
# Plot.show()
# Plot("data")
# Plot("model")
# Plot("ufspec")
# Plot.__call__()


# exec(open('7010080341-output/ni7010080341mpu7_load.py').read())


# # Extracting the Light Curve
# nicerl3_lc = hsp.HSPTask('nicerl3-lc')
# nicerl3_lc.pirange = '300-1500'
# nicerl3_lc.timebin=60.0
# nicerl3_lc.clobber='YES'
# result = nicerl3_lc(indir = '7010080341')
# print(result)


# fplot = hsp.HSPTask('fplot')
# fplot.offset='YES'
# fplot.device = '/xs'
# result = fplot(infile = '7010080341/xti/event_cl/ni7010080341mpu7_sr.lc', )
# print(result)








