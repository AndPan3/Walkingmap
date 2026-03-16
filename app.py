from geopy.geocoders import Nominatim
import time
import cartons
import webbrowser
from branca.element import Element

#Adres-Coords
geolocator = Nominatim(user_agent= "YOUR_USER_AGENT")

print("type location 1")
address1 = input()
z = geolocator.geocode(address1)

if z is None:
    print("could not find adress, please try again, reccomended formatting is, Street, Housenumber, City, Country")
    address1=input()
    z= geolocator.geocode(address1)
    if z is None:
        print("Sorry, there is a problem with the Address, it may be beacouse of bad formatting or the Adress dosen't exist in th OpenStreetMap Database")
        exit()
        
time.sleep(1)

print("type location 2")
address2 = input()
q = geolocator.geocode(address2)

if q is None:
    print("could not find address, please try again, reccomended formatting is, Street, Housenumber, City, Country")
    address2=input()
    q=geolocator.geocode(address2)
    if q is None:
        print("Sorry, there is a problem with the Address, it may be beacouse of bad formatting or the Adress dosen't exist in th OpenStreetMap Database")
        exit()
time.sleep(1)
#route
startlon = z.longitude
startlat = z.latitude
endlon = q.longitude
endlat = q.latitude

route=cartons.get_route("YOUR_BASE_URL", startlon,startlat,endlon,endlat,transport="foot")


coords= route.geometry
duration=route.duration / 60, 1
distance=route.distance / 1000
#map
swappedcords = [(lon, lat) for lat, lon in coords]
html = "<h1>Hello Map</h1>"
map_route = cartons.fastdraw(swappedcords,"red","5",tiles="CartoDB Positron",attribution="© CartoDB Positron",)
#html
html = html = f"""
<div style="position:fixed; top:50px; left:50px; background:white;">
<ul>
    <li>Distance = {distance:.2f} km</li>
    <li>Duration = {duration:.2f} min</li>
</ul>
</div>
"""
map_route.get_root().html.add_child(Element(html))

filename = "route.html"
map_route.save(filename)
webbrowser.open(filename)

