import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
import json
from pathlib import Path
from flatten_json import flatten
from urllib.error import HTTPError
import time, sys
from IPython.display import clear_output
from sklearn.neighbors import NearestNeighbors