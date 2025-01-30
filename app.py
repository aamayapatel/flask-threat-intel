import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
VT_API_KEY = os.getenv("VT_API_KEY")
ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

app = Flask(__name__)

VT_API_URL = "https://www.virustotal.com/api/v3/ip_addresses/"
ABUSEIPDB_API_URL = "https://api.abuseipdb.com/api/v2/check"

def check_ip_virustotal(ip):
    """Query VirusTotal API for IP reputation."""
    headers = {"x-apikey": VT_API_KEY}
    response = requests.get(f"{VT_API_URL}{ip}", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve data from VirusTotal", "status_code": response.status_code}

def check_ip_abuseipdb(ip):
    """Query AbuseIPDB API for IP reputation."""
    headers = {"Key": ABUSEIPDB_API_KEY}
    params = {"ipAddress": ip}
    response = requests.get(ABUSEIPDB_API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve data from AbuseIPDB", "status_code": response.status_code}

@app.route('/check-ip', methods=['GET'])
def check_ip():
    """API endpoint to check an IP address."""
    ip = request.args.get('ip')
    
    if not ip:
        return jsonify({"error": "Missing IP address"}), 400

    vt_data = check_ip_virustotal(ip)
    abuse_data = check_ip_abuseipdb(ip)

    # Merge data from both APIs
    result = {
        "virus_total": vt_data,
        "abuse_ipdb": abuse_data
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
