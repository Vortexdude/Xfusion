from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation
home_path = "/home/jsins/opt/vortexdude/Xfusion"

# images = [
#     Image.open("/Users/apple/Desktop/" + f)
#     for f in ["bbd.jpg", "bbd1.jpg", "bbd2.jpg"]
# ]

def convert_to_pdf(input_image: str, output_file: str) -> None:

    images = [Image.open(f"{home_path}/output/{input_image}")]
    pdf_path = f"{home_path}/output/{output_file}"
        
    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images
    )
