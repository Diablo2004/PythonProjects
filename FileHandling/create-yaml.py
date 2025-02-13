import yaml
data = {
    "name": "Mehul",
    "age": 21,
    "skills": ["Python", "Machine Learning", "Cloud"],
    "details": {
        "city": "Hyderabad",
        "job": "Software Engineer"
    }
}

# Writing YAML file
with open("data.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)

print("YAML file written successfully!")
