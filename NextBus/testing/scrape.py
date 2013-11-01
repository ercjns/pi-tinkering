import urllib.request
    
class obaSign:
    def __init__(self, url, route):
        self.url = url
        self.route_name = route
        self.arrivals = []
        
    def update(self):
        self.arrivals = []
        sign = urllib.request.urlopen(self.url)
        sign = sign.read().decode('utf-8')
        entries = sign.split('<tr class="arrivalsRow"')
        entires = entries[1:]
        for bus in entires:
            data = self.get_busdata(bus)
            self.arrivals.append(data)
    
    def get_busdata(self, bus):
        data = bus.split('class="')
        data=data[1:]
        for entry in data:
            if entry.startswith('arrivalsTimeEntry'):
                s = entry.find('>') + 1 
                e = entry.find('<', s)
                time = entry[s:e]
                continue
        return(time)

udist = obaSign('http://pugetsound.onebusaway.org/where/sign/stop.action?id=1_11200&showTitle=false&minutesBefore=1&route=1_49', '49>UDistrict')

downtown = obaSign('http://pugetsound.onebusaway.org/where/sign/stop.action?id=1_11040&showTitle=false&minutesBefore=1&route=1_49', '49>Downtown')

seacenter = obaSign('http://pugetsound.onebusaway.org/where/sign/stop.action?id=1_29264&showTitle=false&minutesBefore=1&route=1_8', '8>SeaCenter')

montlake = obaSign('http://pugetsound.onebusaway.org/where/sign/stop.action?id=1_29252&showTitle=false&minutesBefore=1&route=1_43', '43>Montlake')

redmond = obaSign('http://pugetsound.onebusaway.org/where/sign/stop.action?id=1_13460&showTitle=false&minutesBefore=1&route=40_545', '545>Redmond')

myroutes = [udist, downtown, seacenter, montlake, redmond]

for route in myroutes:
    route.update()
    print(route.route_name)
    print(route.arrivals)
