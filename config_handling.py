from yaml import safe_load

# Configuration handling
with open("config.yaml") as f:
    config_file = safe_load(f) 
    citra_path = config_file["citra_path"] # Line 6
    in_path = config_file["in_path"] # Line 11
    out_path = config_file["out_path"] # line 12
    default_file_name = config_file["default_file_name"] # line 16