import xml.etree.ElementTree as ET
import mysql.connector

# Load XML data from a file
xml_file_path = 'downloads\generated_xml_20240203004342.xml'
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Aksh@123",
    database="dev"
)
cursor = db_connection.cursor()

# Create a table for accident records if not exists
create_table_query = '''
CREATE TABLE IF NOT EXISTS accidents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    location_city VARCHAR(255),
    location_state VARCHAR(255),
    description VARCHAR(255),
    severity VARCHAR(50),
    make VARCHAR(50),
    model VARCHAR(50),
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    license_plate VARCHAR(20)
)
'''
cursor.execute(create_table_query)

# Iterate through each accident record and insert into the database
for accident in root.findall('accident'):
    date = accident.find('date').text
    location_city = accident.find('location/city').text
    location_state = accident.find('location/state').text
    description = accident.find('details/description').text
    severity = accident.find('details/severity').text

    vehicles_data = []
    individuals_data = []

    # Iterate through vehicles and collect data
    for vehicle in accident.findall('vehicles/vehicle'):
        make = vehicle.find('make').text
        model = vehicle.find('model').text
        license_plate = vehicle.find('license_plate').text
        vehicles_data.append((make, model, license_plate))

    # Iterate through individuals and collect data
    for person in accident.findall('individuals/person'):
        name = person.find('name').text
        age = person.find('age').text
        gender = person.find('gender').text
        individuals_data.append((name, age, gender))

    # Example SQL query for inserting accident and related vehicles and persons
    insert_query = '''
    INSERT INTO accidents (date, location_city, location_state, description, severity, make, model, license_plate, name, age, gender)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    # Combine all data for the accident
    values = [(date, location_city, location_state, description, severity, *vehicle_data, *individual_data)
              for vehicle_data in vehicles_data for individual_data in individuals_data]

    cursor.executemany(insert_query, values)

# Commit the changes and close connections
db_connection.commit()
cursor.close()
db_connection.close()
