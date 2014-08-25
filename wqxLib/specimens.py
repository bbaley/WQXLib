# -*- coding: utf-8 -*-
#========================================================================= 
# BBALEY/Automated Control Systems, Inc. 08-25-2014
# Aquatic Informatics (WQX) Water Quality data interface / API client
#========================================================================= 



import apiMethods as api
import json


# WQX classes
import samplinglocations as sl
#========================================================================= 

class cSpecimen(object):
    # WQX activity
    def __init__(self, 
                 _id = "",
                 _customId = "",
                 _name = "",
                 _description = "",
                 _stype = "",                 
                 _samplingTime = ""
                 ):
 
        self.id = _id;
        self.customId = _customId
        self.sname = _name,
        self.description = _description
        self.stype = _stype
        self.samplingTime = _samplingTime
        
        self.samplingLocation = sl.cSamplingLocation()
        

    def toDict(self):
        # return a dict payload that can be sent to RESTful inteface/service
    
        jpl = {
        'type' : self.stype,
        'customId' : self.customId,
        'description' : self.description,
        'name' : self.sname,
        'samplingTime' : self.samplingTime,
        'samplingLocation' : { 'id' : self.samplingLocation.id  }
        }
        
        return jpl
        
        
          #stype
          #description
          #name
          #samplingTime
          #samplingLocation
  


#=========================================================================     
# retrieves a project from API and returns a project oobject if found
#========================================================================= 
def getSpecimen(_customId):
    allspec = api.getData('specimens')
    sp = cSpecimen()
    
    found = False
        
    for obj in json.loads(allspec):
        # print allobs
        
        if (obj['customId'] == _customId) or (obj['id'] == _customId):
            
            sp.id = obj['id']
            sp.samplingTime = obj['samplingTime']
            sp.description = obj['description']
            sp.sname = obj['name']
            sp.stype = obj['type']
            sp.customId = obj['customId']                        
               
            found = True            
    if not found:
        sp = None        
    return sp


#=========================================================================   