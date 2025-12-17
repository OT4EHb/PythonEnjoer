import xml.etree.ElementTree as ET

lat_min, lon_min = map(
    float,
    input("Введите минимальные границы участка (float float):\n").split()
)
lat_max, lon_max = map(
    float,
    input("Введите максимальные границы участка (float float):\n").split()
)

fname=input("Введите название файла:\n")
tree = ET.parse(fname)
root = tree.getroot()
supermarkets = dict()
for node in root.findall('node'):
    lat = float(node.get('lat'))
    lon = float(node.get('lon'))
    if lat_min > lat or lat > lat_max:
        continue
    if lon_min > lon or lon > lon_max:
        continue
    tags = node.findall('tag')
    kvtags = {i.get('k'): i.get('v') for i in tags}
    if kvtags.get('shop') == 'supermarket':
        name = kvtags.get('name').lower()
        supermarkets[name] = 1 + supermarkets.get(name, 0)
print("\nНайденные супермаркеты:")
for i, j in supermarkets.items():
    print(i, j)
