# 📊 Smart CV Evaluator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**AI-powered CV analysis for job seekers. Get instant feedback on ATS compatibility, content quality, and improvement recommendations.**

[🚀 Live Demo](#-quick-start) • [📖 Documentation](#-features) • [🐳 Docker](#-docker-deployment) • [🤝 Contributing](#-contributing)

</div>

---

## ✨ Features

### 🎯 **Intelligent Analysis**
- **ATS Compatibility Scoring** - Comprehensive 100-point evaluation system
- **AI-Powered Recommendations** - Actionable suggestions for improvement
- **Multi-Format Support** - PDF and DOCX file processing
- **Privacy-First** - Local AI processing with Ollama

### 📈 **Professional Insights**
- **Section-by-Section Analysis** - Education, Experience, Skills, Projects
- **Quality Assessment** - Professional summary and scoring
- **Industry Best Practices** - ATS optimization guidelines
- **Real-time Processing** - Fast, efficient analysis

### 🎨 **Modern Interface**
- **Responsive Design** - Works on desktop and mobile
- **Professional UI** - Clean, intuitive user experience
- **Real-time Feedback** - Progress indicators and status updates
- **Export Ready** - Results ready for sharing

## 🚀 Quick Start

### Option 1: Direct Python (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-cv-evaluator.git
cd smart-cv-evaluator

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Option 2: Docker (Production Ready)

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-cv-evaluator.git
cd smart-cv-evaluator

# Build and run with Docker
docker-compose up --build

# Or use the convenient script
run_docker.bat  # Windows
./run_docker.sh  # Linux/Mac
```

### Option 3: Easy Startup Scripts

```bash
# For Python execution
run_app.bat  # Windows
./run_app.sh  # Linux/Mac

# For Docker execution
run_docker.bat  # Windows
./run_docker.sh  # Linux/Mac
```

## 🔧 Prerequisites

### Required Software
- **Python 3.10+** - [Download Python](https://python.org)
- **Ollama** - [Install Ollama](https://ollama.ai)
- **Docker** (optional) - [Install Docker](https://docker.com)

### Ollama Setup
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the required model
ollama pull deepseek-coder:1.3b

# Start Ollama service
ollama serve
```

## 📊 ATS Scoring System

Our comprehensive evaluation system assesses CVs across 8 key criteria:

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Contact Information** | 10 pts | Complete contact details |
| **Professional Summary** | 15 pts | Clear, compelling summary |
| **Work Experience** | 25 pts | Relevant experience with achievements |
| **Education** | 10 pts | Educational background |
| **Skills Section** | 15 pts | Technical and soft skills |
| **Format & Structure** | 10 pts | Clean, professional layout |
| **Keywords & ATS** | 10 pts | ATS-optimized content |
| **Achievements** | 5 pts | Quantifiable results |

### Scoring Scale
- **90-100**: 🎉 Exceptional - Ready for ATS and human review
- **80-89**: ✅ Strong - Minor improvements needed
- **70-79**: 📈 Good - Several areas for improvement
- **60-69**: ⚠️ Average - Significant improvements required
- **Below 60**: 🔄 Needs Overhaul - Major restructuring required

## 🏗️ Project Structure

```
Smart CV Evaluator/
├── 📱 Application
│   ├── app.py                    # Main Streamlit application
│   ├── requirements.txt          # Python dependencies
│   └── src/                      # Source code modules
│       ├── parser.py            # CV text extraction
│       ├── rag_pipeline.py      # AI analysis pipeline
│       └── prompt_templates.py  # AI prompt templates
├── 🐳 Docker Configuration
│   ├── Dockerfile               # Docker image definition
│   ├── docker-compose.yml      # Multi-container setup
│   └── .dockerignore           # Docker build optimization
├── 🚀 Deployment Scripts
│   ├── run_app.bat             # Python startup (Windows)
│   ├── run_docker.bat          # Docker startup (Windows)
│   └── run_app.sh              # Python startup (Linux/Mac)
├── 📚 Documentation
│   ├── README.md               # This file
│   ├── DOCKER_DEPLOYMENT.md    # Docker deployment guide
│   └── PROJECT_COMPLETION.md   # Project status
└── 🎨 Static Assets
    └── static/                 # CSS and static files
```

## 🐳 Docker Deployment

### Quick Docker Setup

```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d --build

# Stop services
docker-compose down
```

### Production Deployment

```bash
# Build production image
docker build -t smart-cv-evaluator:latest .

# Run with custom configuration
docker run -p 8501:8501 \
  -v $(pwd)/uploads:/app/uploads \
  -v $(pwd)/temp:/app/temp \
  smart-cv-evaluator:latest
```

For detailed Docker instructions, see [DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md).

## ⚙️ Configuration

### Environment Variables

```bash
# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Ollama Configuration
OLLAMA_HOST=localhost
OLLAMA_PORT=11434
```

### Customizing AI Models

Edit `src/rag_pipeline.py` to change the AI model:

```python
self.llm = ChatOllama(
    model="deepseek-coder:1.3b",  # Change model here
    temperature=0.5,
    top_k=40,
    top_p=0.9,
    num_ctx=2048
)
```

### Modifying Scoring Criteria

Update `src/prompt_templates.py` to adjust scoring weights and criteria.

## 🛠️ Development

### Setting Up Development Environment

```bash
# Clone repository
git clone https://github.com/yourusername/smart-cv-evaluator.git
cd smart-cv-evaluator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Run in development mode
streamlit run app.py
```

### Adding New Features

1. **New File Formats**: Extend `src/parser.py`
2. **Additional Analysis**: Modify `src/rag_pipeline.py`
3. **UI Components**: Update `app.py`
4. **Scoring Criteria**: Edit `src/prompt_templates.py`

## 🔍 Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| **"Model not found"** | Ensure Ollama is running: `ollama serve` |
| **Import errors** | Install dependencies: `pip install -r requirements.txt` |
| **Empty text extraction** | Check file format and corruption |
| **Docker build fails** | Check network connection and Docker daemon |
| **Port already in use** | Change port: `streamlit run app.py --server.port 8502` |

### Getting Help

- **Application Issues**: Check the logs and error messages
- **Docker Issues**: See [DOCKER_DEPLOYMENT.md](DOCKER_DEPLOYMENT.md)
- **Ollama Issues**: Visit [Ollama Documentation](https://ollama.ai/docs)
- **General Support**: Open an issue on GitHub

## 📈 Performance

- **Startup Time**: ~5-10 seconds
- **Analysis Time**: ~20-30 seconds per CV
- **Memory Usage**: ~200-500MB
- **Supported Formats**: PDF, DOCX
- **File Size Limit**: 10MB (configurable)

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### How to Contribute

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation
- Ensure Docker compatibility

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Streamlit** - For the amazing web framework
- **Ollama** - For local AI model support
- **LangChain** - For LLM integration
- **Community** - For feedback and contributions

<div align="center">

**⭐ Star this repository if you found it helpful!**

[🚀 Get Started](#-quick-start) • [📖 Documentation](#-features) • [🐳 Docker](#-docker-deployment) • [🤝 Contributing](#-contributing)

Made with ❤️ by the Smart CV Evaluator Team

</div>
