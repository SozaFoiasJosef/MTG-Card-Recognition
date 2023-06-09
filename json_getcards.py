import json

with open("filtered_cards.json", encoding="utf-8") as f:
    
    json_data = json.load(f)

#filtered_data = [item for item in json_data if item["set"] == "mh2"]
normal_images = [item["image_uris"]["art_crop"] for item in json_data if "image_uris" in item and "art_crop" in item["image_uris"]]

#filtered_data = [item for item in json_data if "image_uris" in item and "normal" in item["image_uris"]]
#normal_images = [item["image_uris"]["normal"] for item in json_data if "image_uris" in item and "normal" in item["image_uris"]]
#normal_images = [item["image_uris"]["art_crop"] for item in json_data if "image_uris" in item and "art_crop" in item["image_uris"]]


with open("full_artcrop.json", "w") as f:
    json.dump(normal_images, f, indent=2)

#print(json.dumps(filtered_data, indent=2))
