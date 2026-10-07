import requests
import json

BASE = "http://127.0.0.1:8000"

print("\n========================================")
print("   CART → CHECKOUT → ORDERS TEST")
print("========================================")

# -------------------------------------------------
# 1. CHECK PRODUCT
# -------------------------------------------------
print("\n===== 1. CHECKING PRODUCT =====")

r = requests.get(f"{BASE}/products/")
print("Status:", r.status_code)

try:
    products = r.json()
    print("Products available:", len(products))

    if isinstance(products, list) and products:
        product_id = products[0].get("id", 1)
        print("Using Product ID:", product_id)
    else:
        product_id = 1
except Exception:
    product_id = 1
    print("Using default Product ID:", product_id)


# -------------------------------------------------
# 2. GET CART
# -------------------------------------------------
print("\n===== 2. GET CART =====")

r = requests.get(f"{BASE}/cart/")
print("Status:", r.status_code)
print("Response:", r.text)


# -------------------------------------------------
# 3. ADD PRODUCT TO CART
# -------------------------------------------------
print("\n===== 3. ADD PRODUCT TO CART =====")

cart_data = {
    "product_id": product_id,
    "quantity": 1
}

print("Request:", json.dumps(cart_data, indent=2))

r = requests.post(
    f"{BASE}/cart/",
    json=cart_data
)

print("Status:", r.status_code)
print("Response:", r.text)


# -------------------------------------------------
# 4. VIEW CART AGAIN
# -------------------------------------------------
print("\n===== 4. CART AFTER ADDING PRODUCT =====")

r = requests.get(f"{BASE}/cart/")
print("Status:", r.status_code)
print("Response:", r.text)


# -------------------------------------------------
# 5. CHECKOUT
# -------------------------------------------------
print("\n===== 5. CHECKOUT =====")

r = requests.post(f"{BASE}/orders/checkout")

print("Status:", r.status_code)
print("Response:", r.text)

order_id = None

try:
    data = r.json()

    if isinstance(data, dict):
        order_id = (
            data.get("id")
            or data.get("order_id")
            or data.get("order", {}).get("id")
        )

    print("Detected Order ID:", order_id)

except Exception:
    print("Checkout response was not JSON.")


# -------------------------------------------------
# 6. GET ALL ORDERS
# -------------------------------------------------
print("\n===== 6. GET ALL ORDERS =====")

r = requests.get(f"{BASE}/orders/")
print("Status:", r.status_code)
print("Response:", r.text)


# -------------------------------------------------
# 7. GET SPECIFIC ORDER
# -------------------------------------------------
if order_id:

    print("\n===== 7. GET ORDER DETAILS =====")

    r = requests.get(f"{BASE}/orders/{order_id}")

    print("Status:", r.status_code)
    print("Response:", r.text)


    # -------------------------------------------------
    # 8. ORDER STATUS
    # -------------------------------------------------
    print("\n===== 8. GET ORDER STATUS =====")

    r = requests.get(
        f"{BASE}/orders/{order_id}/status"
    )

    print("Status:", r.status_code)
    print("Response:", r.text)


# -------------------------------------------------
# 9. NOTIFICATIONS
# -------------------------------------------------
print("\n===== 9. CHECK NOTIFICATIONS =====")

r = requests.get(f"{BASE}/notifications/")

print("Status:", r.status_code)
print("Response:", r.text)


print("\n========================================")
print("       CART/ORDER TEST COMPLETE")
print("========================================")
