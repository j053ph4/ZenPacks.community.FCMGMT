from ZenPacks.community.ConstructionKit.BasicDefinition import *
from ZenPacks.community.ConstructionKit.Construct import *

BASE = "FCMGMT"
VERSION = Version(1, 0, 0)

###################### CONN UNIT ####################

# basic function to map RRD value to a status string
def getMapValue(ob, datapoint, map):
    ''' attempt to map number to data dict'''
    try:
        value = int(ob.getRRDValue(datapoint))
        return map[value]
    except:
        return 'unknown'

def getUnitState(ob):  return ob.getMapValue('connUnitState_connUnitState', ob.connUnitStateMap) 
def getUnitStatus(ob):  return ob.getMapValue('connUnitStatus_connUnitStatus', ob.connUnitStatusMap)

connUnitDefinition = type('connUnitDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'connUnit',
        'componentData' : {
                          'singular': 'Connectivity Unit',
                          'plural': 'Connectivity Units',
                          'properties': { 
                                        'connUnitId' : addProperty('connUnitId'),
                                        'connUnitGlobalId' : addProperty('connUnitGlobalId'),
                                        'connUnitType' : addProperty('connUnitType'),
                                        'connUnitNumports' : addProperty('connUnitNumports'),
                                        'connUnitProduct' : addProperty('connUnitProduct'),
                                        'connUnitSn' : addProperty('connUnitSn'),
                                        'connUnitUrl': addProperty('connUnitUrl'),
                                        'connUnitDomainId' : addProperty('connUnitDomainId'),
                                        'connUnitProxyMaster' : addProperty('connUnitProxyMaster'),
                                        'connUnitModuleId' : addProperty('connUnitModuleId'),
                                        'connUnitName' : addProperty('connUnitName'),
                                        'connUnitInfo' : addProperty('connUnitInfo'),
                                        'connUnitControl' : addProperty('connUnitControl'),
                                        'connUnitContact' : addProperty('connUnitContact'),
                                        'getUnitState' : getReferredMethod('Unit State', 'getUnitState'),
                                        'getUnitStatus' : getReferredMethod('Unit Status', 'getUnitStatus'),
                                        },
                          },
        
        'componentAttributes' : {
                                 'connUnitStateMap': { 1: 'unknown', 2: 'online', 3: 'offline'}, 
                                 'connUnitStatusMap': { 1: 'unknown', 2: 'unused', 3: 'ready', 4: 'warning', 5: 'failed'}, 
                                 'statusmap':{
                                                1: ('grey', 0, 'unknown'),
                                                2: ('green', 0, 'unused'),
                                                3: ('green', 0, 'ready'),
                                                4: ('orange', 4, 'warning'),
                                                5: ('red', 5, 'failed'),
                                            }
                                 },
        'componentMethods' : [getMapValue, getUnitState, getUnitStatus],
        }
)

###################### CONN UNIT PORT ####################

def getPortState(ob):  return ob.getMapValue('connUnitPortState_connUnitPortState', ob.connUnitPortStateMap) 
def getPortStatus(ob):  return ob.getMapValue('connUnitPortStatus_connUnitPortStatus', ob.connUnitPortStatusMap)
def getPortHwState(ob):  return ob.getMapValue('connUnitPortHWState_connUnitPortHWState', ob.connUnitPortHWStateMap)
 
connUnitPortStateMap = { 1: 'unknown', 2: 'online', 3: 'offline', 4: 'bypassed', 5: 'diagnostics', }
connUnitPortStatusMap = { 1: 'unknown', 2: 'unused', 3: 'ready', 4: 'warning', 5: 'failure', 6: 'notparticipating', 7: 'initializing', 8: 'bypass', 9: 'ols' }
connUnitPortHWStateMap = { 1: 'unknown', 2: 'failed', 3: 'bypassed', 4: 'active', 5: 'loopback', 6: 'txfault', 7: 'noMedia', 8: 'linkDown',}

statusmap ={1: ('grey', 0, 'unknown'),
            2: ('green', 0, 'unused'),
            3: ('green', 0, 'ready'),
            4: ('orange', 4, 'warning'),
            5: ('red', 5, 'failure'),
            6: ('grey', 0, 'notparticipating'),
            7: ('yellow', 0, 'initializing'),
            8: ('green', 0, 'bypass'),
            9: ('green', 0, 'ols'),
            }

