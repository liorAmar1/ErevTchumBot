
# MESSGAGE_FORMATS
ADD_STATION = u'add s (?P<param1>.*)'
RM_STATION = u'rm s (?P<param1>.*)'
ADD_GROUP = u'add g (?P<param1>.*)'
RM_GROUP = u'rm g (?P<param1>.*)'
BUSY_STATION = u'(?P<param1>.*) in (?P<param2>.*)'
FREE_STATION = u'(?P<param1>.*) free'
GROUP_GO_TO = u'(?P<param1>.*) go (?P<param2>.*)'


CURRENT_STATE = u"Free:\n{free}\nBusy:\n{busy}\n"
STATION_STATE = u"{name}: group:{group} waits:{waits}"

class Station(object):
    def __init__(self, name):
        self.name = name
        self.waits = []
        self.group = None

    def __repr__(self):
        return STATION_STATE.format(name=self.name, group=self.group, waits=', '.join(self.waits))

    def is_free(self):
        return (self.group == None) and (not len(self.waits))

stations = {}
groups = []

def add_station(station=None):
	assert station, "Missing station name"
	stations[station] = Station(station)

def rm_station(station=None):
	assert station, "Missing station name"
	stations.pop(station)

def add_group(group=None):
	assert group, "Missing group id"
	groups.append(group)

def rm_group(group=None):
	assert group, "Missing group id"
	groups.remove(group)

def busy_station(station=None, group=None):
	assert group, "Missing group id"
	assert station, "Missing station name"
	assert station in stations, "Wrong station name"
	assert groups.count(group) == 1, "Wrong group id"
	stations[station].group = group

def free_station(station=None):
	assert station, "Missing station name"
	assert station in stations, "Wrong station name"
	stations[station].group = None

def go_to_station(group=None, station=None):
	assert group, "Missing group id"
	assert station, "Missing station name"
	assert station in stations, "Wrong station name"
	assert groups.count(group) == 1, "Wrong group id"
	old_station = [stations[s] for s in stations if stations[s].group == group]
	if any(old_station):
		for s in old_station:
			s.group=None
	stations[station].waits.append(group)
