import json
import requests

with open("filtered_cards.json", encoding="utf-8") as f:
    
    json_data = json.load(f)

#filtered_data = [item for item in json_data if item["set"] == "mh2"]
#filtered_data = [item for item in json_data if "image_uris" in item and "normal" in item["image_uris"]]
normal_images = [item["image_uris"]["normal"] for item in json_data if "image_uris" in item and "normal" in item["image_uris"]]


with open("filtered_cards1.json", "w") as f:
    json.dump(normal_images, f, indent=2)

#print(json.dumps(filtered_data, indent=2))

for i, url in enumerate(normal_images):
    response = requests.get(url)
    filename = f"image{i}.jpg"
    with open(filename, "wb") as f:
        f.write(response.content)