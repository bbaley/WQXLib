# -*- coding: utf-8 -*-
#========================================================================= 
# BBALEY/Automated Control Systems, Inc. 08-25-2014
# Aquatic Informatics (WQX) Water Quality data interface / API client
#========================================================================= 


import apiMethods as api
import json

# WQX classes
#========================================================================= 

# Observations can be either for a samplingLocation,
# OR a specimen !

class cObservedProperty(object):
    # WQX observation
    def __init__(self, 
                 _id = "",
                 _customId = "",
                 _sname = "",
                 _description = ""
                 ):
 
        self.id = _id 
        self.customId = _customId
        self.sname = _sname
        self.description = _description
        
    def toDict(self):
        # return a dict payload that can be sent to RESTful inteface/service
    
        jpl = {
        'description' : self.description,
        'name' : self.sname,
        'customId' : self.customId
        }
        
        return jpl
        
        
          #sname
          #description

#========================================================================= 
def getObservedProperty(_customId):
    allres = api.getData('observedproperties')
    op = cObservedProperty()
    
    found = False
        
    for obj in json.loads(allres):
        # print allobs
        
        if (obj['customId'] == _customId) or (obj['id'] == _customId):
            
            op.id = obj['id']
            op.customId = obj['customId']
            op.sname = obj['name']           
            op.description = obj['description']
               
            found = True            
    if not found:
        op = None        
    return op

        
        
#=========================================================================  