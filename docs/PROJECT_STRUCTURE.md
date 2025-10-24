# 📁 Smart CV Evaluator - Project Structure

This document outlines the professional project structure for Smart CV Evaluator.

## 🏗️ Directory Overview

```
Smart CV Evaluator/
├── 📱 Application Core
│   ├── app.py                    # Main Streamlit application
│   ├── requirements.txt          # Python dependencies
│   └── pyproject.toml            # Modern Python project configuration
│
├── 🧠 Source Code (src/)
│   ├── parser.py                # CV text extraction and parsing
│   ├── rag_pipeline.py          # AI analysis pipeline
│   └── prompt_templates.py      # AI prompt templates
│
├── ⚙️ Configuration (config/)
│   ├── settings.py              # Application settings and constants
│   └── __init__.py              # Configuration package
│
├── 🧪 Testing (tests/)
│   ├── conftest.py              # Pytest configuration and fixtures
│   ├── test_parser.py           # Parser functionality tests
│   ├── test_rag_pipeline.py     # RAG pipeline tests
│   └── __init__.py              # Test package
│
├── 🐳 Docker Configuration
│   ├── Dockerfile               # Docker image definition
│   ├── docker-compose.yml       # Multi-container setup
│   └── .dockerignore            # Docker build optimization
│
├── 🚀 Deployment Scripts (scripts/)
│   ├── run_app.bat              # Windows Python startup
│   ├── run_app.sh               # Linux/Mac Python startup
│   ├── run_docker.bat           # Windows Docker startup
│   └── run_docker.sh            # Linux/Mac Docker startup
│
├── 📚 Documentation (docs/)
│   ├── PROJECT_STRUCTURE.md     # This file
│   ├── DOCKER_DEPLOYMENT.md     # Docker deployment guide
│   └── PROJECT_COMPLETION.md    # Project status and completion
│
├── 🎨 Assets (assets/)
│   └── static/                  # CSS and static files
│       └── style.css            # Custom styling
│
├── 📄 Templates (templates/)
│   └── (Future template files)  # UI templates and components
│
└── 📋 Project Files
    ├── README.md                # Main project documentation
    ├── CONTRIBUTING.md          # Contribution guidelines
    ├── CHANGELOG.md             # Version history
    ├── LICENSE                  # MIT License
    └── env.example              # Environment configuration template
```

## 🎯 Design Principles

### 1. **Separation of Concerns**
- **Application Logic**: `app.py` - Main Streamlit interface
- **Business Logic**: `src/` - Core functionality modules
- **Configuration**: `config/` - Settings and constants
- **Testing**: `tests/` - Comprehensive test suite

### 2. **Professional Organization**
- **Clear Structure**: Logical directory hierarchy
- **Modular Design**: Reusable components
- **Configuration Management**: Centralized settings
- **Documentation**: Comprehensive guides

### 3. **Development Ready**
- **Testing Framework**: Pytest with fixtures
- **Code Quality**: Black, flake8, mypy
- **Pre-commit Hooks**: Automated quality checks
- **Docker Support**: Complete containerization

## 📦 Package Structure

### Core Application (`app.py`)
- Streamlit web interface
- File upload handling
- UI components and styling
- Integration with business logic

### Source Modules (`src/`)
- **`parser.py`**: CV text extraction from PDF/DOCX
- **`rag_pipeline.py`**: AI analysis and scoring
- **`prompt_templates.py`**: AI prompt management

### Configuration (`config/`)
- **`settings.py`**: Centralized configuration
- Environment variable management
- Path definitions and constants
- Feature flags and options

### Testing (`tests/`)
- **`conftest.py`**: Shared fixtures and setup
- **`test_parser.py`**: Parser functionality tests
- **`test_rag_pipeline.py`**: AI pipeline tests
- Comprehensive coverage

## 🚀 Deployment Options

### 1. **Direct Python Execution**
```bash
# Development
streamlit run app.py

# Production
python app.py
```

### 2. **Docker Containerization**
```bash
# Development
docker-compose up --build

# Production
docker run -p 8501:8501 smart-cv-evaluator
```

### 3. **Script-based Deployment**
```bash
# Windows
scripts/run_app.bat
scripts/run_docker.bat

# Linux/Mac
scripts/run_app.sh
scripts/run_docker.sh
```

## 🔧 Configuration Management

### Environment Variables
- **Development**: `.env` file (create from `env.example`)
- **Production**: System environment variables
- **Docker**: Docker Compose environment section

### Settings Hierarchy
1. **Default Values**: `config/settings.py`
2. **Environment Variables**: `.env` file
3. **System Variables**: OS environment
4. **Runtime Overrides**: Application parameters

## 🧪 Testing Strategy

### Test Organization
- **Unit Tests**: Individual component testing
- **Integration Tests**: Component interaction testing
- **End-to-End Tests**: Full workflow testing
- **Performance Tests**: Load and stress testing

### Test Coverage
- **Target**: >80% code coverage
- **Tools**: pytest, pytest-cov
- **Reports**: HTML and terminal output
- **CI/CD**: Automated testing pipeline

## 📈 Scalability Considerations

### Horizontal Scaling
- **Docker Containers**: Easy replication
- **Load Balancing**: Multiple container instances
- **Database**: External database support
- **Caching**: Redis integration ready

### Vertical Scaling
- **Resource Limits**: Docker resource constraints
- **Memory Management**: Efficient resource usage
- **Performance**: Optimized algorithms
- **Monitoring**: Health checks and metrics

## 🔒 Security Features

### File Security
- **Upload Validation**: File type and size checks
- **Temporary Files**: Automatic cleanup
- **Path Security**: Safe file handling
- **Input Sanitization**: XSS prevention

### Application Security
- **Environment Isolation**: Docker containers
- **Secret Management**: Environment variables
- **Access Control**: Authentication ready
- **Audit Logging**: Comprehensive logging

## 📊 Monitoring and Logging

### Logging Configuration
- **Levels**: DEBUG, INFO, WARNING, ERROR
- **Formats**: Structured JSON logging
- **Rotation**: Size-based log rotation
- **Retention**: Configurable retention policy

### Health Monitoring
- **Health Checks**: Docker health checks
- **Metrics**: Performance metrics
- **Alerts**: Error and performance alerts
- **Dashboards**: Monitoring dashboards

## 🚀 Future Enhancements

### Planned Additions
- **API Endpoints**: REST API support
- **Authentication**: User management
- **Database**: Persistent storage
- **Analytics**: Usage analytics
- **Multi-tenancy**: Multi-user support

### Architecture Evolution
- **Microservices**: Service decomposition
- **Event-driven**: Async processing
- **Message Queues**: Background processing
- **Cloud Native**: Kubernetes deployment

## 📚 Documentation Standards

### Code Documentation
- **Docstrings**: Google style docstrings
- **Type Hints**: Full type annotation
- **Comments**: Inline code comments
- **README**: Comprehensive project overview

### API Documentation
- **OpenAPI**: Swagger documentation
- **Examples**: Code examples
- **Tutorials**: Step-by-step guides
- **Reference**: Complete API reference

---

This project structure provides a solid foundation for a professional, scalable, and maintainable application. The modular design allows for easy extension and modification while maintaining code quality and best practices.
