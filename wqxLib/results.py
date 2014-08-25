# -*- coding: utf-8 -*-
#========================================================================= 
# BBALEY/Automated Control Systems, Inc. 08-25-2014
# Aquatic Informatics (WQX) Water Quality data interface / API client
#========================================================================= 


import apiMethods as api
import json

# WQX classes
#========================================================================= 



class cResult(object):
    # WQX observation
    def __init__(self, 
                 _id = "",
                 _customId = "",
                 _unit = "",
                 _value = 0.00
                 ):
 
        self.id = _id
        self.customId = _customId
        self.unit = _unit
        self.value = _value
        
        
    def toDict(self):
        # return a dict payload that can be sent to RESTful inteface/service
    
        jpl = {
        'customId' : self.customId,
        'unit' : self.unit,
        'value' : self.value
        }           
        
        return jpl
        #json.dumps(jpl)
        
        
#========================================================================= 
def getResult(_customId):
    allres = api.getData('results')
    res = cResult()
    
    found = False
        
    for obj in json.loads(allres):
        # print allobs
        
        
        if (obj['customId'] == _customId) or (obj['id'] == _customId):    
            res.id = obj['id']
            res.customId = obj['customId']
            res.unit = obj['unit']           
            res.value = obj['value']
               
            found = True            
    if not found:
        res = None        
    return res

        
        
#=========================================================================  
  