import requests
import json
import base64


def generate_image(prompt):
    # API endpoint extracted from the curl command
    api_url = "http://localhost:7860/sdapi/v1/txt2img" ##Replace with the URL of your SD WebUI

    # Prepare the headers as in the curl command
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    # Prepare the data payload as in the curl command, updating the prompt dynamically
    data = {
        "prompt": prompt,
        "negative_prompt": neg_prompt,
        "styles": [""],
        "seed": -1,
        "subseed": -1,
        "subseed_strength": 0,
        "seed_resize_from_h": -1,
        "seed_resize_from_w": -1,
        "sampler_name": "Euler",
        "batch_size": 1,
        "n_iter": 1,
        "steps": 50,
        "cfg_scale": 7,
        "width": 512,
        "height": 512,
        "restore_faces": False,
        "tiling": True,
        "do_not_save_samples": False,
        "do_not_save_grid": False,
        "eta": 0,
        "denoising_strength": 0,
        "s_min_uncond": 0,
        "s_churn": 0,
        "s_tmax": 0,
        "s_tmin": 0,
        "s_noise": 0,
        "override_settings": {},
        "override_settings_restore_afterwards": True,
        "disable_extra_networks": True,
        "send_images": True,
        "save_images": False
    }

    # Make the POST request
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    saved_files = []

    if response.status_code == 200:
        response_json = response.json()

        # Check if the API response includes base64 encoded image data
        if 'images' in response_json:
            # Assuming 'image_data' is a list of strings
            encoded_image_data = response_json['images']
            # Join the list into a single string if it's not already
            if isinstance(encoded_image_data, list):
                encoded_image_data = ''.join(encoded_image_data)

            # Decode the base64 string
            image_bytes = base64.b64decode(encoded_image_data)
            image_filename = '/home/neutrinotek/generated_image_from_base64.png'
            with open(image_filename, 'wb') as image_file:
                image_file.write(image_bytes)
            print(f"Image generated from base64 and saved as {image_filename}")
            saved_files.append(str(image_filename))
            return saved_files
        else:
            print("The API response does not contain 'image_data'.")
    else:
        print("Failed to generate image:", response.text)


# Example usage
prompt = "A picture of a beautiful sunset"  # Replace with your desired prompt
neg_prompt = ("bad quality, worst quality, (deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, "
              "cartoon, drawing, anime), text, cropped, out of frame")
generate_image(prompt)
