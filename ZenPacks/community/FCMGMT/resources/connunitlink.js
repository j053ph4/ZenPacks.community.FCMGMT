
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
    
    ZC.connUnitLinkPanel = Ext.extend(ZC.ComponentGridPanel, {
        constructor: function(config) {
            config = Ext.applyIf(config||{}, {
                componentType: 'connUnitLink',
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
                        "name": "getCunitdeviceLink"
                    }, 
                    {
                        "name": "getFromunitLink"
                    }, 
                    {
                        "name": "getLinkType"
                    }, 
                    {
                        "name": "getTounitLink"
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
                        "header": "To Device", 
                        "renderer": "pass_link", 
                        "id": "getCunitdeviceLink", 
                        "dataIndex": "getCunitdeviceLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "From Unit", 
                        "renderer": "pass_link", 
                        "id": "getFromunitLink", 
                        "dataIndex": "getFromunitLink"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "Link Type", 
                        "renderer": "pass_link", 
                        "id": "getLinkType", 
                        "dataIndex": "getLinkType"
                    }, 
                    {
                        "sortable": "true", 
                        "width": 120, 
                        "header": "To Unit", 
                        "renderer": "pass_link", 
                        "id": "getTounitLink", 
                        "dataIndex": "getTounitLink"
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
            ZC.connUnitLinkPanel.superclass.constructor.call(this, config);
        }
    });
    
    Ext.reg('connUnitLinkPanel', ZC.connUnitLinkPanel);
    ZC.registerName('connUnitLink', _t('Connectivity Unit Link'), _t('Connectivity Units Links'));
    
    })();

