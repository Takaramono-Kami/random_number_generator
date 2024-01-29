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
def linear_congruential_generator(number_list, multiplier, increment, seed, *modulus):
    
    modulus = len(number_list)
    random_number_instant = ((multiplier * seed) + increment) % modulus
    random_number = number_list[random_number_instant]
    
    return [random_number, random_number_instant]

# function of normal distribution probability density -> PDF
def noraml_pdf(x, miu, sigma):
    
    return (1/(sigma*(2*math.pi)**0.5)) * math.exp(-0.5*((x-miu)/sigma)**2)


# function to generate 
def decimal_normal_distribution(miu = 0, variance = 1):
    
    result = []
    seed = 2
    
    for _ in range(100):
        u1 = linear_congruential_generator(decimal_uniform_distribution_zeroone(), 1, 2, seed)
        u2 = linear_congruential_generator(decimal_uniform_distribution_zeroone(), 1, 2, u1[1])
        z0 = math.sqrt(-2 * math.log(u1[0], math.exp(1))) * math.sin(2 * math.pi * u2[0])
        z = z0 * variance + miu  
        result.append(z)
        seed = u2[1]
    return result


# print(integer_uniform_distribution(10,3))
# print(decimal_uniform_distribution(10))
print(decimal_normal_distribution())

# seed = 5
# for _ in range(5):
#     print(linear_congruential_generator(decimal_uniform_distribution_zeroone(),2, 4, seed, 1)[0])
#     seed = linear_congruential_generator(decimal_uniform_distribution_zeroone(),2, 4, seed, 1)[1]
    