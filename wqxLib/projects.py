# -*- coding: utf-8 -*-
#========================================================================= 
# BBALEY/Automated Control Systems, Inc. 08-25-2014
# Aquatic Informatics (WQX) Water Quality data interface / API client
#========================================================================= 


import apiMethods as api
import json

# WQX classes
import activities as ac
#========================================================================= 

class cProject(object):
    # WQX Sampling/monitoring location
    def __init__(self, 
                 _id = "",
                 _sname = "",
                 _customId = "",
                 _description = ""
                 ):
 
        self.id = _id
        self.sname = _sname
        self.customId = _customId
        self.description = _description
        
        self.activities = []   #ac.cActivity[]

        
    def toDict(self):
        # return a dict payload that can be sent to RESTful inteface/service
    
        jpl = {
        'name' : self.sname,
        'customId' : self.customId,
        'description' : self.description
        }
        
        return jpl
        
    def toDictAll(self):
        # return a dict payload that can be sent to RESTful inteface/service
    
        jpl = {
        'name' : self.sname,
        'customId' : self.customId,
        'description' : self.description,
        'activities' : self.activities
        }
        
        return jpl
        
    #========================================================================= 
    # pass either a list of customIDs or activity objects
    # if passing objects, it is assumed they exist
    # use the api.getActivity() method to get and pass them !
    #========================================================================= 
    def addActivities(self, _actCIDlist):
            result = ""
            
            alist = []
            
            if _actCIDlist[0] is str:
                for cid in _actCIDlist:
                    aid = api.getActivity(cid)
                
                    if aid is not None:
                        alist.append(aid.id)
                        
            else:
                if isinstance(_actCIDlist[0],ac.cActivity):
                    for cid in _actCIDlist:
                        alist.append(cid.id)
                                
            self.activities = alist
        
            result = api.putData(self.toDictAll(), 'projects', self.id)
            #print result
            
            return result
  
    #========================================================================= 



#=========================================================================     
# retrieves a project from API and returns a project oobject if found
# pass either an id or a customId
#========================================================================= 
def getProject(_customId):
    allprj = api.getData('projects')
    prj = cProject()
    
    found = False
        
    for obj in json.loads(allprj):
        # print allobs
        
        if (obj['customId'] == _customId) or (obj['id'] == _customId):
            
            prj.id = obj['id']
            prj.description = obj['description']
            prj.customId = obj['customId']
            prj.sname = obj['name']
            
            if 'activities' in obj:                   
                for aid in obj['activities']:
                    a = ac.getActivity(aid)
                    prj.activities.append(a)
                    
                # prj.activities = obj['activities']
               
            found = True            
    if not found:
        prj = None        
    return prj


#========================================================================= 

        
        
        
        
        
        
        
        