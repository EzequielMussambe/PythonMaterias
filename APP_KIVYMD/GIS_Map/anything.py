from arcgis.gis import GIS
from arcgis.geocoding import geocode, reverse_geocode
from arcgis.geometry import Point

gis = GIS()

geocode_result = geocode(address="Hollywood sign", as_featureset=True)

# A list of features
#geocode_result.features

m = gis.map("Los Angeles, CA", zoomlevel=11)

m.draw(geocode_result)


import matplotlib.pyplot as plt