connUnitPortDefinition = type('connUnitPortDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'connUnitPort',
        'componentData' : {
                          'singular': 'Connectivity Unit Port',
                          'plural': 'Connectivity Unit Ports',
                          'properties': { 
                                        'connUnitPortUnitId' : addProperty('connUnitPortUnitId'),
                                        'connUnitPortIndex' : addProperty('connUnitPortIndex'),
                                        'connUnitPortName' : addProperty('connUnitPortName'),
                                        'connUnitPortType' : addProperty('connUnitPortType', optional=False, order=2),
                                        'connUnitPortTransmitterType' : addProperty('connUnitPortTransmitterType', optional=False, order=3),
                                        'connUnitPortModuleType' : addProperty('connUnitPortModuleType', optional=False, order=4),
                                        'connUnitPortFCId' : addProperty('connUnitPortFCId'),
                                        'connUnitPortSn' : addProperty('connUnitPortSn'),
                                        'connUnitPortSpeed' : addProperty('connUnitPortSpeed'),
                                        'connUnitPortPhysicalNumber' : addProperty('connUnitPortPhysicalNumber'),
                                        'getPortState' : getReferredMethod('Port State', 'getPortState'),
                                        'getPortStatus' : getReferredMethod('Port Status', 'getPortStatus'),
                                        'getPortHwState' : getReferredMethod('Port HW State', 'getPortHwState'),
                                        },
                          },
         
        'componentAttributes' : {
                                 'connUnitPortStateMap': connUnitPortStateMap, 
                                 'connUnitPortStatusMap': connUnitPortStatusMap, 
                                 'connUnitPortHWStateMap': connUnitPortHWStateMap,
                                 'statusmap':{1: ('grey', 0, 'unknown'),
                                            2: ('green', 0, 'unused'),
                                            3: ('green', 0, 'ready'),
                                            4: ('orange', 4, 'warning'),
                                            5: ('red', 5, 'failure'),
                                            6: ('grey', 0, 'notparticipating'),
                                            7: ('yellow', 0, 'initializing'),
                                            8: ('green', 0, 'bypass'),
                                            9: ('green', 0, 'ols'),
                                            }
                                    },
        'componentMethods' : [getMapValue, getPortState, getPortStatus, getPortHwState],
        }
)
 
addDefinitionSelfComponentRelation(connUnitPortDefinition, 
                          'cunitports',  ToMany, 'ZenPacks.community.FCMGMT.connUnitPort', 'connUnitPortUnitId',
                          'cunit', ToOne, 'ZenPacks.community.FCMGMT.connUnit','connUnitGlobalId',
                          'Connectivity Unit', 'id')

addDefinitionDeviceRelation(connUnitPortDefinition,
                          'cunitports', ToMany, 'ZenPacks.community.FCMGMT.connUnitPort','connUnitPortName',
                          'cunitportdevice',  ToOne, 'Products.ZenModel.Device', 'id',
                          "To Device")

###################### CONN UNIT SENSOR ####################

def getSensorState(ob): return ob.getMapValue('connUnitSensorStatus_connUnitSensorStatus', ob.sensorStatusMap)
 
# string map of number to status
sensorStatusMap = { 1: 'unknown', 2: 'other', 3: 'ok',  4: 'warning', 5: 'failed' }
# string map number to sensor type
sensorTypeMap = { 1: 'unknown', 2: 'other', 3: 'battery',  4: 'fan', 5: 'power-supply',
                  6: 'transmitter', 7: 'enclosure', 8: 'board', 9: 'receiver' }
 
 
connUnitSensorDefinition = type('connUnitSensorDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'connUnitSensor',
        'componentData' : {
                          'singular': 'Connectivity Unit Sensor',
                          'plural': 'Connectivity Unit Sensors',
                          'properties': { 
                                        'connUnitSensorUnitId' : addProperty('connUnitSensorUnitId'),
                                        'connUnitSensorIndex' : addProperty('connUnitSensorIndex'),
                                        'connUnitSensorName' : addProperty('connUnitSensorName'),
                                        'connUnitSensorType' : addProperty('connUnitSensorType'),
                                        'connUnitSensorCharacteristic' : addProperty('connUnitSensorCharacteristic'),
                                        'getSensorState' : getReferredMethod('Sensor State', 'getSensorState'),
                                        },
                          },
        'componentAttributes' : {'sensorStatusMap': sensorStatusMap,
                                 'sensorTypeMap': sensorTypeMap,
                                 'statusmap':{
                                                1: ('grey', 0, 'unknown'),
                                                2: ('green', 0, 'other'),
                                                3: ('green', 0, 'ok'),
                                                4: ('orange', 4, 'warning'),
                                                5: ('red', 5, 'failed'),
                                            }
                                 },
        'componentMethods' : [getMapValue, getSensorState]
        }
)
 
