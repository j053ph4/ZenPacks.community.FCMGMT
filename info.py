from ZenPacks.community.ConstructionKit.ClassHelper import *

def connUnitgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class connUnitInfo(ClassHelper.connUnitInfo):
    ''''''

def connUnitSensorgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class connUnitSensorInfo(ClassHelper.connUnitSensorInfo):
    ''''''

def connUnitLinkgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class connUnitLinkInfo(ClassHelper.connUnitLinkInfo):
    ''''''

def connUnitPortgetEventClassesVocabulary(context):
    return SimpleVocabulary.fromValues(context.listgetEventClasses())

class connUnitPortInfo(ClassHelper.connUnitPortInfo):
    ''''''


