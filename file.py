from geopy.geocoders import Nominatim
import time
import cartons
import webbrowser

#Adres-Coords
geolocator = Nominatim(user_agent= "AndPan3_WalkingAPP")

print("type location 1")
adress1 = input()
z = geolocator.geocode(adress1)

if z is None:
    print("could not find adress, please try again, reccomended formatting is, Street, Housenumber, City, Country")
    adress1=input()
    z= geolocator.geocode(adress1)
    if z is None:
        print("Sorry, there is a problem with the Adress, it may be beacouse of bad formatting or the Adress dosen't exist in th OpenStreetMap Database")
        exit()
        
time.sleep(1)

print("type location 2")
adress2 = input()
q = geolocator.geocode(adress2)

if q is None:
    print("could not find adress, please try again, reccomended formatting is, Street, Housenumber, City, Country")
    adress2=input()
    q=geolocator.geocode(adress2)
    if q is None:
        print("Sorry, there is a problem with the Adress, it may be beacouse of bad formatting or the Adress dosen't exist in th OpenStreetMap Database")
        exit()
time.sleep(1)
#route
startlon = z.longitude
startlat = z.latitude
endlon = q.longitude
endlat = q.latitude

route=cartons.get_route("https://router.project-osrm.org", startlon,startlat,endlon,endlat,"foot")


coords= route.geometry
duration=route.duration
distance=route.distance
#map
map_route = cartons.fastdraw(coords,"red","5","OpenStreetMap")
#NEXT: einbindne duration and distance in map (map is folium)
filename = "route.html"
map_route=filename
webbrowser.open(filename)

