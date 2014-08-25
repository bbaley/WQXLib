# -*- coding: utf-8 -*-
# http://docs.python-requests.org/en/latest/user/quickstart/

#========================================================================= 
# BBALEY/Automated Control Systems, Inc. 08-25-2014
# Aquatic Informatics (WQX) Water Quality data interface / API client
#========================================================================= 
# this script is a test script with examples for using the API


import sys
import json
import requests
import logging
from time import strptime,strftime,localtime,sleep 

# WQX classes
import wqxLib.projects
import wqxLib.samplinglocations
import wqxLib.activities
import wqxLib.observedProperties
import wqxLib.observations
import wqxLib.specimens
import wqxLib.apiMethods as api

#========================================================================= 
errors = 0
#========================================================================= 


def start(url):
    global errors
    print '\n________________________________________________________________\n' 
    print 'Test @ ( %s ) %d' % (url, errors)
            

#========================================================================= 

def testResult1():
    res = wqxLib.results.cResult()
    res.customId = 'Result_Test_2'
    res.unit = 'F'
    res.value = '34.2'
        
    sid = api.postData(res.toDict(), 'results')
    print sid

#========================================================================= 

def testResult2():
    res = wqxLib.results.cResult()
    res.customId = 'Result_Test_1'
    res.unit = 'F'
    res.value = '76.8'
        
    sid = api.postData(res.toDict(), 'results')
    print sid
    
#========================================================================= 

def testResult3():
    res = wqxLib.results.cResult()
    res.customId = 'Result_Test_3'
    res.unit = 'F'
    res.value = '78.0'
        
    sid = api.postData(res.toDict(), 'results')
    print sid
#========================================================================= 

def testSampleLocation1():
    sloc = wqxLib.samplinglocations.cSamplingLocation()
    sloc.sname = "Sampling Location 1"
    sloc.customId = "SL_001_WXBO"
    sloc.stype = "RIVER"
    sloc.latitude = "44.900406"
    sloc.longitude = "-122.0893909"
    #sloc.horizontalDatum = ""
    #sloc.verticalDatum = ""
    #sloc.horizontalCollectionMethod = ""
    #sloc.verticalCollectionMethod = ""
    #sloc.countryCode = ""
    sloc.stateCode = "OR"
    #sloc.countyCode = ""
    
    sid = api.postData(sloc.toDict(), 'samplinglocations')
    print sid
    
#========================================================================= 

def testSampleLocation2():
    sloc = wqxLib.samplinglocations.cSamplingLocation()
    sloc.sname = "Sampling Location 2"
    sloc.customId = "SL_002_WXBO"
    sloc.stype = "RIVER"
    sloc.latitude = "44.900406"
    sloc.longitude = "-122.0893909"
    #sloc.horizontalDatum = ""
    #sloc.verticalDatum = ""
    #sloc.horizontalCollectionMethod = ""
    #sloc.verticalCollectionMethod = ""
    #sloc.countryCode = ""
    sloc.stateCode = "OR"
    #sloc.countyCode = ""
    
    sid = api.postData(sloc.toDict(), 'samplinglocations')
    print sid
    
#========================================================================= 

def testProject1():
    proj = wqxLib.projects.cProject()
    proj.sname = "Project_Test_1"
    proj.customId = "Project_Test_1"
    proj.description = "The Big sample dig"
    
    sid = api.postData(proj.toDict(), 'projects')
    print sid

#========================================================================= 

def testProject2():
    proj = wqxLib.projects.cProject()
    proj.sname = "Project_Test_2"
    proj.customId = "Project_Test_2"
    proj.description = "like, the second project !!!"
    
    sid = api.postData(proj.toDict(), 'projects')
    print sid

#=========================================================================     

def testActivity1():
    act = wqxLib.activities.cActivity()
    act.stype = "SAMPLE_ROUTINE"
    act.customId = "Activity_test_1"
    act.mediaName = "WATER"
    act.startTime = "2014-04-27T00:00:00.000-07"
    act.endTime = "2015-04-27T00:00:00.000-07"
    
    sid = api.postData(act.toDict(), 'activities')
    print sid

#=========================================================================     

def testActivity2():
    act = wqxLib.activities.cActivity()
    act.stype = "SAMPLE_ROUTINE"
    act.customId = "Activity_test_2"
    act.mediaName = "WATER"
    act.startTime = "2014-04-27T00:00:00.000-07"
    act.endTime = "2015-04-27T00:00:00.000-07"
    
    sid = api.postData(act.toDict(), 'activities')
    print sid

#=========================================================================     

