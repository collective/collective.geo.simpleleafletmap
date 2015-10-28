from collective.geo.geographer.interfaces import IGeoreferenced
from Products.Five.browser import BrowserView

class SimpleLeafletMapView(BrowserView):
    """ this will return coordinates, if the current object is georeferenced """
    def __init__(self,context,request):
        self.context = context
        self.request = request
        request.set('disable_border', True)
        
    @property    
    def coordinates(self):
        # using the magic of interfaces
        # we retrieve the georeferenced
        # data from our object
        obj = IGeoreferenced(self.context, None)
        return obj.coordinates
        
    def js_contextvariables(self):
        # switches the () for []'s
        # making it valid json
        return """<script>window.contextvariables = {
                polygon : '%s'
            }
            </script>""" % str(self.coordinates)[1:-1].replace('(','[').replace(')',']')[:-1]