import astropy.coordinates


'''
Class that contains the data for a single stellar entity. 

Given a name, it will attempt to discover the coordinates of the entity from astropy.
# TODO ask if the things we care about are going to be in astropy or we need to look them up ourselves
# TODO discover if there's settings astropy will want

'''
class Target(Object):
    def __init__(self, name):
        self.name = name
        # TODO Figure out what from_name() actually returns
        # If it's none or something check for that instead of try/except
        try:
            self._position = coordinates.ICRS.from_name(name)
        except:
            raise ValueError(f'No coordinates found in astropy ICRS for object <{name}>')
    
    @attribute
    def position(self):
        return (self._position.ra.dagree, self._position.dec.degree)
        
    def __str__(self):
        pos = self.position
        return f'<self.name> at <{pos[0]}, {pos[1]}>'

class Procedure(Object):
    def __init__(self, filter, exposureTime, numExposures):
        # Aren't there two filter wheels?
        self.filter = filter
        self.exposureTime = exposureTime
        self.numExposures = numExposures
        
    def __str__(self):
        # TODO change exposureTime-seconds to something that will return time and units
        # TODO figure out what the filters are based on the letters
        return f'{self.numExposures} {self.exposureTime}-second exposures with {self.filter} filter'