def testActivity3():
    act = wqxLib.activities.cActivity()
    act.stype = "SAMPLE_ROUTINE"
    act.customId = "Activity_test_3"
    act.mediaName = "WATER"
    act.startTime = "2014-04-27T00:00:00.000-07"
    act.endTime = "2015-04-27T00:00:00.000-07"
    
    sid = api.postData(act.toDict(), 'activities')
    print sid
            
#=========================================================================     

def testObservedProperty():
    op = wqxLib.observedProperties.cObservedProperty()
    op.sname = "Temperature, water"
    op.description = "Temperature, water, ObsProperty test"
    op.customId = 'OP_Water_Temp'
    
    sid = api.postData(op.toDict(), 'observedproperties')
    print sid

#=========================================================================   

def testSpecimen1():    
    sp = wqxLib.specimens.cSpecimen()
    sp.sname = "Specimen_Test_1"
    sp.description = "Specimen_Test_1, description"
    sp.customId = 'Specimen_Test_1'
    sp.samplingTime = "2014-08-21T00:00:00.000-00:00"
    sp.stype = "water bottle"
    
#    sp.samplingLocation.id = "3122765f-cbaf-4234-aaeb-6dcebd9bbfbc"
    
    sl = wqxLib.samplinglocations.getSamplingLocation('SL_001_WXBO')
    sp.samplingLocation = sl
    
    sid = api.postData(sp.toDict(), 'specimens')
    print sid

#=========================================================================   

def testSpecimen2():    
    sp = wqxLib.specimens.cSpecimen()
    sp.sname = "Specimen_Test_2"
    sp.description = "Specimen_Test_2, description"
    sp.customId = 'Specimen_Test_2'
    sp.samplingTime = "2014-08-22T00:00:00.000-00:00"
    sp.stype = "water bottle"
    
#    sp.samplingLocation.id = "3122765f-cbaf-4234-aaeb-6dcebd9bbfbc"
    
    sl = wqxLib.samplinglocations.getSamplingLocation('SL_002_WXBO')
    sp.samplingLocation = sl
    
    sid = api.postData(sp.toDict(), 'specimens')
    print sid
            
#========================================================================= 

def testProjectActivity1():
    proj = wqxLib.projects.getProject('Project_Test_1')
    acts = []
    
    if proj is not None:          
        aid = wqxLib.activities.getActivity("Activity_test_1")
        if aid is not None:
            acts.append(aid)
        aid = wqxLib.activities.getActivity("Activity_test_2")
        if aid is not None:
            acts.append(aid)        
        aid = wqxLib.activities.getActivity("Activity_test_3")
        if aid is not None:
            acts.append(aid)
    
        result = proj.addActivities(acts)
        print result
        
#========================================================================= 

def testProjectActivity2():
    proj = wqxLib.projects.getProject('Project_Test_2')
    acts = []
    
    if proj is not None:          
        aid = wqxLib.activities.getActivity("Activity_test_1")
        if aid is not None:
            acts.append(aid)
    
        result = proj.addActivities(acts)
        print result
        
#========================================================================= 

def testObservation1():    
    # using specimen, not sampling location
    # in this version, the Observation is created first,
    # then specimens and observed properties are added after

    obs = wqxLib.observations.cObservation()
    obs.customId = 'Observation_Test_1'
    obs.dataClassification = 'LAB'
    obs.medium = 'WATER'
    obs.observedTime = '2014-08-21T00:00:00.000-07'
    obs.resultTime = '2014-08-23T00:00:00.000-07'

    op = wqxLib.observedProperties.getObservedProperty('OP_Water_Temp')       
    obs.observedProperty = op
                             
    sl = wqxLib.specimens.getSpecimen('Specimen_Test_1')
    obs.specimen = sl
            
    sid = api.postData(obs.toDict(), 'observations')
    print sid
        
#=========================================================================

def testObservation2():    
    # using sampling location, not specimen
    # in this version, the observation properties and sampling locations are created
    # at the same time as the observation
    
    obs = wqxLib.observations.cObservation()
    obs.customId = 'Observation_Test_2'
    obs.dataClassification = 'SENSOR'
    obs.medium = 'WATER'
    obs.observedTime = '2014-08-23T00:00:00.000-07'
    obs.resultTime = '2014-08-23T00:00:00.000-07'    

    op = wqxLib.observedProperties.getObservedProperty('OP_Water_Temp')       
    obs.observedProperty = op

    sl = wqxLib.samplinglocations.getSamplingLocation('SL_002_WXBO')
    obs.samplingLocation = sl    
    
    res = wqxLib.results.getResult('Result_Test_1')
    obs.results.append(res)
    
    res = wqxLib.results.getResult('Result_Test_2')
    obs.results.append(res)
        
    sid = api.postData(obs.toDict(), 'observations')
    print sid

