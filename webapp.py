from flask import Flask, render_template, Response, request
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_xml():
    if request.method == 'POST':
        # Get form values from the submitted form
        accident_id = request.form.get('id')
        accident_date = request.form.get('date')
        city = request.form.get('location_city')
        state = request.form.get('location_state')
        license_plate = request.form.get('license_plate')
        make = request.form.get('make')
        model = request.form.get('model')
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        description = request.form.get('description')
        severity = request.form.get('severity')
    else:
        # If the form is not submitted, set values to empty strings
        accident_id = ''
        accident_date = ''
        city = ''
        state = ''
        license_plate = ''
        make = ''
        model = ''
        name = ''
        age = ''
        gender = ''
        description = ''
        severity = ''

    accidents = Element("accidents")

    # Create accident element
    accident = SubElement(accidents, "accident")
    SubElement(accident, "id").text = accident_id
    SubElement(accident, "date").text = accident_date

    # Create location element
    location = SubElement(accident, "location")
    SubElement(location, "city").text = city
    SubElement(location, "state").text = state

    # Create vehicles element
    vehicles = SubElement(accident, "vehicles")
    vehicle = SubElement(vehicles, "vehicle")
    SubElement(vehicle, "license_plate").text = license_plate
    SubElement(vehicle, "make").text = make
    SubElement(vehicle, "model").text = model

    # Create individuals element
    individuals = SubElement(accident, "individuals")
    person = SubElement(individuals, "person")
    SubElement(person, "name").text = name
    SubElement(person, "age").text = age
    SubElement(person, "gender").text = gender

    # Create details element
    details = SubElement(accident, "details")
    SubElement(details, "description").text = description
    SubElement(details, "severity").text = severity

    xml_str = minidom.parseString(tostring(accidents)).toprettyxml(indent="    ")

    # Save the XML content to a file with a timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'generated_xml_latest.xml'
    filepath = os.path.join('downloads', filename)

    with open(filepath, 'w') as file:
        file.write(xml_str)

    return render_template('index.html', xml_str=xml_str)

if __name__ == '__main__':
    app.run(debug=True)
