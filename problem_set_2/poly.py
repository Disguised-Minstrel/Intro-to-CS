def evaluate_poly(poly, x):
    if len(poly) == 1:
        return poly[0]
    return evaluate_poly(poly[:-1], x) + (x**(len(poly)-1))*poly[-1]

def compute_deriv(poly):
    if len(poly) == 0:
        return 0
    deriv = tuple()
    for i in range(len(poly)):
        if i == 0:
            continue
        deriv = deriv + (i*poly[i],)
    return deriv

def compute_root(poly, guess, epsilon):
    no_of_guesses = 0
    deriv = compute_deriv(poly)
    while not (evaluate_poly(poly, guess) < epsilon and \
               evaluate_poly(poly, guess) > -epsilon):
        guess = guess - (evaluate_poly(poly, guess) / 
                         evaluate_poly(deriv, guess))
        no_of_guesses += 1
        print("Guess:", guess)
    return guess, no_of_guesses

order = int(input("Enter order of poly: "))
lst = list()
for i in range(order+1):
    lst.append(float(input("Enter the coefficient for %d power of poly: " % i)))
x = float(input("Enter value of x: "))
poly = tuple(lst)
print(poly)
print(evaluate_poly(poly, x))
print(compute_deriv(poly))
guess = float(input("Guess the root of poly: "))
print(compute_root(poly, guess, 0.0001))
