from astroquery.heasarc import Heasarc
from astropy.coordinates import SkyCoord


obs = input()
pos = SkyCoord.from_name(obs)

nicerl3 = hsp.HSPTask('nicerl3-spect')
nicerl3.clobber="yes"
nicerl3.geomag_path=paths.geomag_path
nicerl3(indir