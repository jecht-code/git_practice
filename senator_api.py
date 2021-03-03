#extracting and parsing data from senatorstockwatch XML.
import requests
import xml.etree.ElementTree as ET

url = 'https://senate-stock-watcher-data.s3.amazonaws.com'
r = requests.get(url)
print(r.status_code)

 # saving the xml file 
with open('senate_stock_data.xml', 'wb') as f: 
    f.write(r.content)

xmlfile = 'senate_stock_data.xml'
tree = ET.parse(xmlfile)
root = tree.getroot()

