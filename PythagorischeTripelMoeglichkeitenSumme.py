def find_pythagorean_triplets(max_sum):
	"""Liefert alle Tripel (x, y, z) mit x < y < z, x**2 + y**2 = z**2 und x + y + z <= max_sum."""
	

	triplets = []

	for x in range(1, max_sum - 1):
		for y in range(x + 1, max_sum):
			z_sq = x * x + y * y
			z = int(z_sq**0.5)

			# z muss ganzzahlig sein und die Summe darf die Schranke nicht überschreiten
			if z * z == z_sq and z > y and x + y + z <= max_sum:
				triplets.append((x, y, z))

	return triplets


def main():
	max_sum_eingabe=input ("Maximale Summe der Zahlen ist: ")
	
	max_sum=int (max_sum_eingabe)
	triplets = find_pythagorean_triplets(max_sum)

	if not triplets:
		print("Keine Tripel gefunden.")
		return

	print(f"Pythagoreische Tripel mit Summe <= {max_sum}:")
	for i, (x, y, z) in enumerate(triplets, start=1):
		print(f"{i:2d}: ({x}, {y}, {z})  Summe={x + y + z}  Produkt={x * y * z}")


if __name__ == "__main__":
	main()
