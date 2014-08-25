# -*- coding: utf-8 -*-
# http://docs.python-requests.org/en/latest/user/quickstart/
#========================================================================= 
# BBALEY/Automated Control Systems, Inc. 08-25-2014
# Aquatic Informatics (WQX) Water Quality data interface / API client
#========================================================================= 

import json
import requests
#========================================================================= 

errors = 0
url = 'https://usace.gaiaserve.net'
authToken = "4d331524a58fca12168c0a48a4ae5bdd"
hdrs = {'Authorization': 'token ' + authToken, 'Content-Type': 'application/json'}
#========================================================================= 
    
def getData(_interface):   
    uri = url + u'/api/v1/%s' %_interface
       
    req = requests.get(uri, headers=hdrs)     
    
    response = req.text
    #print response
    
    if (response == 'Token is invalid.'):
        print 'error : ' + response   
    #else:
    #    for jo in json.loads(response):
    #        # print jo
    #        print json.dumps(jo, sort_keys = False, indent = 4)
            
    return response
                    
#=========================================================================         
def deleteData(_interface, _id ):
    global errors
    
    uri = url + '/api/v1/%s/%s' % (_interface, _id)
    
    try:
        req = requests.delete(uri, headers=hdrs)              
        response = req.text
        #print response
        
        if (response is not None): # or (req.status_code != 204):               
            #print 'response : ' + str(req.status_code)
        
                    
            if req.status_code == 204:
                return '[DELETE] successful : ' + str(req.status_code)
            elif req.status_code == 500:
                return '[DELETE] item not found : ' + str(req.status_code)
            elif req.status_code == 401:
                return '[DELETE] operation not permitted : ' + str(req.status_code) + "\\r\\n" + response
            else:
                return '[DELETE] response : ' + str(req.status_code) + "\\r\\n" + response
            
    except Exception, e:
        if str(e) == '204':
            return '[DELETE] successful : ' + str(req.status_code) 
        else:    
            errors += 1
            print e
            print 'exception : ' + str(req.status_code)
            err = 'error: ' + str(e) + "\\r\\n" + '[DELETE] : ' + str(req.status_code) + "\\r\\n" + response
            return err   
        
#=========================================================================         
        
def putData(_wqxobj, _interface, _id ):
    global errors
    
    uri = url + '/api/v1/%s/%s' % (_interface, _id)
    
    payload = _wqxobj    
    #print '#======================= PAYLOAD =========================== #'
    #print payload
    #print '#==================== ENDPAYLOAD =========================== #'
    
    try:
        req = requests.put(uri, data=json.dumps(payload), headers=hdrs)              
        response = req.text
        #print response
        
        if (response == 'Token is invalid.'):
            print 'error : ' + response
            
        if "gaia.domain.exceptions.NotUniqueException" in response:
            return "error: %s is not unique!"  %_interface
        else:    
            rj = req.json()
            print rj    
         
            _id = rj['id']

            return _id
    except Exception, e:
        errors += 1
        #print e
        err = 'error: ' + str(e)
        return err   
            
    
#========================================================================= 
        
def postData(_wqxobj, _interface ):
    global errors
    
    uri = url + u'/api/v1/%s' %_interface
    hdrs = {'Authorization': 'token ' + authToken, 'Content-Type': 'application/json'}
    
    payload = _wqxobj   # _wqxobj.toDict()
    #print '#======================= PAYLOAD =========================== #
    #print payload
    #print '#==================== ENDPAYLOAD =========================== #
    
    try:
        req = requests.post(uri, data=json.dumps(payload), headers=hdrs)              
        response = req.text
        
        if (response == 'Token is invalid.'):
            print 'error : ' + response
            
        if "gaia.domain.exceptions.NotUniqueException" in response:
            return "error: %s is not unique!"  %_interface
        else:    
            rj = req.json()
            #print rj    
         
            _id = rj['id']

            return _id
    except Exception, e:
        errors += 1
        #print e
        err = 'error: ' + str(e)
        return err   
            
    