#=========================================================================

def testObservation3():    
    # using sampling location, not specimen
    # in this version, the observation properties and sampling locations are created
    # at the same time as the observation
    
    obs = wqxLib.observations.cObservation()
    obs.customId = 'Observation_Test_3'
    obs.dataClassification = 'LAB'
    obs.medium = 'WATER'
    obs.observedTime = '2014-08-24T00:00:00.000-07'
    obs.resultTime = '2014-08-24T00:00:00.000-07'    

    op = wqxLib.observedProperties.getObservedProperty('OP_Water_Temp')       
    obs.observedProperty = op

    sl = wqxLib.specimens.getSpecimen('Specimen_Test_1')
    obs.specimen = sl
    
    res = wqxLib.results.getResult('Result_Test_3')
    obs.results.append(res)
           
    sid = api.postData(obs.toDict(), 'observations')
    print sid
    
#=========================================================================       
        
def testActivityObservation1():
    act = wqxLib.activities.getActivity('Activity_Test_1')
    
    if act is not None:    
        obs1 = wqxLib.observations.getObservation('Observation_Test_1')
        obs2 = wqxLib.observations.getObservation('Observation_Test_2')

        if obs1 is not None:
            act.observations.append(obs1.id)
            
        if obs2 is not None:
            act.observations.append(obs2.id)
            
        sid = api.putData(act.toDict(), 'activities', act.id)
        print sid

#=========================================================================
        
def testActivityObservation2():
    act = wqxLib.activities.getActivity('Activity_Test_2')
    
    if act is not None:    
        obs1 = wqxLib.observations.getObservation('Observation_Test_1')
        obs2 = wqxLib.observations.getObservation('Observation_Test_3')

        if obs1 is not None:
            act.observations.append(obs1.id)
            
        if obs2 is not None:
            act.observations.append(obs2.id)
            
        sid = api.putData(act.toDict(), 'activities', act.id)
        print sid

#=========================================================================
    
def deleteAllTestsAuto():
    #-------------------------------------------------------------------------      
    allact =  wqxLib.apiMethods.getData('projects')   
    for obj in json.loads(allact):
        sid = obj['id']
        
        r = api.deleteData('projects', sid)        
        print r
    #-------------------------------------------------------------------------      
    allact =  wqxLib.apiMethods.getData('activities')   
    for obj in json.loads(allact):
        sid = obj['id']
        
        r = api.deleteData('activities', sid)        
        print r
    #-------------------------------------------------------------------------      
    allact =  wqxLib.apiMethods.getData('observations')   
    for obj in json.loads(allact):
        sid = obj['id']
        
        r = api.deleteData('observations', sid)        
        print r
    #-------------------------------------------------------------------------      
    allact =  wqxLib.apiMethods.getData('specimens')   
    for obj in json.loads(allact):
        sid = obj['id']
        
        r = api.deleteData('specimens', sid)        
        print r
    #-------------------------------------------------------------------------      
    allact =  wqxLib.apiMethods.getData('samplinglocations')   
    for obj in json.loads(allact):
        sid = obj['id']
        
        r = api.deleteData('samplinglocations', sid)        
        print r
    #-------------------------------------------------------------------------      
    allact =  wqxLib.apiMethods.getData('results')   
    for obj in json.loads(allact):
        sid = obj['id']
        
        r = api.deleteData('results', sid)        
        print r
    #-------------------------------------------------------------------------      
    allact =  wqxLib.apiMethods.getData('observedproperties')   
    for obj in json.loads(allact):
        sid = obj['id']
        
        r = api.deleteData('observedproperties', sid)        
        print r        
        
    
#=========================================================================        
    
if __name__ == '__main__':
    errors = 0
    
    # Just for debugging purposes.
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('requests').setLevel(logging.DEBUG)    

    deleteAllTestsAuto()

    testResult1()
    testResult2()
    testResult3()
    testSampleLocation1()
    testSampleLocation2()
    testObservedProperty()
    testSpecimen1()
    testSpecimen2()
    testObservation1()
    testObservation3()
    testObservation2()
    testActivity1()
    testActivity2()
    testActivity3()
    testActivityObservation1()
    testActivityObservation2()
    testProject1()
    testProject2()
    testProjectActivity1()
    testProjectActivity2()
    
    # deleteAllTestsAuto()

    print api.getData('results')
    print api.getData('specimens')
    print api.getData('samplinglocations')
    print api.getData('observedproperties')    
    print api.getData('observations') 
    print api.getData('activities')    
    print api.getData('projects')         
    
    
    
    