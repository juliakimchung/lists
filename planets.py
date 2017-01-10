planet_list = list()
planet_list = ["Mercury","Venus", "Mars", ]
planet_list.append("Jupiter")
print(planet_list)
planet_list.extend(["Saturn", "Uranus", "Neptune"])
print(planet_list)
planet_list.insert(2,"earth")
print(planet_list)
planet_list.append("pluto")
print(planet_list)
planet_list.pop(2)
print(planet_list)
planet_list.insert(2, "earth")
rocky_planets = planet_list[1:4:2]
print(rocky_planets)
del planet_list[4]
print(planet_list)

planets_visited = [("earth", "me"),("mars", "cassini"), ("mymoon", "you")]
print(planets_visited[2])
for planets in planets_visited:
	for planet in planets:
		print(planet)