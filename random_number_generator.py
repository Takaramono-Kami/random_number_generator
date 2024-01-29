# in the name of ALLAH

import math

"""
this is a libray that include all function to generate distribution that we need and function to generate 

distribution:
1) integer_uniform_distribution -> genrate a list of integer number by uniform distribution 
2) decimal_uniform_distribution -> genrate a list of float number by uniform distribution
3) decimal_normal_distribution -> generate a list of float number by noramal distribution

"""

# this function get two arguments and return result as list include integer number [a...b]

def integer_uniform_distribution(b, a = 0):
    
    result = list(range(a,b+1))
    result = [i for i in result]

    return result


# this function generate alot decimal number between 0,1

def decimal_uniform_distribution_zeroone():

    numbers_list = list(range(10**4 + 1))
    result = [i/10**4 for i in numbers_list]
    
    return result

# this function map result of last function to range that user entered it, if user doesnt enter start of interval
# ... we set it zero, we use this trick in some function

def decimal_uniform_distribution(b, a =0):
    
    number_list = decimal_uniform_distribution_zeroone()
    interval_range = b - a
    
    result = [(number*interval_range + a) for number in number_list]

    return result

# this function make list of random final number
def linear_congruential_generator(b, multiplier, increment, seed, a= 0, *modulus):
    
    number_list = integer_uniform_distribution(b, a)
    
    modulus = len(number_list)
    random_number_instant = ((multiplier * seed) + increment) % modulus
    random_number = number_list[random_number_instant]
    
    
    return [random_number, random_number_instant]

def noraml_pdf(x, miu, sigma):
    return (1/(sigma*(2*math.pi)**0.5)) * math.exp(-0.5*((x-miu)/sigma)**2)


def decimal_normal_distribution(b, a = 0):
    
    unifrom_number_list = decimal_uniform_distribution(b, a = 0)
    
    result = []
    for unifrom_number in unifrom_number_list:
        f_uniform_number = noraml_pdf(unifrom_number, miu = (b/2), sigma = 1)
        for _ in range(int(f_uniform_number*b**2)):
            result.append(unifrom_number)

    return result


# print(integer_uniform_distribution(10,3))
# print(decimal_uniform_distribution(10))
# print(decimal_normal_distribution(25))

# seed = 5
# for _ in range(5):
#     print(linear_congruential_generator(20,2, 4, seed, 1)[0])
#     seed = linear_congruential_generator(20,2, 4, seed, 1)[1]
    