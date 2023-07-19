def tower_of_hanoi(n, source, aux, target):
 	if n > 0:
 		tower_of_hanoi(n-1, source, target, aux)

 		print(f"Move disk {n} from {source} to {target}")

 		tower_of_hanoi(n-1, aux, source, target)


tower_of_hanoi(3, 'A', 'B', 'C')
