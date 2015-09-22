#Overview
This project is a way to match neighborhoods to block groups.  Neighborhood shapes are in the form of geojson, and come from [zetashapes](http://zetashapes.com).  Block groups come from TIGER data in cesus.gov


#File description
##tl_2014_31_bg 
This folder conatiains the Census Block data used by NeighborhoodAdder.py the field 'NHOOD' has been added to this data

##31055.geojson 
This file contains the Zetashape data used by NeighborhoodAdder.py

##NeighborhoodAdder.py
This file compares the previous mentioned data to add neighborhoods to census blocks in Omaha,NE
			This program outputs 3 files called FinalProduct.*

##pyshp-master.zip
This is the external module pyshp used in this program
