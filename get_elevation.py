#!/usr/bin/env python

"""
Get site elevation by interfacing with the Google Maps Elevation API
https://developers.google.com/maps/documentation/elevation/intro

Returns elevation in metres

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (29.09.2015)"
__email__ = "mdekauwe@gmail.com"

import simplejson
import urllib

def get_elevation(lat, lon):

    base_url = 'https://maps.googleapis.com/maps/api/elevation/json'
    url_params = "locations=%.7f,%.7f" % (lat, lon)
    url = "%s?%s" % (base_url,  url_params)
    result = simplejson.load(urllib.urlopen(url))
    elevation = result["results"][0]["elevation"]

    return (elevation)


if __name__ == '__main__':

    lat = -29.26399994
    lon = -61.02799988
    elevation = get_elevation(lat, lon)
    print elevation
