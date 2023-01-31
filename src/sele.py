#Program
import pandas as pd
import yaml
#Read Config File
config_path = "/Users/soli0/Sites/pg-it/clase/config/config.yml"
config = yaml.load(open(config_path),Loader=yaml.FullLoader)
df = pd.read_csv( config["file_path"])
#All Players
print(df)