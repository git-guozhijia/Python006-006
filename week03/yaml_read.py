import yaml,pathlib

path = str(pathlib.Path(__file__).parent.resolve())
file = f"{path}/config_file/config.yaml"

f = open(file, "r", encoding="utf-8")
sdata = yaml.full_load(f)
f.close()
print(sdata)
