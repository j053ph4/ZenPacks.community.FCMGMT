from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FCMGMT.Definition import *

__doc__ = """connUnitPortMap

connUnitPortMap detects Conn Unit Ports
This version adds a relation to associated connUnits.

"""


connUnitPortTypeMap = { 1: 'unknown', 2: 'other', 3: 'not-present', 4: 'hub-port', 
                       5: 'n-port', 6: 'l-port', 7: 'fl-port', 8: 'f-port', 
                       9: 'e-port', 10:'g-port', 11: 'domain-ctl', 12: 'hub-controller', 
                       13: 'scsi', 14: 'escon', 15: 'lan', 16: 'wan' , 
                       17: 'ac', 18: 'dc', 19: 'ssa'}

connUnitPortTransmitterTypeMap = {1: 'unknown', 2: 'other', 3: 'unused', 4: 'shortwave',
                                  5: 'longwave', 6: 'copper', 7: 'scsi', 8: 'longwaveNoOFC',
                                  9: 'shortwaveNoOFC', 10: 'longwaveLED', 11: 'ssa'}

connUnitPortModuleTypeMap = {1: 'unknown', 2: 'other', 3: 'gbic', 4: 'embedded',
                                  5: 'glm', 6: 'gbicSerialId', 7: 'gbicNoSerialId', 8: 'gbicNotInstalled',
                                  9: 'smallFormFactor'}


class connUnitPortMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(connUnitPortDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpEntryName = 'connUnitPortEntry'
    snmpEntryOID = '.1.3.6.1.3.94.1.10.1'
    snmpIndexName = 'connUnitPortUnitId'
    snmpTitleName = 'connUnitPortName'

    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.1': snmpIndexName,
            '.2': 'connUnitPortIndex',
            '.3': 'connUnitPortType',
            '.8': 'connUnitPortTransmitterType',
            '.9': 'connUnitPortModuleType',
            '.11': 'connUnitPortFCId',
            '.12': 'connUnitPortSn',
            '.15': 'connUnitPortSpeed',
            '.17': snmpTitleName,
            '.18': 'connUnitPortPhysicalNumber',
            }),
        )
    
    def dotify(self, octets): return ".".join( [ '%d'%(ord(c)) for c in octets ] )
    
    def process(self, device, results, log):
        log.info("Modeler %s processing data for device %s",
            self.name(), device.id)
        getdata, tabledata = results
        maps = []
        rm = self.relMap()
        trunktable = tabledata.get(self.snmpEntryName)
        snmpindex = 1
        for trunk in trunktable.values():
            #log.debug(trunk)
            om = self.objectMap(trunk)
            if trunk['connUnitPortSn'] == '': name = str(snmpindex)
            else: name = "%s" % trunk['connUnitPortSn']#getattr(om, self.connUnitPortSn)
            om.id = self.prepId(name)
            om.title = name
            om.connUnitPortUnitId = self.dotify(om.connUnitPortUnitId)
            om.connUnitPortFCId = self.dotify(om.connUnitPortFCId)
            om.connUnitPortType = connUnitPortTypeMap[trunk['connUnitPortType']]
            om.connUnitPortTransmitterType = connUnitPortTransmitterTypeMap[trunk['connUnitPortTransmitterType']]
            om.connUnitPortModuleType = connUnitPortModuleTypeMap[trunk['connUnitPortModuleType']]
            om.snmpindex = "%s.%s" % ( om.connUnitPortUnitId, om.connUnitPortIndex)
            om.setCunit = om.connUnitPortUnitId
            om.setCunitportdevice = trunk['connUnitPortName']
            rm.append(om)
            log.debug(om)
            snmpindex +=1
        maps.append(rm)
        return maps

