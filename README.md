# AI Text-to-Image Generator

A powerful AI-driven text-to-image generation tool built with Gradio and Hugging Face Diffusers. This application provides an intuitive web interface for creating stunning images from text descriptions using state-of-the-art diffusion models.

## Features

- **Easy-to-use web interface** powered by Gradio
- **Advanced AI image generation** using pre-trained diffusion models
- **Real-time processing** with progress tracking
- **Customizable generation parameters** (steps, guidance scale, dimensions)
- **Multiple art styles and models** to choose from
- **Responsive design** that works on desktop and mobile
- **High-quality outputs** with various resolution options
- **No API keys required** - runs locally

## Demo

Simply enter a text prompt describing what you want to create, adjust settings if needed, click "Generate," and watch as AI brings your imagination to life!

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- CUDA-compatible GPU (recommended for faster generation)
- At least 8GB of RAM (16GB+ recommended)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/sudeshna999/Text-to-Image-Generator.git
   cd ai-text-to-image-generator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the web interface**
   Open your browser and navigate to `http://localhost:7860`

## Dependencies

The project relies on the following key libraries:

- **diffusers**: Hugging Face library for diffusion models
- **gradio**: Web interface framework for machine learning applications
- **torch**: PyTorch deep learning framework
- **transformers**: For text encoding and processing
- **accelerate**: For optimized model loading and inference
- **safetensors**: Secure tensor serialization format
- **Additional dependencies**: See `requirements.txt` for complete list

## Usage

1. **Launch the application** by running `python app.py`
2. **Open the web interface** in your browser
3. **Enter your text prompt** describing the image you want to generate
4. **Adjust generation settings**:
   - Number of inference steps (quality vs speed)
   - Guidance scale (prompt adherence)
   - Image dimensions
   - Random seed (for reproducibility)
5. **Click "Generate"** to create your image
6. **Download or save** the generated images

### Example Prompts

- "A serene mountain landscape at sunset with purple clouds"
- "A futuristic cityscape with neon lights and flying cars"
- "A cute robot reading a book in a cozy library"
- "Abstract art with vibrant colors and geometric patterns"
- "A photorealistic portrait of a wise old wizard"
- "A minimalist logo design for a tech startup"

### Supported Styles

- Photorealistic images
- Digital art and illustrations
- Abstract and artistic creations
- Logo and graphic design
- Concept art and sketches
- Fantasy and sci-fi imagery

## Technical Details

- **Models**: Uses state-of-the-art diffusion models (Stable Diffusion, DALL-E style models)
- **Interface**: Gradio provides a clean, intuitive web UI with real-time previews
- **Processing**: Runs entirely locally - your prompts and images stay private
- **Performance**: Optimized for GPU acceleration with fallback to CPU
- **Memory Management**: Efficient model loading with options for low-VRAM systems

## Project Structure

```
ai-text-to-image-generator/
├── app.py              # Main Gradio application
├── models/             # Model configuration and utilities
├── utils/              # Helper functions and image processing
├── requirements.txt    # Python dependencies
├── config.yaml         # Configuration settings
└── README.md          # Project documentation
```

## Configuration

You can customize the application by editing `config.yaml`:

```yaml
model:
  name: "stabilityai/stable-diffusion-2-1"
  device: "auto"  # auto, cuda, cpu
  precision: "fp16"

generation:
  default_steps: 50
  default_guidance: 7.5
  default_width: 512
  default_height: 512
  max_batch_size: 4

interface:
  title: "AI Text-to-Image Generator"
  theme: "default"
  share: false
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- Add support for different diffusion models (DALL-E, Midjourney-style)
- Implement image-to-image generation capabilities
- Add style transfer and artistic filters
- Create prompt suggestion and enhancement features
- Implement batch generation for multiple prompts
- Add image editing and post-processing tools
- Improve the UI/UX with advanced controls
- Add API endpoints for programmatic access

## Troubleshooting

### Common Issues

**"CUDA out of memory" error**
- Reduce image dimensions or batch size
- Enable mixed precision in config
- Close other GPU-intensive applications

**"Model not found" error**
- Ensure stable internet connection for initial model download
- Check if you have sufficient disk space (models can be 2-5GB)

**Slow generation times**
- Reduce number of inference steps (try 20-30 instead of 50)
- Use smaller image dimensions for faster results
- Ensure GPU drivers are up to date

**Poor image quality**
- Increase inference steps for better quality
- Experiment with different guidance scale values
- Try more detailed and specific prompts

## Performance Tips

- **For faster generation**: Use fewer steps (20-30), smaller images (256x256)
- **For better quality**: Use more steps (50-100), higher guidance scale (7-15)
- **For consistent results**: Set a fixed seed value
- **For variety**: Use negative seeds or random seed generation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing excellent diffusion models and libraries
- [Stability AI](https://stability.ai/) for Stable Diffusion models
- [Gradio](https://gradio.app/) for the amazing web interface framework
- The open-source community for continuous innovation in AI art generation

## Ethical Use

Please use this tool responsibly:
- Respect copyright and intellectual property rights
- Avoid generating harmful, offensive, or inappropriate content
- Consider the environmental impact of AI model training and inference
- Credit AI assistance when using generated images commercially

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/ai-text-to-image-generator/issues) page
2. Create a new issue with detailed information about your system and the problem
3. Include sample prompts and error messages when applicable
4. Star the repository if you find it useful!

## Roadmap

- [ ] Support for ControlNet and guided generation
- [ ] Integration with popular art styles and aesthetic models
- [ ] Real-time prompt suggestions and auto-completion
- [ ] Advanced image editing and inpainting capabilities
- [ ] Multi-language prompt support
- [ ] Cloud deployment options

---

**Happy Creating!**

## Author
### Sudeshna Dey
### Contact & Contributions

#### Email: sudeshnadey1000@gmail.com
