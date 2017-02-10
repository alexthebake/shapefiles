# Shapefiles
This repo contains utility scripts/modules for dealing with Shapefiles.

## Installation
### Must Haves
You'll definitely need [pip](https://pip.pypa.io/en/stable/installing/).

Then you can run:
```
pip install -r requirements.txt
```

### Virtualenv
If you have [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) installed,
you can run the following to install everything:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage
### `find_points.py`

`find_points.py` simply checks if a given CSV of longitude and lattitude points
exist within a given shapefile. Most of the implementation was taken from [StackOverflow](http://stackoverflow.com/questions/7861196/check-if-a-geopoint-with-latitude-and-longitude-is-within-a-shapefile).

```
python find_points.py <shapefile_filename> <points_csv_filename>
```
