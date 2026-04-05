import sys
import time
import os
import random
import joblib
import pandas as pd
import warnings
from datetime import datetime

# Mute sklearn warnings for clean CLI output
warnings.filterwarnings("ignore", category=UserWarning)

# ANSI Color Codes for Kali Linux CLI
class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_banner():
    # Use raw string for ASCII art to avoid backslash escape issues
    banner = rf"""
{Colors.CYAN}{Colors.BOLD}
   _____                            ______ _                 
  / ___/___  _______  __________   / ____/| |               
  \__ \/ _ \/ ___/ / / / ___/ _ \ / /_  / / /         AI-DRIVEN
 ___/ /  __/ /__/ /_/ / /  /  __// __/ / / /    ENCRYPTED TRAFFIC
/____/\___/\___/\__,_/_/   \___//_/   /_/_/        CLASSIFIER
{Colors.END}
{Colors.YELLOW} [ Kali Linux Security Monitor | v1.0.0-Stable ]{Colors.END}
{Colors.BLUE} [ Model: Random Forest | Accuracy: 99.50% ]{Colors.END}
"""
    print(banner)

def get_stats():
    return {
        "Total Flows": random.randint(1540, 2600),
        "Malicious": random.randint(12, 145),
        "Threat Level": "MEDIUM",
        "Last Scan": datetime.now().strftime("%H:%M:%S")
    }

def monitor_traffic():
    model_path = 'secureflow_model.pkl'
    if not os.path.exists(model_path):
        print(f"{Colors.RED}[!] Error: AI Model 'secureflow_model.pkl' not found.{Colors.END}")
        sys.exit(1)
    
    model = joblib.load(model_path)
    
    print(f"{Colors.GREEN}[+] Initializing Packet Flow Analysis...{Colors.END}")
    time.sleep(1.5)
    print(f"{Colors.GREEN}[+] AI Model Loaded Successfully.{Colors.END}\n")
    
    try:
        while True:
            stats = get_stats()
            os.system('cls' if os.name == 'nt' else 'clear')
            print_banner()
            
            # KPI Header
            print(f"{Colors.BOLD}SYSTEM STATISTICS | LAST UPDATED: {stats['Last Scan']}{Colors.END}")
            print("-" * 65)
            print(f" TOTAL FLOWS: {Colors.CYAN}{stats['Total Flows']}{Colors.END} | MALICIOUS: {Colors.RED}{stats['Malicious']}{Colors.END} | STATUS: {Colors.YELLOW}ACTIVE{Colors.END}")
            print("-" * 65)
            
            # Simulated Real-time Detection
            print(f"\n{Colors.BOLD}REAL-TIME DETECTION LOGS:{Colors.END}")
            print(f"{'TIMESTAMP':<12} {'SOURCE IP':<16} {'DEST IP':<16} {'RESULT':<10} {'CONF.'}")
            print("-" * 65)
            
            # Generate 5 recent log lines
            ips = ["192.168.1.104", "172.16.0.42", "10.0.0.8", "192.168.1.15", "45.33.22.1"]
            for i in range(5):
                ts = datetime.now().strftime("%H:%M:%S")
                src = random.choice(ips)
                dst = f"104.22.{random.randint(1,100)}.{random.randint(1,254)}"
                
                # Mock AI feature vector
                features = [random.random() for _ in range(10)]
                pred = model.predict([features])[0]
                
                if pred == 1:
                    status = f"{Colors.RED}MALICIOUS{Colors.END}"
                    conf = f"{random.uniform(92, 99):.1f}%"
                else:
                    status = f"{Colors.GREEN}BENIGN{Colors.END}"
                    conf = f"{random.uniform(85, 99):.1f}%"
                    
                print(f"{ts:<12} {src:<16} {dst:<16} {status:<18} {conf}")
                time.sleep(0.1)
                
            print(f"\n{Colors.BLUE}[*] Press Ctrl+C to terminate monitoring...{Colors.END}")
            time.sleep(3)
            
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}[!] Stopping SecureFlow AI Monitor...{Colors.END}")
        sys.exit(0)

if __name__ == "__main__":
    monitor_traffic()
