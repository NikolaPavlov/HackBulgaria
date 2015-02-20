import math

# Problem 1
def calc_tetrahedron_volume(a):
	v = (math.sqrt(2) / 12) * math.pow(a, 3)
	v /= 1000
	return round(v, 2)

print calc_tetrahedron_volume(100)
print calc_tetrahedron_volume(119)
print calc_tetrahedron_volume(30)

# Problem 2
def calc_tetrahedron_filled(tetrahedrons, liters):
	count = 0
	tetrahedrons.sort()
	for tetrahedron in tetrahedrons:
		liters -= calc_tetrahedron_volume(tetrahedron)
		if (liters >= 0):
			count += 1
		else:
			break
	return count

print calc_tetrahedron_filled([100, 20, 30], 10)
print calc_tetrahedron_filled([30, 31, 30], 10)
print calc_tetrahedron_filled([999, 111, 43], 10)
