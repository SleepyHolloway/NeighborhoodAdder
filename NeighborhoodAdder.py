"""
Neighborhood Adder:

This program uses the exterenal module pyshp and Python 3

This program uses a Zetashapes file of Omaha, and a modified Census Blcok Groups file from TIGER to
add the neighborhood attribute to the existing entries in Douglas county. The modification to the
Block group file is that an empty field 'NHOOD' is added to the Census Block Groups file before
starting the program.

This program outputs 3 files, FinalProduct.* these files contain the database with the updated neighborhoods
"""


import json

import shapefile #This is an external module https://github.com/GeospatialPython/pyshp



i=0 #counter initialization
j=0

file_name = "tl_2014_31_bg/tl_2014_31_bg"   #filename of Census Block Groups
sf = shapefile.Reader(file_name)            #brings the shapefile in as an object
records = sf.records()                      #loads the database data from the shapefile into python object records

with open('31055.geojson') as d:#brings the json data in as a dictionary
   data = json.load(d)
   

while j < len(records): #Loop through each line of the shapefile database
    
    if records[j][1] == "055": #Skip the entry if the data is not from Douglas County
        
        for feature in data['features']: #For each neighborhood
            i=0                          #counter reset   
            
            while i < len(feature['properties']['blockids']):  #iterate through each block value in the json data

                if(feature['properties']['blockids'][i:i+12]==records[j][4]):#search for a match between the json data and the shape data
                    temp = feature['properties']['label']                    #Creates temp string of Neighborhood for current value   
                    records[j][12] = temp.replace(" ","_")                   #Sets the 'NHOOD' column of the current record to the 'label' value of the current json feature
                    break                                                    #stop searching after a match is found
                
                i += 16   #increment by 16, the distance between entries in the json blockids
              

    j += 1 #On to the next line of the Census Data!

w = shapefile.Writer(shapefile.POLYGON) #Creates a shapefile writer
w.fields = list(sf.fields)              #Adds the Census Block fields to the writer
w.records.extend(records)               #Adds the Census Block records as modified by this program
w._shapes.extend(sf.shapes())           #Adds the Shapes
w.save("FinalProduct")                  #Outputs the final file
print("FinalProduct.* has been creaated")


