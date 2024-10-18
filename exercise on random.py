import random 
import statistics
random_integers = [random.randint(1, 50) for _ in range(100)]
print(f"random integers are:{random_integers}")
mean = statistics.mean(random_integers)
median = statistics.median(random_integers)
mode = statistics.mode(random_integers)
std_dev = statistics.stdev(random_integers)
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev}")