
(function(){
    var ZC = Ext.ns('Zenoss.component');

    function render_link(ob) {
        if (ob && ob.uid) {
            return Zenoss.render.link(ob.uid);
        } else {
            return ob;
        }
    }
    
    function pass_link(ob){ 
        return ob; 
    }
    
    ZC.connUnitPortPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'connUnitPort',
                autoExpandColumn: 'name', 
                fields:                 [
                    {
                        "name": "uid"
                    }, 
                    {
                        "name": "severity"
                    }, 
                    {
                        "name": "status"
                    }, 
                    {
                        "name": "name"
                    }, 
                    {
                        "name": "connUnitPortModuleType"
                    }, 
                    {
                        "name": "connUnitPortTransmitterType"
                    }, 
                    {
                        "name": "connUnitPortType"
                    }, 
                    {
                        "name": "getCunitLink"
                    }, 
                    {
                        "name": "getCunitportdeviceLink"
                    }, 
                    {
                        "name": "getPortHwState"
                    }, 
                    {
                        "name": "getPortState"
                    }, 
                    {
                        "name": "getPortStatus"
                    }, 
                    {
                        "name": "usesMonitorAttribute"
                    }, 
                    {
                        "name": "monitor"
                    }, 
                    {
                        "name": "monitored"
                    }, 
                    {
                        "name": "locking"
                    }
                ]
,
                columns:                [
                    {
                        "sortable": "true", 
                        "width": 50, 
                        "header": "Events", 
                        "renderer": Zenoss.render.severity, 
                        "id": "severity", 
                        "dataIndex": "severity"
                    }, 
                    {
                        "header": "Name", 
                        "width": 70, 
                        "sortable": "true", 
                        "id": "name", 
                        "dataIndex": "name"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "connUnitPortModuleType", 
                        "renderer": "pass_link", 
                        "id": "connUnitPortModuleType", 
                        "dataIndex": "connUnitPortModuleType"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "connUnitPortTransmitterType", 
                        "renderer": "pass_link", 
                        "id": "connUnitPortTransmitterType", 
                        "dataIndex": "connUnitPortTransmitterType"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "connUnitPortType", 
                        "renderer": "pass_link", 
                        "id": "connUnitPortType", 
                        "dataIndex": "connUnitPortType"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Connectivity Unit", 
                        "renderer": "pass_link", 
                        "id": "getCunitLink", 
                        "dataIndex": "getCunitLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "To Device", 
                        "renderer": "pass_link", 
                        "id": "getCunitportdeviceLink", 
                        "dataIndex": "getCunitportdeviceLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Port HW State", 
                        "renderer": "pass_link", 
                        "id": "getPortHwState", 
                        "dataIndex": "getPortHwState"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Port State", 
                        "renderer": "pass_link", 
                        "id": "getPortState", 
                        "dataIndex": "getPortState"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Port Status", 
                        "renderer": "pass_link", 
                        "id": "getPortStatus", 
                        "dataIndex": "getPortStatus"
                    }, 
                    {
                        "header": "Monitored", 
                        "width": 65, 
                        "sortable": "true", 
                        "id": "monitored", 
                        "dataIndex": "monitored"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 65, 
                        "header": "Locking", 
                        "renderer": Zenoss.render.locking_icons, 
                        "id": "locking", 
                        "dataIndex": "locking"
                    }
                ]

            });
            ZC.connUnitPortPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('connUnitPortPanel', ZC.connUnitPortPanel);
    ZC.registerName('connUnitPort', _t('Connectivity Unit Port'), _t('Connectivity Unit Ports'));
    
    })();

