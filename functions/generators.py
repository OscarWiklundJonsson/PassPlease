# Mostly (fully), built on using faker. https://faker.readthedocs.io/en/master/

import random
from faker import Faker

faker = Faker()

def generate_name(gender):
    if gender.lower() == 'male':
        return faker.name_male()
    elif gender.lower() == 'female':
        return faker.name_female()
    else:
        return faker.name()

# Generate a random address with street name, street number, postal code, city, county, and country
# Currently, the state is in the USA, but the country is random. South Georgi and the South Sandwich Islands :p
def generate_random_address():
    # Generate random street number and postal code
    street_number = random.randint(1, 9999)
    postal_code = random.randint(10000, 99999)
    
    # Generate random street name, city, county, and country using faker
    street_name = faker.street_name()
    city = faker.city()
    county = faker.state()
    country = faker.country()
    
    # Format the address
    address = f"{street_number} {street_name}, {postal_code}, {city}, {county}, {country}"
    
    return address


def generate_fake_email(): # https://faker.readthedocs.io/en/master/providers/faker.providers.internet.html
    #return faker.ascii_safe_email()
    return faker.ascii_free_email()


def generate_fake_dob():
    return faker.passport_dob()
    