from adapters.dimmable_bulb_adapter import DimmableBulbAdapter
from adapters.dimmable_ct_bulb_adapter import DimmableCtBulbAdapter
from adapters.on_off_switch_adapter import OnOffSwitchAdapter


icasa_adapters = {
    'ICZB-IW11D': DimmableBulbAdapter,  # iCasa Zigbee 3.0 Dimmer
    'ICZB-IW11SW': OnOffSwitchAdapter,  # iCasa Zigbee 3.0 Switch
    'ICZB-B1FC60/B3FC64/B2FC95/B2FC125': DimmableCtBulbAdapter, # iCasa Zigbee 3.0 Filament Lamp 60/64/95/125 mm
    'ICZB-R11D': DimmableBulbAdapter    # iCasa Zigbee AC dimmer
}
