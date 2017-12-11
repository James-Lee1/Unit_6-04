# Created by: James Lee
# Created on: Dec 2017
# Created for: ICS3U
# This program displays an example of a structure with two enumerated types

from enum import Enum

# an enumerated type of streets
Street_types = Enum('Street', 'Boulevard', 'Road', 'Avenue', 'Crescent')

# an enumerated type of provinces and territories
Provinces_and_territories = Enum('AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT')

class Address():
    # this class is the structure for the canada post address with enumerated types
    def __init__(self, name, street_number, street_name, street_type, city, province, postal_code):
        self.name = name
        self.street_number = street_number
        self.street_name = street_name
        self.street_type = street_type
        self.city = city
        self.province = province
        self.postal_code = postal_code


user_name = raw_input("Enter your name: ")
user_street_number = raw_input("Enter your street number: ")
user_street_name = raw_input("Enter your street name: ")
print("Choose your street type: Street, Boulevard, Road, Avenue, Crescent")
user_street_type = raw_input("Enter your street type: ")
if user_street_type in Street_types:
    print('Valid Street Type')
    user_city = raw_input("Enter your city: ")
    print("Enter the abbreviation of the province or territory in this list: AB (Alberta), BC (British Columbia), MB (Manitoba), NB (New Brunswick), NL (Newfoundland and Labrador), NT (Northwest Territories), NS (Nova Scotia), NU (Nunavut), ON (Ontario), PE (Prince Edward Island), QC (Quebec), SK (Saskatchewan)")
    user_province_or_territory = raw_input("Enter your province or territory: ")
    if user_province_or_territory in Provinces_and_territories:
        print('Valid Province or Territory')
        user_postal_code = raw_input("Enter your postal code: ")
        user_input = Address(user_name, user_street_number, user_street_name, user_street_type, user_city, user_province_or_territory, user_postal_code)
        print(user_input.name + '\n' + user_input.street_number + ' ' + user_input.street_name + ' ' +  user_input.street_type + '\n' + user_input.city + ' ' + user_input.province + '   ' +    user_input.postal_code)
    else:
        print('Invalid Street Type')
else:
    print('Invalid Province or Territory')


