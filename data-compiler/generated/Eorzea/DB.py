# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Eorzea

import flatbuffers

class DB(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDB(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DB()
        x.Init(buf, n + offset)
        return x

    # DB
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DB
    def GatheringItems(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .GatheringItem import GatheringItem
            obj = GatheringItem()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # DB
    def GatheringItemsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # DB
    def FishingItems(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .FishingItem import FishingItem
            obj = FishingItem()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # DB
    def FishingItemsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # DB
    def WeatherMaps(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .WeatherMap import WeatherMap
            obj = WeatherMap()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # DB
    def WeatherMapsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def DBStart(builder): builder.StartObject(3)
def DBAddGatheringItems(builder, gatheringItems): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(gatheringItems), 0)
def DBStartGatheringItemsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def DBAddFishingItems(builder, fishingItems): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fishingItems), 0)
def DBStartFishingItemsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def DBAddWeatherMaps(builder, weatherMaps): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(weatherMaps), 0)
def DBStartWeatherMapsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def DBEnd(builder): return builder.EndObject()
