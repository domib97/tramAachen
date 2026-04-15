import requests
import time
import json
from datetime import datetime

# Configuration
API_URL = "http://localhost:8000"  # Change to Cluster IP or Ingress if running remotely
CAR_ID = "AC-TRAM-01"

def simulate_24h():
    print(f"--- Starting 24h Simulation for {CAR_ID} ---")
    
    # Simulation states: (Hour, Battery Level, Expected Scenario)
    scenarios = [
        (2, 0.15, "Night / Critical Battery"),
        (8, 0.45, "Morning Peak / Traffic Support"),
        (13, 0.60, "Noon / Solar Surplus"),
        (17, 0.55, "Evening Peak / Grid Balancing"),
        (22, 0.85, "Night / Maintenance")
    ]

    for hour, bat, desc in scenarios:
        print(f"\n[Time: {hour:02d}:00] Scenario: {desc}")
        print(f"Current Battery: {bat*100}%")
        
        try:
            # 1. Check Environmental Context
            solar = requests.get(f"{API_URL}/energy/prediction").json()
            traffic = requests.get(f"{API_URL}/traffic/peaks").json()
            grid = requests.get(f"{API_URL}/grid/status").json()
            
            print(f" > Solar: {solar['predicted_solar_yield_kwh']}kWh | Traffic Peak: {traffic.get('peak_detected')}")

            # 2. Get V2G Decision
            decision = requests.post(
                f"{API_URL}/v2g/decision", 
                params={"car_id": CAR_ID, "battery_level": bat}
            ).json()

            print(f" >>> DECISION: {decision['action']} (Priority: {decision['priority']})")
            print(f" >>> REASON: {decision['reason']}")

        except Exception as e:
            print(f"Error during simulation step: {e}")
        
        time.sleep(1) # Faster simulation

if __name__ == "__main__":
    simulate_24h()
