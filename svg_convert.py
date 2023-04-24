import json
import os
import requests
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# Load the JSON file containing image URLs
with open('sets.json') as f:
    json_data = json.load(f)

icon_svg_uris = [set_data['icon_svg_uri'] for set_data in json_data['data']]



def download_svg(urls):
    for i, url in enumerate(urls):
        response = requests.get(url)
        filename = f"image{i}.svg"
        with open(filename, "wb") as f:
            f.write(response.content)



dir_path = os.path.dirname(os.path.realpath(__file__))
input_dir = dir_path
output_dir = os.path.join(dir_path, 'output')

def svg_to_jpg(input_dir, output_dir):
    # Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for file_name in os.listdir(input_dir):
        # Check if the file is an SVG file
        if file_name.endswith('.svg'):
            # Construct input and output file paths
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + '.jpg')
        
            # Convert SVG to JPG using svglib and reportlab
            drawing = svg2rlg(input_path)
            renderPM.drawToFile(drawing, output_path, fmt='JPG')
            
#download_svg(icon_svg_uris)
#svg_to_jpg(input_dir, output_dir)


