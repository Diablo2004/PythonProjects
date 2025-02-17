import yaml

with open('ex1.yaml','r') as read_file:
    content = yaml.safe_load(read_file)
    print(content)
    print(type(content))

with open("data.yaml", "r") as file:
    existing_data = yaml.safe_load(file)

# Modify data
existing_data["email"] = "mehul@example.com"

# Write updated YAML back
with open("data.yaml", "w") as file:
    yaml.dump(existing_data, file, default_flow_style=False)

print("Updated YAML file!")
