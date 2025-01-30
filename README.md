# HNG12 Stage 0 Task- Public API

This is a simple public API developed for **HNG12 Stage 0 Backend Task**. The API returns basic information in JSON format, including:
- The email I registered with for the internship
- The current datetime in ISO 8601 format (UTC)
- The GitHub repository URL of this project

## Tech Stack

- **Programming Language:** Python
- **Framework:** Flask
- **Deployment:** Render
- **CORS Handling:** Enabled with `flask-cors`

---

## API Endpoint

### **Base URL:**

- [Deployed URL](https://hng12-stage0-task-ezoc.onrender.com/)


### **GET /**
- Returns basic information in JSON format

#### **Request:**
```http
GET /
```

#### **Response (200 OK):**
```json
{
  "email": "rhodalee.dev@gmail.com",
  "current_datetime": "2025-01-30T18:13:15.469455Z",
  "github_url": "https://github.com/rhoda-lee/hng12-internship"
}
```

---

## Installation & Setup

### **1. Clone the Repository**
```sh
git clone https://github.com/rhoda-lee/hng12-internship.git
cd hng12-internship/stage0
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Run the API Locally**
```sh
python app.py
```
The API will start on `http://127.0.0.1:5000/`.

---


## Need Developers?
- [Hire Python Developers](https://hng.tech/hire/python-developers)