addDefinitionSelfComponentRelation(connUnitSensorDefinition, 
                          'cunitsensors',  ToMany, 'ZenPacks.community.FCMGMT.connUnitSensor', 'connUnitSensorUnitId',
                          'cunit', ToOne, 'ZenPacks.community.FCMGMT.connUnit','connUnitGlobalId',
                          'Connectivity Unit', 'id')
 
###################### CONN UNIT LINK ####################
linkTypeMap = { 1: 'unknown', 2: 'other', 3: 'hub',  4: 'switch', 5: 'gateway',
            6: 'converter', 7: 'hba', 8: 'proxyAgent', 9: 'storeageDevice', 10:'host', 
            11:'storageSubsystem', 12:'module', 13:'swDriver', 14:'storageAccessDevice' }

def getLinkType(ob):  
    try: return ob.linkTypeMap[ob.connUnitLinkUnitTypeY]
    except: return ob.linkTypeMap[1]
    
connUnitLinkDefinition = type('connUnitLinkDefinition', (BasicDefinition,), {
        'version' : VERSION,
        'zenpackbase': BASE,
        'component' : 'connUnitLink',
        'componentData' : {
                          'singular': 'Connectivity Unit Link',
                          'plural': 'Connectivity Units Links',
                          'properties': { 
                                        'connUnitLinkUnitId' : addProperty('connUnitLinkUnitId'),
                                        'connUnitLinkIndex' : addProperty('connUnitLinkIndex'),
                                        'connUnitLinkNodeIdX' : addProperty('connUnitLinkNodeIdX'),
                                        'connUnitLinkPortNumberX' : addProperty('connUnitLinkPortNumberX'),
                                        'connUnitLinkPortWwnX' : addProperty('connUnitLinkPortWwnX'),
                                        'connUnitLinkNodeIdY' : addProperty('connUnitLinkNodeIdY'),
                                        'connUnitLinkPortWwnY' : addProperty('connUnitLinkPortWwnY'),
                                        'connUnitLinkPortNumberY' : addProperty('connUnitLinkPortNumberY'),
                                        'connUnitLinkAgentAddressY' : addProperty('connUnitLinkAgentAddressY'),
                                        'connUnitLinkAgentAddressTypeY' : addProperty('connUnitLinkAgentAddressTypeY'),
                                        'connUnitLinkAgentPortY' : addProperty('connUnitLinkAgentPortY'),
                                        'connUnitLinkUnitTypeY' : addProperty('connUnitLinkUnitTypeY'),
                                        'connUnitLinkConnIdY' : addProperty('connUnitLinkConnIdY'),
                                        'getLinkType' : getReferredMethod('Link Type', 'getLinkType'),
                                        },
                          },
        'componentAttributes' : {'linkTypeMap': linkTypeMap,},
        'componentMethods' : [getLinkType]
        }
)
 
addDefinitionDeviceRelation(connUnitLinkDefinition,
                          'cunitlinks', ToMany, 'ZenPacks.community.FCMGMT.connUnitLink','connUnitLinkAgentAddressY',
                          'cunitdevice',  ToOne, 'Products.ZenModel.Device', 'manageIp',
                          "To Device")
 
addDefinitionAnyComponentRelation(connUnitLinkDefinition,
                          'tolinks', ToMany, 'ZenPacks.community.FCMGMT.connUnitLink','connUnitLinkNodeIdY',
                          'tounit',  ToOne, 'ZenPacks.community.FCMGMT.connUnit', 'connUnitGlobalId',
                          "To Unit", 'title')
 
addDefinitionAnyComponentRelation(connUnitLinkDefinition,
                            'fromlinks', ToMany, 'ZenPacks.community.FCMGMT.connUnitLink','connUnitLinkNodeIdX',
                            'fromunit',  ToOne, 'ZenPacks.community.FCMGMT.connUnit', 'connUnitGlobalId',
                            'From Unit', 'title')


