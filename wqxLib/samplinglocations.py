# -*- coding: utf-8 -*-
#========================================================================= 
# BBALEY/Automated Control Systems, Inc. 08-25-2014
# Aquatic Informatics (WQX) Water Quality data interface / API client
#========================================================================= 

import apiMethods as api
import json

# WQX classes
#========================================================================= 


class cSamplingLocation(object):
    # WQX Sampling/monitoring location
    def __init__(self, 
                 _id = "",
                 _sname = "",
                 _customId = "",
                 _stype = "",
                 _latitude = "",
                 _longitude = "",
                 _horizontalDatum = "DM_horizontal_datum",
                 _verticalDatum = "DM_vertical_datum",
                 _horizontalCollectionMethod = "DM_horizontal_collection_method",
                 _verticalCollectionMethod = "DM_vertical_collection_method",
                 _countryCode = "US",
                 _stateCode = "OR",
                 _countyCode = ""                 
                 ):
 
        self.id = _id;
        self.sname = _sname
        self.customId = _customId
        self.stype = _stype
        self.latitude = _latitude
        self.longitude = _longitude
        self.horizontalDatum = _horizontalDatum
        self.verticalDatum = _verticalDatum
        self.horizontalCollectionMethod = _horizontalCollectionMethod
        self.verticalCollectionMethod = _verticalCollectionMethod
        self.countryCode = _countryCode
        self.stateCode = _stateCode
        self.countyCode = _countyCode

        
    def toDict(self):
        # return a dict payload that can be sent to RESTful inteface/service
    
        jpl = {
        'name' : self.sname,
        'customId' : self.customId,
        'type' : self.stype,
        'latitude' : self.latitude,
        'longitude' : self.longitude,
        'horizontalDatum' : self.horizontalDatum,
        'verticalDatum' : self.verticalDatum,
        'horizontalCollectionMethod' : self.horizontalCollectionMethod,
        'verticalCollectionMethod' : self.verticalCollectionMethod,
        'countryCode' : self.countryCode,
        'stateCode' : self.stateCode,
        'countyCode' : self.countyCode
        }
        
        return jpl
        
        
          #sname
          #customId
          #stype
          #latitude
          #longitude
          #horizontalDatum
          #verticalDatum
          #horizontalCollectionMethod
          #verticalCollectionMethod
          #countryCode
          #stateCode
          #countyCode
        
#========================================================================= 
def getSamplingLocation(_customId):
    allres = api.getData('samplinglocations')
    sloc = cSamplingLocation()
    
    found = False
        
    for obj in json.loads(allres):
        # print allobs
        
        if (obj['customId'] == _customId) or (obj['id'] == _customId):
            
            sloc.id = obj['id']
            sloc.sname = obj['name']
            sloc.customId = obj['customId']
            sloc.stype = obj['type']
            sloc.latitude = obj['latitude']
            sloc.longitude = obj['longitude']
            sloc.horizontalDatum = obj['horizontalDatum']
            sloc.verticalDatum = obj['verticalDatum']
            sloc.horizontalCollectionMethod = obj['horizontalCollectionMethod']
            sloc.verticalCollectionMethod = obj['verticalCollectionMethod']
            sloc.countryCode = obj['countryCode']
            sloc.stateCode = obj['stateCode']
            sloc.countyCode = obj['countyCode']
               
            found = True            
    if not found:
        sloc = None        
    return sloc

        
        
#=========================================================================          
  
  