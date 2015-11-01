from collective.geo.geographer.interfaces import IGeoreferenced
from Products.Five.browser import BrowserView
from .geomet import wkt
#from collective.geo.simpleleafletmap.browser.geomet import wkt

class SimpleLeafletMapView(BrowserView):
    """ this will return coordinates, if the current object is georeferenced """
    def __init__(self,context,request):
        self.context = context
        self.request = request
        # request.set('disable_border', True)
    
    def s(self, intup):
        """ returns a WKT point part - no parens"""
        return '{} {}'.format(intup[0], intup[1])
    
    def gc(self, intup):
        return ','.join([self.s(m) for m in intup[0]])
    
    def flip(self, indata):
        return (indata[1],indata[0])
    
    def cg2ll(self, intype, intup):
        if intype == 'Point':
            print intype + '>><<' + str(intup)
            feat = 'L.marker([{}, {}])'.format(intup[1],intup[0])
        
        if intype == 'LineString':
            print intype + '>><<' + str(intup)
            #l = eval(intup)
            t = (str([self.flip(q) for q in intup]).replace('(','[').replace(')',']'))
            feat = 'L.polyline({})'.format(t)
        
        if intype == 'Polygon':
            print intype + '>><<' + str(intup)
            #l = eval(intup)
            t = (str([self.flip(q) for q in intup[0][:-1]]).replace('(','[').replace(')',']'))
            feat = 'L.polygon({})'.format(t)
        
        
        print 'feat is :::::::' + feat
        return 'L.featureGroup([{}])'.format(feat)
  
  
#   def cg2ll(self, intype, intup):
        
#         if intype == 'Point':
#             print intype + '>><<' + str(intup)
#             return 'L.featureGroup([L.marker([{}, {}])])'.format(intup[1],intup[0])
      
    @property    
    def coordinates(self):
        # using the magic of interfaces
        # we retrieve the georeferenced
        # data from our object
        obj = IGeoreferenced(self.context, None) # what other methods does obj get?
        print '>>> ' + str(obj.type) + '::: ' + str(obj.coordinates) + ' <<<'
        #print '>>> ' + str(self.gc(obj.coordinates)) + ' <<<'
        #vwkt = obj.type + '((' + str(self.gc(obj.coordinates)) + '))'
        #need to place the wkt-geojson stuff here
        #print vwkt.upper()
        #return wkt.loads(vwkt.upper())  #obj.get
        return self.cg2ll(obj.type, obj.coordinates)
        
    def js_contextvariables(self):
        # switches the () for []'s
        # making it valid json
        return """<script>var contextvariables = {
                leafletlayer : %s
            }
            </script>""" % str(self.coordinates)
