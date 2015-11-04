from collective.geo.geographer.interfaces import IGeoreferenced
from Products.Five.browser import BrowserView

class SimpleLeafletMapView(BrowserView):
    """ this will return a leaflet featureGroup, if the current object is 
    georeferenced """
    def __init__(self,context,request):
        self.context = context
        self.request = request

    def flip(self,data):
        return data[::-1]

    def collective_geo_to_leaflet(self, intype, intup):
        if intype == 'Point':
            feat = 'L.marker([{0}, {1}])'.format(intup[1],intup[0])
        
        if intype == 'LineString':
            flipped = [self.flip(coord_set) for coord_set in intup]
            feat = str(flipped).replace('(','[').replace(')',']')
            feat = 'L.polyline({0})'.format(feat)
        
        if intype == 'Polygon':
            flipped = [self.flip(coord_set) for coord_set in intup[0][:-1]]
            feat = str(flipped).replace('(','[').replace(')',']')
            feat = 'L.polygon({0})'.format(feat)
        
        return 'L.featureGroup([{0}])'.format(feat)
  
  

    @property    
    def coordinates(self):
        # using the magic of interfaces
        # we retrieve the georeferenced
        # data from our object
        obj = IGeoreferenced(self.context, None) 
        return self.collective_geo_to_leaflet(obj.type, obj.coordinates)
        
    def js_contextvariables(self):
        js = "<script>var contextvariables = {{leafletlayer : {}}};</script>"
        return js.format(self.coordinates)
