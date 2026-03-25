ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Sorted ages:", ages)
print("Min age:", ages[0], " Max age:", ages[-1])
adheririr = [ages[0], ages[-1]]
ages.extend(adheririr)
ages.sort()
ages_mean= sum(ages) / len(ages)
print("Mean age:", ages_mean)
rango = ages[-1] - ages[0]
print("Range of ages:", rango)
min_promedio = abs(ages[0] - ages_mean)
max_promedio = abs(ages[-1] - ages_mean)
print("diferencia entre minimo menos promedio y maximo menos promedio:", abs(min_promedio - max_promedio))


