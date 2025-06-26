# 🚀 DevOps Demo App

A simple Flask web app demonstrating file upload functionality, containerization with Docker, and continuous deployment using **GitHub Actions** and a **self-hosted runner**.

---

## 📦 Features

- 🐍 Python Flask app with a file upload form
- 📤 Saves uploaded files to the server
- 🐳 Dockerized using Dockerfile
- ⚙️ Multi-container orchestration via Docker Compose
- 🔁 CI/CD pipeline with GitHub Actions
- 🖥️ Deployment on self-hosted GitHub Actions runner

---

## 🧰 Technologies Used

- Python 3
- Flask
- HTML (Jinja2)
- Docker & Docker Compose
- GitHub Actions

---


## 🧰 Project Structure

```
devops-demo-app/
├── docker-compose.yml
├── Dockerfile
└── app/
    ├── main.py                # Flask app logic
    ├── templates/
    │   └── upload.html        # File upload form
    └── uploads/               # Uploaded files go here
```


---

## 📂 How It Works

- Home (`/`) displays a static message.
- Upload page (`/upload`) serves an HTML form.
- On POST, uploaded file is saved to `/app/uploads/`.
- CI/CD pipeline auto-deploys changes using a self-hosted runner.

---
## ▶️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/afshin-8/devops-demo-app.git
cd devops-demo-app
```

### 2. Run via Docker Compose

```bash
docker-compose up --build
```

### 3. Access the App

- Home: [http://localhost:5000](http://localhost:5000)
- Upload: [http://localhost:5000/upload](http://localhost:5000/upload)

---

## 🔁 CI/CD with GitHub Actions

Pipeline is triggered on every push to the `main` branch.  
Runs on a **self-hosted GitHub Actions runner**.

### Sample workflow steps:

- Checkout code  
- Set up Python  
- *(Optional)* Install dependencies and run tests  
- Build and deploy the app
