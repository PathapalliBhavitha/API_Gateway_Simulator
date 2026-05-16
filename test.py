import requests

BASE_URL = "http://127.0.0.1:8000"

payload = {
    "user_id": 1,
    "score": 90
}

print("Testing Gateway API...\n")

response = requests.post(
    f"{BASE_URL}/gateway",
    json=payload
)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())

# -----------------------------
# Invalid Payload Test
# -----------------------------
invalid_payload = {
    "user_id": 1,
    "score": -10
}

print("\nTesting Invalid Payload...\n")

response = requests.post(
    f"{BASE_URL}/gateway",
    json=invalid_payload
)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())

# -----------------------------
# Timeout Simulation
# -----------------------------
timeout_payload = {
    "user_id": 999,
    "score": 80
}

print("\nTesting Timeout Simulation...\n")

try:

    response = requests.post(
        f"{BASE_URL}/gateway",
        json=timeout_payload,
        timeout=2
    )

    print(response.json())

except requests.exceptions.Timeout:

    print("Timeout occurred successfully")