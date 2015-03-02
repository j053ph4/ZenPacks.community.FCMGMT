from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin, GetMap, GetTableMap
from Products.DataCollector.plugins.DataMaps import ObjectMap
from ZenPacks.community.FCMGMT.Definition import *

__doc__ = """connUnitSensorMap

connUnitSensorMap detects Conn Unit Sensors
This version adds a relation to associated connUnits.

"""

class connUnitSensorMap(SnmpPlugin):
    """
    """
    compname = "os"
    constr = Construct(connUnitSensorDefinition)
    relname = constr.relname
    modname = constr.zenpackComponentModule
    baseid = constr.baseid

    snmpEntryName = 'connUnitSensorEntry'
    snmpEntryOID = '.1.3.6.1.3.94.1.8.1'
    snmpIndexName = 'connUnitSensorUnitId'
    snmpTitleName = 'connUnitSensorName'

    snmpGetTableMaps = (
        GetTableMap(snmpEntryName, snmpEntryOID, {
            '.1': snmpIndexName,
            '.2': 'connUnitSensorIndex',
            '.3': 'connUnitSensorName',
            '.4': 'connUnitSensorStatus',
            '.5': 'connUnitSensorInfo',
            '.6': 'connUnitSensorMessage',
            '.7': 'connUnitSensorType',
            '.8': 'connUnitSensorCharacteristic',
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
            om = self.objectMap(trunk)
            name = "%s" % getattr(om, self.snmpTitleName)
            om.id = self.prepId(name)
            om.title = name
            om.snmpindex = "%s.%s" % (self.dotify(getattr(om, self.snmpIndexName)), getattr(om, 'connUnitSensorIndex'))
            om.connUnitSensorUnitId = self.dotify(getattr(om, 'connUnitSensorUnitId'))
            om.connUnitSensorIndex = getattr(om, 'connUnitSensorIndex')
            om.connUnitSensorName = getattr(om, 'connUnitSensorName')
            om.connUnitSensorType = getattr(om, 'connUnitSensorType')
            om.connUnitSensorCharacteristic = getattr(om, 'connUnitSensorCharacteristic')
            om.setCunit = om.connUnitSensorUnitId
            rm.append(om)
            log.debug(om)
            #log.debug("om: %s" % om)
        maps.append(rm)
        return maps
