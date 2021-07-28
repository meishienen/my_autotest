from common.read_ini import ReadIni
from common.read_yaml_two import read_yaml_data
readini = ReadIni()
yaml_data = read_yaml_data(readini.get_yaml_path())
print(yaml_data)