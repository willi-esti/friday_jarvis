## Getting Started

### Create Virtual Environment and Install Dependencies

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Windows:**
```bash
python3 -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Run with Docker
```bash
docker compose up
```

or 

```bash
docker compose -f docker-compose-build.yml up
```