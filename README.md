# Image-text-Image-Audio using Gradio

Here's a sample `README.md` for your project, tailored to include key sections that describe your project, its installation, usage, and other relevant details. You can customize it further based on your specific needs.

```markdown
# Describe-and-Generate Game

## Overview

The **Describe-and-Generate Game** is an interactive web application that allows users to upload images, generate captions for them, and create new images based on those captions. The application uses the Hugging Face API for image processing and generation, leveraging advanced models for text-to-image and image captioning.

## Features

- Upload an image to generate a descriptive caption.
- Generate a new image based on the generated caption.
- Save generated images to a specified folder.
- Play audio related to the generated caption.

## Technologies Used

- [Gradio](https://gradio.app/) for the web interface.
- [Pillow](https://python-pillow.org/) for image processing.
- [Hugging Face API](https://huggingface.co/docs) for image captioning and generation.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/yourusername/describe-and-generate-game.git
cd describe-and-generate-game
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the project root directory and add your Hugging Face API key and any other necessary environment variables:

```plaintext
HF_API_KEY=your_hugging_face_api_key
HF_API_TTI_BASE=https://api-inference.huggingface.co/models/your_model_name
HF_API_ITT_BASE=https://api-inference.huggingface.co/models/your_model_name
```

## Usage

1. Run the application:

```bash
python app.py
```

2. Open your web browser and go to `http://localhost:7860` (or the port specified in your app).

3. Upload an image and click the "Caption and generate" button to generate a caption and a new image based on that caption.

## Image Compression

Uploaded images are automatically compressed to optimize performance. You can adjust the compression settings in the `compress_image` function within the `helpers/image_helpers.py` file.

## Saving Generated Images

All generated images are saved to the `generated_images` folder within the project directory. This can be modified in the `generate` function if needed.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to Hugging Face for providing powerful models for image processing.
- Thanks to Gradio for creating an easy way to build interactive web applications.

```

### Instructions to Customize
- **Project Title**: Change the title to reflect your project name if different.
- **Repository URL**: Update the `git clone` command with the correct URL of your repository.
- **API Endpoint URLs**: Replace the placeholder model names with the actual models you are using.
- **License**: Specify the license you intend to use for your project.
