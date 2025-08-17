# Flask Notes Web App (Docker + MySQL + Docker Compose on AWS EC2)

A simple **Note-Taking Web Application** built with:
- **Flask (Python)** for the backend  
- **MySQL** for persistent storage  
- **Docker & Docker Compose** for container orchestration  
- **AWS EC2** for cloud deployment  

---

## Features
- Add notes via a simple web UI  
- View all notes (latest first)  
- REST API:
  - `POST /notes` → create a note  
  - `GET /notes` → list all notes in JSON  
- Health check endpoint (`/healthz`)  
- Persistent MySQL database using volumes  
- Container healthchecks to ensure reliability  

---

## Architecture

Browser <--> Flask (web container) <--> MySQL (db container)
|
Docker Compose
|
AWS EC2 Instance

---

## Step-by-Step Setup

### 1️⃣ Create an EC2 Instance on AWS
1. Go to [AWS Console → EC2](https://console.aws.amazon.com/ec2/).  
2. Launch a new instance:  
   - **OS**: Amazon Linux 2023 (or Ubuntu 22.04)  
   - **Instance type**: `t2.micro` (free tier)  
   - **Key pair**: Create or choose an existing `.pem` key  
   - **Security Group**: Allow ports **22 (SSH)**, **80 (HTTP)**, and **5000 (Custom TCP)**  
3. Connect to the instance:
   ```bash
   ssh -i mykey.pem ec2-user@<EC2_PUBLIC_IP>

### 2️⃣ Install Dependencies

On the EC2 instance:
# Update packages
   ```bash
   sudo yum update -y
   ```
# Install git and docker
   ```bash
   sudo yum install -y git docker
   ```
# Install Docker Compose
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-$(uname -s)-$(uname -m)" -o        /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
   ```
# Start Docker service
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```
# Verify
   ```bash
   docker --version
   docker-compose --version
   ```
### 3️⃣ Clone the Project
   ```bash
   git clone https://github.com/<your-username>/flask-notes-app.git
   cd flask-notes-app
   ```
#### 4️⃣ Project Files Explained

Dockerfile → Builds Flask container

docker-compose.yml → Defines web + db services

db/init/init.sql → Initializes MySQL database & table

app/ → Flask code and templates

### 5️⃣ Run the Application
   ```bash
   docker-compose up -d --build
   ```
Check containers:

   ```bash
   docker ps
   ```
You should see:

web → Flask app, port 5000
db → MySQL, port 3306

### 6️⃣ Access the App

Web UI → http://<EC2_PUBLIC_IP>:5000

### 7️⃣ Stop the App
docker-compose down

Testing & Verification

Add a note → It should appear in the list
Restart containers → Notes persist (volume storage)
Health check → /healthz returns 200 OK if DB is connected

✅ Summary

This project demonstrates a real-world DevOps workflow:

Build app → Containerize → Orchestrate → Deploy to Cloud
Use environment variables for config (no secrets in code)
Persist database with volumes
Add healthchecks for reliability


