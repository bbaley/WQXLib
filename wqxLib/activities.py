# -*- coding: utf-8 -*-
#========================================================================= 
# BBALEY/Automated Control Systems, Inc. 08-25-2014
# Aquatic Informatics (WQX) Water Quality data interface / API client
#========================================================================= 

import apiMethods as api
import json

# WQX classes
import observations as ob
#========================================================================= 

class cActivity(object): 
    # WQX activity
    def __init__(self, 
                 _id = "",
                 _stype = "",
                 _customId = "",
                 _mediaName = "",
                 _startTime = "",
                 _endTime = ""
                 ):
 
        self.id = _id;
        self.stype = _stype
        self.customId = _customId
        self.mediaName = _mediaName
        self.startTime = _startTime
        self.endTime = _endTime
        
        self.observations = []

        
    def toDict(self):
        # return a dict payload that can be sent to RESTful inteface/service
    
        jpl = {
        'type' : self.stype,
        'customId' : self.customId,
        'mediaName' : self.mediaName,
        'startTime' : self.startTime,
        'endTime' : self.endTime,
        'observations' : self.observations
        }
        
        return jpl
        
        
          #stype
          #customId
          #mediaName
          #startTime
          #endtime
        
        
    #========================================================================= 
    # pass either a list of customIDs or observation objects
    # if passing objects, it is assumed they exist
    # use the api.getObservation() method to get and pass them !
    #========================================================================= 
    def addObservations(self, _CIDlist):
            result = ""
            
            alist = []
            
            if _CIDlist[0] is str:
                for cid in _CIDlist:
                    aid = api.getActivity(cid)
                
                    if aid is not None:
                        alist.append(aid.id)
                        
            else:
                if _CIDlist[0] is isinstance(_CIDlist[0], ob.cObservation):
                    for cid in _CIDlist:
                        alist.append(cid.id)
                                
            self.observations = alist
        
            result = api.putData(self.toDictAll(), 'observations', self.id)
            #print result
            
            return result
  
    #=========================================================================     
  
#========================================================================= 
def getActivity(_customId):
    allact = api.getData('activities')
    act = cActivity()
    
    found = False
        
    for obj in json.loads(allact):
        # print allobs
        
        if (obj['customId'] == _customId) or (obj['id'] == _customId):
            
            act.id = obj['id']
            act.customId = obj['customId']
            act.startTime = obj['startTime']           
            act.endTime = obj['endTime']
            act.mediaName = obj['mediaName']
            
            if 'observations' in obj:
                act.observations = obj['observations']
               
            found = True            
    if not found:
        act = None        
    return act

        
        
#=========================================================================         
    
                
    
    