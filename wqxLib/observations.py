# -*- coding: utf-8 -*-
#========================================================================= 
# BBALEY/Automated Control Systems, Inc. 08-25-2014
# Aquatic Informatics (WQX) Water Quality data interface / API client
#========================================================================= 



import apiMethods as api
import json

# WQX classes
import observedProperties as op
import samplinglocations as sl
import specimens as sp
import results as res
#========================================================================= 

# Observations can be either for a samplingLocation,
# OR a specimen !

# when samplingLocation : "dataClassification": "DERIVED"
# when specimen : "dataClassification": "LAB"

# Rules:
# an Observation can have:
#     only one observered property
#     only one sampling location
#     more than one result
#     only one specimen
#     cannot have both a specimen and a sampling location
#         when has a speciment, has no sampling location, as the specimen will have a sampling location
#            all specimens have a sampling location


class cObservation(object):
    # WQX observation
    def __init__(self, 
                 _id = "",
                 _dataClassification = "",
                 _customId = "",
                 _medium = "",
                 _resultTime = "",
                 _observedTime = ""
                 ):
 
        self.id = _id
        self.dataClassification = _dataClassification
        self.customId = _customId
        self.medium = _medium
        self.resultTime = _resultTime
        self.observedTime = _observedTime
        
        self.observedProperty = None  #op.cObservedProperty()
        
        self.specimen = None # sp.cSpecimen()

        self.samplingLocation = None  # sl.cSamplingLocation()
        
        self.results = []

        
    def toDict(self):
        # return a dict payload that can be sent to RESTful inteface/service
    
        
        jpl = {
            'dataClassification' : self.dataClassification,
            'customId' : self.customId,
            'resultTime' : self.resultTime,
            'medium' : self.medium,
            'observedTime' : self.observedTime
            }

        if self.samplingLocation is not None:
            jpl.update({ 'samplingLocation' : { 'id' : self.samplingLocation.id } })      
            
        if self.observedProperty is not None:
            jpl.update({ 'observedProperty' : { 'id' : self.observedProperty.id } })            

        if self.specimen  is not None:
            jpl.update({ 'specimen' : { 'id' : self.specimen.id } })
        
        if self.results != []:
            rid = []                                    

                
            for r in list(self.results):
                rid.append(r.id)
                
                jpl.update({ 'results' : rid })
        
        return dict(jpl)
        
        
        
    #========================================================================= 
    # pass either a list of customIDs or result objects
    # if passing objects, it is assumed they exist
    # use the api.getResult() method to get and pass them !
    #========================================================================= 
    def addResults(self, _CIDlist):
            result = ""
            
            alist = []
            
            if _CIDlist[0] is str:
                for cid in _CIDlist:
                    aid = api.getResult(cid)
                
                    if aid is not None:
                        alist.append(aid.id)
                        
            else:
                if _CIDlist[0] is isinstance(_CIDlist[0], res.cResult):
                    for cid in _CIDlist:
                        alist.append(cid.id)
                                
            self.results = alist
        
            result = api.putData(self.toDictAll(), 'observations', self.id)
            #print result
            
            return result
  
    #=========================================================================    
        
#    # I don't think these are needed - currently the model only allows
#    # one of each of these per observation
#    #========================================================================= 
#    # pass either a list of customIDs or observation objects
#    # if passing objects, it is assumed they exist
#    # use the api.getObservation() method to get and pass them !
#    #========================================================================= 
#    def addSamplingLocations(self, _CIDlist):
#            result = ""
#            
#            alist = []
#            
#            if _CIDlist[0] is str:
#                for cid in _CIDlist:
#                    aid = api.getSamplingLocation(cid)
#                
#                    if aid is not None:
#                        alist.append(aid.id)
#                        
#            else:
#                if _CIDlist[0] is sl.cSamplingLocation:
#                    for cid in _CIDlist:
#                        alist.append(cid.id)
#                                
#            self.samplingLocations = alist
#        
#            result = api.putData(self.toDictAll(), 'observations', self.id)
#            #print result
#            
#            return result
#  
#    #=========================================================================    
#  
#    #========================================================================= 
#    # pass either a list of customIDs or observation objects
#    # if passing objects, it is assumed they exist
#    # use the api.getObservation() method to get and pass them !
#    #========================================================================= 
#    def addObservedProperties(self, _CIDlist):
#            result = ""
#            
#            alist = []
#            
#            if _CIDlist[0] is str:
#                for cid in _CIDlist:
#                    aid = api.getActivity(cid)
#                
#                    if aid is not None:
#                        alist.append(aid.id)
#                        
#            else:
#                if _CIDlist[0] is ob.cObservation:
#                    for cid in _CIDlist:
#                        alist.append(cid.id)
#                                
#            self.observations = alist
#        
#            result = api.putData(self.toDictAll(), 'observations', self.id)
#            #print result
#            
#            return result
#  
#    #=========================================================================    
#  
#    #========================================================================= 
#    # pass either a list of customIDs or observation objects
#    # if passing objects, it is assumed they exist
#    # use the api.getObservation() method to get and pass them !
#    #========================================================================= 
#    def addSpecimens(self, _CIDlist):
#            result = ""
#            
#            alist = []
#            
#            if _CIDlist[0] is str:
#                for cid in _CIDlist:
#                    aid = api.getActivity(cid)
#                
#                    if aid is not None:
#                        alist.append(aid.id)
#                        
#            else:
#                if _CIDlist[0] is ob.cObservation:
#                    for cid in _CIDlist:
#                        alist.append(cid.id)
#                                
#            self.observations = alist
#        
#            result = api.putData(self.toDictAll(), 'observations', self.id)
#            #print result
#            
#            return result
  
#=========================================================================  
# find and return an observation from the API  
#========================================================================= 
def getObservation(_customId):
    allact = api.getData('observations')
    obs = cObservation()
    
    found = False
        
    for obj in json.loads(allact):
        # print allobs
        
        if (obj['customId'] == _customId) or (obj['id'] == _customId):
            
            obs.id = obj['id']
            obs.customId = obj['customId']
            obs.medium = obj['medium']           
            obs.resultTime = obj['resultTime']
            obs.observedTime = obj['observedTime']
            obs.dataClassification = obj['dataClassification']
            
            if 'specimen' in obj:
                obs.specimenId = obj['specimen']
                
            if 'samplingLocation' in obj:
                obs.samplingLocationId = obj['samplingLocation']

            if 'observedProperty' in obj:
                obs.observedPropertyId = obj['observedProperty']
                
            # list of results, 0..x
            if 'results' in obj:
                obs.results = obj['resilts']                
                
            found = True            
    if not found:
        obs = None        
    return obs

        
        
#=========================================================================    