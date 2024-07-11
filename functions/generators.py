# Mostly (fully), built using faker. https://faker.readthedocs.io/en/master/

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
# Currently, the state is in the USA, but the country is random. South Georgia and the South Sandwich Islands :p
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
    # @todo: Look into differnce.
    #return faker.ascii_safe_email()
    return faker.ascii_free_email()


def generate_fake_dob():
    return faker.passport_dob()
    

# function to generate a complete "fake" identity. 
from faker import Faker

# Corrected function to generate a complete "fake" identity complete with name, adress, dob, and such. 
def generate_fake_identity(gender, country_code, mail):
    # Corrected the locale format from 'se_sv' to 'sv_SE'
    corrected_country_code = 'sv_SE' if country_code == 'se_sv' else country_code
    faker = Faker(corrected_country_code)
    
    # Generate name based on gender
    if gender.lower() == 'male':
        name = faker.name_male()
    elif gender.lower() == 'female':
        name = faker.name_female()
    else:
        name = faker.name()
    
    # Generate other details
    dob = faker.date_of_birth()
    phone_number = faker.phone_number()
    address = faker.address()
    email = faker.ascii_free_email() if mail else ""
    
    # Generate credit card details
    credit_card_provider = faker.credit_card_provider()
    credit_card_number = faker.credit_card_number(card_type=None)
    credit_card_expire = faker.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
    credit_card_security_code = faker.credit_card_security_code(card_type=None)
    
    # Compile the identity information
    identity = {
        "name": name,
        "dob": dob,
        "phone_number": phone_number,
        "address": address,
        "email": email,
        "credit_card": {
            "provider": credit_card_provider,
            "number": credit_card_number,
            "expire": credit_card_expire,
            "security_code": credit_card_security_code
        }
    }
    
    return identity

print(generate_fake_identity('male', 'sv_SE', 'mail'))
