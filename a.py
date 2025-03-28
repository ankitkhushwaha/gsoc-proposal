import os

def list_directory(root_dir):
    for root, dirs, files in os.walk(root_dir):
        level = root.replace(root_dir, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        sub_indent = " " * 4 * (level + 1)
        for file in files:
            print(f"{sub_indent}{file}")

root_directory = "/home/ankit/Development/Heasarc/nicer/Cas_A/output"
list_directory(root_directory)


class GeomagneticData:
    """
    Handles the geomagnetic data
    initialized at start of software if internet is availble,
    checks for the new files and Downloads them 
    """
    @classmethod
    def fetch_geomag_data():
        """
        run `nigeodown` under hood and download and install data
        """

class NicerDataPipeline:
    """
    Completer data Reduction/extraction Pipeline for Nicer
    """
    def __init__(self, obs_path, **kwargs):
        """
        initialize the Heasoft software
        Checks for Calibration files
        """
        caldb = caldb_files.exists()                # checks for calibration files exists or not
        valid_obs = check_valid_obs(obs_path)      # incase of local Obs directry given  
        if not valid_obs:
            raise TypeError('Given dir is Not Valid Nicer Observation')

    def data_reduction(infile, ra, dec, **kwargs):
        """
        The the data processing and Reduces the raw data
        Save it in Output Obs directry using `nicerl2`
        """
        nicerl2 = hsp.HSPTask('nicerl2')
        nicerl2.clobber="yes"
        result = nicerl2(infile= infile, ra, dec, **kwargs)
        return result

    def extract_spectrum(indir, ra, dec, **kwargs):
        """
        Extract the Spectrum from output from `nicerl2` using
        `nicerl3-spect & Save it in Output Obs directry` 
        """
        nicerl3 = hsp.HSPTask('nicerl3-spect')
        nicerl3.clobber="yes"
        result = nicerl3(infile=indir, ra, dec, **kwargs)
        return result

    def extract_lc(ininfile, pirange = '300-1500', timebin=60.0,clobber = 'Yes', **kwargs):
        """
        Extract the Light curve from output from `nicerl2` using
        `nicerl3-lc & Save it in Output Obs directry` 
        """
        nicerl3_lc = hsp.HSPTask('nicerl3-lc')
        nicerl3_lc.pirange = pirange        # channel (energy) range 
        nicerl3_lc.timebin= timebin         # time bin size in seconds 
        nicerl3_lc.clobber= clobber
        result = nicerl3_lc(indir = indir, **kwargs)
        return result


from astroquery.heasarc import Heasarc
from astropy.coordinates import SkyCoord

class Retrieve_Heasarc:
    
    @classmethod
    def filter_data(self):
        """
        Fetch the Observation different attributes
        This Will intergrate with UI and user will filter the 
        data based on different attributes. 
        """

    @classmethod
    def fetch_data(self, pos , catalog = 'nicermastr'):
        """
        This will return the Obs data to UI. 
        Which will be displayed by UI.
        """
        pos = SkyCoord.from_name(pos)
        tab = Heasarc.query_region(pos, catalog = catalog)
        tab = self.filter_data(tab)
        return tab
    
    @classmethod
    def download_obs(tabs, obs_to_download):
        """
        download the observation from fetch_data or links 
        provided as input
        """
        links = Heasarc.locate_data(tab(obs_to_download))
        tab = tabs
        tab.add_columns(links['access_url'], name = 'access_url', index = 0)
        if obs.size > 10 'Gb':
            # shows a msg stating the size of Observation data 
            # Downloads observation in Chunks
        else:
            obs = Heasarc.download_data(links = links)
        obs_download_status = True if obs.file.exists else False
        return obs_download_status

# def retrieve_heasarc(pos = 'Cas A'):
#     tab = tab[tab['exposure'] > 0]

#     links = Heasarc.locate_data(tab[:3])
#     links.add_column()
#     links['access_url'].pprint()
#     Heasarc.download_data(links=links[1:2]) # download the files in current folder

class Observations:
    """
    Process Multiple Observation at once. Plot useful insights from Processed Data.
    Deals with ML techniques to classify the observations.
    """
    def __init__(self, obs = "Nicer"):
        """
        Each Observation will be associated with unique Keyword, eg. 'nicer', 'nustar'
        """
        self.obs = []

    def load_data(self, data):
        """
        Load multiple processed observations into the class.
        take inputs in form of list, direct local path of Observation.
        """
        self.data = data

    def plot(self):
        """
        Generic function to plot observation data.
        This will plot the various plots for ex, Lightcurve, Spectrum,\
            hardness-ratios and color-color diagrams
        """
    
    def classify_observations(self, model):
        """
        Classify the observations using a pretrained ML model.
        """

    def Save(self):
        """
        Saves the Plot in Graphical Output.
        """

class XRayClassifier:
    def __init__(self, obs):
        """
        Initialize the classifier with a trained model.
        
        Inputs a Observations class instance checks whether required file exist or not.
        Collects required features(Power spectrum, light curve) 
        """

    def preprocess_features(self, *features):
        """
        Preprocess the input features before prediction, and
        will process Multiple observation features at once
        """
        # Standardize the features
        if self.scaler:
            features = self.scaler.transform([features])
        else:
            features = np.array([features])
        return features

    def predict(self, *processed_features):
        """
        Predict the observation state based on standardized input features.
        """
        prediction = self.model.predict(processed_features)
        return prediction