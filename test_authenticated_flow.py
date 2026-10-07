import requests
import json
import sys

BASE = "http://127.0.0.1:8000"

EMAIL = "demo@smartecommerce.com"
PASSWORD = "Demo@12345"
NAME = "Demo User"

print("\n========================================")
print("   AUTHENTICATED E-COMMERCE FLOW TEST")
print("========================================")

session = requests.Session()


# ============================================================
# HELPER
# ============================================================

def show(title, response):
    print(f"\n===== {title} =====")
    print("Status:", response.status_code)
    print("Response:", response.text[:3000])


# ============================================================
# 1. READ OPENAPI
# ============================================================

print("\n===== 1. READING API SCHEMAS =====")

try:
    openapi = session.get(f"{BASE}/openapi.json").json()
    print("OpenAPI loaded successfully.")
except Exception as e:
    print("Could not load OpenAPI:", e)
    sys.exit()


# ============================================================
# 2. FIND REQUEST FORMAT
# ============================================================

def get_request_info(path, method):
    endpoint = openapi.get("paths", {}).get(path, {})
    details = endpoint.get(method.lower(), {})

    body = details.get("requestBody", {})
    content = body.get("content", {})

    if not content:
        return None, None

    content_type = next(iter(content.keys()))
    schema = content[content_type].get("schema", {})

    return content_type, schema


# ============================================================
# 3. BUILD AUTH PAYLOAD DYNAMICALLY
# ============================================================

def build_payload(path, method):
    content_type, schema = get_request_info(path, method)

    if not schema:
        return {}, None

    properties = schema.get("properties", {})

    # Resolve referenced schema
    if "$ref" in schema:
        ref = schema["$ref"]
        schema_name = ref.split("/")[-1]
        schema = openapi.get("components", {}).get(
            "schemas", {}
        ).get(schema_name, {})

        properties = schema.get("properties", {})

    payload = {}

    for field in properties:

        field_lower = field.lower()

        if field_lower in ["email", "email_address"]:
            payload[field] = EMAIL

        elif field_lower in ["password", "pass", "pwd"]:
            payload[field] = PASSWORD

        elif field_lower in ["name", "full_name", "username"]:
            payload[field] = NAME

        elif field_lower == "first_name":
            payload[field] = "Demo"

        elif field_lower == "last_name":
            payload[field] = "User"

        elif field_lower == "role":
            payload[field] = "customer"

    return payload, content_type


# ============================================================
# 4. REGISTER
# ============================================================

register_payload, register_type = build_payload(
    "/auth/register",
    "post"
)

print("\n===== 2. REGISTER USER =====")
print("Payload:", json.dumps(register_payload, indent=2))
print("Content-Type:", register_type)

if "form" in str(register_type):
    r = session.post(
        f"{BASE}/auth/register",
        data=register_payload
    )
else:
    r = session.post(
        f"{BASE}/auth/register",
        json=register_payload
    )

show("REGISTER RESULT", r)


# ============================================================
# 5. LOGIN
# ============================================================

login_payload, login_type = build_payload(
    "/auth/login",
    "post"
)

print("\n===== 3. LOGIN USER =====")
print("Payload:", json.dumps(login_payload, indent=2))
print("Content-Type:", login_type)

if "form" in str(login_type):
    r = session.post(
        f"{BASE}/auth/login",
        data=login_payload
    )
else:
    r = session.post(
        f"{BASE}/auth/login",
        json=login_payload
    )

show("LOGIN RESULT", r)


# ============================================================
# 6. EXTRACT JWT
# ============================================================

token = None

try:
    login_data = r.json()

    possible_keys = [
        "access_token",
        "token",
        "jwt",
        "accessToken"
    ]

    for key in possible_keys:
        if login_data.get(key):
            token = login_data[key]
            break

    # Sometimes token may be nested
    if not token:
        for value in login_data.values():
            if isinstance(value, dict):
                for key in possible_keys:
                    if value.get(key):
                        token = value[key]
                        break

