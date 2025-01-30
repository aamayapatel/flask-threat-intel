# 🚀 Dockerized Flask API for Threat Intelligence

- This project provides an API to check IP addresses against **VirusTotal** and **AbuseIPDB** for threat intelligence.

## 🚀 Features
- Checks an IP address using **VirusTotal API** for malicious reports.
- Checks an IP address using **AbuseIPDB API** for abuse confidence scores.
- Dockerized for easy deployment.

## 🔧 Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/flask-threat-intel.git
cd flask-threat-intel
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys  
Create a `.env` file:
```
VIRUSTOTAL_API_KEY=your_virustotal_api_key
ABUSEIPDB_API_KEY=your_abuseipdb_api_key
```

### 4️⃣ Run the Application Locally
```bash
python3 app.py
```
Visit:  
http://localhost:5000/check-ip?ip=8.8.8.8

---

## 🐳 Docker Instructions

### 1️⃣ Build the Docker Image
```bash
docker build -t flask-threat-intel .
```

### 2️⃣ Run the Docker Container
```bash
docker run -p 5000:5000 --env-file .env flask-threat-intel
```

### 3️⃣ Test API
http://localhost:5000/check-ip?ip=8.8.8.8

---

## 📡 API Response Example:
```json
{
  "ip": "8.8.8.8",
  "virustotal": {
    "malicious_votes": 0,
    "suspicious_votes": 0,
    "reputation": 99
  },
  "abuseipdb": {
    "abuseConfidenceScore": 0,
    "country": "United States",
    "lastReportedAt": "N/A"
  }
}
```

---

## 🛠 Tech Stack
- Flask (Python)
- Requests (API calls)
- Docker (Containerization)
- VirusTotal API
- AbuseIPDB API

---

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

___

## 🚀 Happy Coding!
```python
print("Happy Coding! 🚀")
```
```python
