#Prueba de clases y objetos
class estadistica: 
    def __init__(self, numeros= [0,1,2,3,4,5,6,7,8,9]):
        self.numeros = numeros
    def count_numeros(self):
        return len(self.numeros)
    def sum_numeros(self):
        return sum(self.numeros)
    def min_numeros(self):
        return min(self.numeros)
    def max_numeros(self):
        return max(self.numeros)
    def range_numeros(self):
        return max(self.numeros) - min(self.numeros)
    def mean_numeros(self):
        return sum(self.numeros)/len(self.numeros)
    def median_numeros(self):
        sorted_numeros = sorted(self.numeros)
        n = len(sorted_numeros)
        if n % 2 == 0:
            median = (sorted_numeros[n//2 - 1] + sorted_numeros[n//2]) / 2
        else:
            median = sorted_numeros[n//2]
        return median
    def mode_numeros(self):
        from collections import Counter
        count = Counter(self.numeros)
        mode = count.most_common(1)[0][0]
        return mode
    def standard_deviation_numeros(self):
        mean = self.mean_numeros()
        variance = sum((x - mean) ** 2 for x in self.numeros) / len(self.numeros)
        return variance ** 0.5
    def variance_numeros(self):
        mean = self.mean_numeros()
        variance = sum((x - mean) ** 2 for x in self.numeros) / len(self.numeros)
        return variance
    def frequency_distribution_numeros(self):
        from collections import Counter
        count = Counter(self.numeros)
        total = len(self.numeros)
        frequency_distribution = {k: v / total for k, v in count.items()}
        return frequency_distribution

numeros=estadistica([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
print("Count:", numeros.count_numeros())
print("Sum:", numeros.sum_numeros())
print("Min:", numeros.min_numeros())
print("Max:", numeros.max_numeros())
print("Range:", numeros.range_numeros())
print("Mean:", numeros.mean_numeros())
print("Median:", numeros.median_numeros())
print("Mode:", numeros.mode_numeros())
print("Standard Deviation:", numeros.standard_deviation_numeros())
print("Variance:", numeros.variance_numeros())
print("Frequency Distribution:", numeros.frequency_distribution_numeros())
