
import yaml
CONFIG_FPATH = "./sample.yml"

# open the yml file
with open(CONFIG_FPATH) as f:
     dictionary = yaml.safe_load(f)
# print elements in dictionary
for key, value in dictionary.items():
     print(key + " : " + str(value))
     print()