except Exception:
    pass


if not token:

    # Registration may have returned a token
    try:
        register_data = session.post(
            f"{BASE}/auth/login",
            json=login_payload
        ).json()

        for key in [
            "access_token",
            "token",
            "jwt",
            "accessToken"
        ]:
            if register_data.get(key):
                token = register_data[key]
                break

    except Exception:
        pass


if not token:

    print("\n❌ JWT TOKEN NOT FOUND")
    print("Authentication needs inspection before continuing.")
    sys.exit()


print("\n===== 4. JWT FOUND =====")
print("Token received successfully.")
print("Token preview:", token[:30] + "...")


# ============================================================
# 7. ATTACH JWT
# ============================================================

session.headers.update({
    "Authorization": f"Bearer {token}"
})

print("\nJWT attached to all future requests.")


# ============================================================
# 8. PRODUCTS
# ============================================================

print("\n===== 5. CHECK PRODUCTS =====")

r = session.get(f"{BASE}/products/")
show("PRODUCTS", r)

product_id = 1

try:
    products = r.json()

    if isinstance(products, list) and products:
        product_id = products[0].get("id", 1)

    elif isinstance(products, dict):
        items = (
            products.get("items")
            or products.get("products")
            or []
        )

        if items:
            product_id = items[0].get("id", 1)

except Exception:
    pass

print("Using Product ID:", product_id)


# ============================================================
# 9. GET CART
# ============================================================

r = session.get(f"{BASE}/cart/")
show("GET CART", r)


# ============================================================
# 10. ADD TO CART
# ============================================================

cart_payload = {
    "product_id": product_id,
    "quantity": 1
}

print("\nCart payload:")
print(json.dumps(cart_payload, indent=2))

r = session.post(
    f"{BASE}/cart/",
    json=cart_payload
)

show("ADD TO CART", r)


# ============================================================
# 11. GET CART AGAIN
# ============================================================

r = session.get(f"{BASE}/cart/")
show("CART AFTER ADD", r)


# ============================================================
# 12. CHECKOUT
# ============================================================

r = session.post(
    f"{BASE}/orders/checkout"
)

show("CHECKOUT", r)


# ============================================================
# 13. GET ORDERS
# ============================================================

r = session.get(
    f"{BASE}/orders/"
)

show("MY ORDERS", r)


# ============================================================
# 14. FIND ORDER ID
# ============================================================

order_id = None

try:
    data = r.json()

    if isinstance(data, list) and data:
        order_id = data[0].get("id") or data[0].get("order_id")

    elif isinstance(data, dict):

        order_id = (
            data.get("id")
            or data.get("order_id")
        )

        if not order_id:
            orders = data.get("orders", [])

            if orders:
                order_id = (
                    orders[0].get("id")
                    or orders[0].get("order_id")
                )

except Exception:
    pass


# ============================================================
# 15. ORDER DETAILS + STATUS
# ============================================================

if order_id:

    print("\nDetected Order ID:", order_id)

    r = session.get(
        f"{BASE}/orders/{order_id}"
    )

    show("ORDER DETAILS", r)

    r = session.get(
        f"{BASE}/orders/{order_id}/status"
    )

    show("ORDER STATUS", r)

else:
    print("\nNo Order ID detected.")


# ============================================================
# 16. NOTIFICATIONS
# ============================================================

r = session.get(
    f"{BASE}/notifications/"
)

show("NOTIFICATIONS", r)


# ============================================================
# FINAL
# ============================================================

print("\n========================================")
print("   AUTHENTICATED FLOW TEST COMPLETE")
print("========================================")

print("""
FLOW TESTED:

AUTH REGISTER
      ↓
AUTH LOGIN
      ↓
JWT AUTHENTICATION
      ↓
PRODUCTS
      ↓
CART
      ↓
CHECKOUT
      ↓
ORDERS
      ↓
ORDER STATUS
      ↓
NOTIFICATIONS
""")
