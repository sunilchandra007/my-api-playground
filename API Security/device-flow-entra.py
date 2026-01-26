import msal
import requests
import json
import webbrowser

# Entra Configuration
TENANT_ID = "3596192b-fdf5-4e2c-a6fa-acb706c963d8"
CLIENT_ID = "7529f416-6b98-41ed-a422-810985411305"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

app = msal.PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

# 1. Get your app token first
print("=== Getting your app token ===")

#flow = app.initiate_device_flow(scopes=[f"api://{CLIENT_ID}/my-scope-access"])
flow = app.initiate_device_flow(scopes=[f"{CLIENT_ID}/.default"])

print(flow["message"])
webbrowser.open(flow["verification_uri"]+f"?entercode={flow['user_code']}")
app_token_result = app.acquire_token_by_device_flow(flow)

if "access_token" not in app_token_result:
    print("Failed to get app token:", app_token_result.get("error_description"))
    exit(1)

print("✓ Got app token")

# Open app token in jwt.io
webbrowser.open(f"https://jwt.io/#token={app_token_result['access_token']}")
print("✓ Opened app token in jwt.io")

# 2. Now get Graph token (should be silent since user already logged in)
print("\n=== Getting Graph token ===")
graph_result = app.acquire_token_silent(
    scopes=["https://graph.microsoft.com/User.Read"],
    account=app.get_accounts()[0] if app.get_accounts() else None
)

if not graph_result:
    # Need interactive flow for Graph
    flow = app.initiate_device_flow(scopes=["https://graph.microsoft.com/User.Read"])
    print(flow["message"])
    webbrowser.open(flow["verification_uri"])
    graph_result = app.acquire_token_by_device_flow(flow)


# Open graph token in jwt.io
webbrowser.open(f"https://jwt.io/#token={graph_result['access_token']}")
print("✓ Opened graph token in jwt.io")

if "access_token" in graph_result:
    # 3. Fetch employeeId from Graph
    headers = {'Authorization': f'Bearer {graph_result["access_token"]}'}
    response = requests.get(
        "https://graph.microsoft.com/v1.0/me?$select=displayName,employeeId,mail",
        headers=headers
    )
    user_data = response.json()
    
    print(f"\n=== USER INFO ===")
    print(f"Name: {user_data.get('displayName')}")
    print(f"Employee ID: {user_data.get('employeeId')}")
    print(f"Email: {user_data.get('mail')}")
    
    # Save both tokens
    with open('tokens.json', 'w') as f:
        json.dump({
            'app_token': app_token_result,
            'graph_token': graph_result,
            'user_profile': user_data
        }, f, indent=4)
    print("\n✓ Tokens saved to tokens.json")
else:
    print("Failed to get Graph token:", graph_result.get("error_description"))
