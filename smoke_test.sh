#!/bin/bash

BASE="http://127.0.0.1:8000"

echo ""
echo "======================================"
echo "   SMART E-COMMERCE SMOKE TEST"
echo "======================================"

echo ""
echo "===== 1. ROOT ====="
curl -s "$BASE/" | python -m json.tool 2>/dev/null || curl -s "$BASE/"

echo ""
echo "===== 2. HEALTH ====="
curl -s "$BASE/health" | python -m json.tool 2>/dev/null || curl -s "$BASE/health"

echo ""
echo "===== 3. PRODUCTS ====="
curl -s "$BASE/products/" | python -m json.tool 2>/dev/null || curl -s "$BASE/products/"

echo ""
echo "===== 4. PRODUCTS SORTED ====="
curl -s "$BASE/products/?sort=latest" | python -m json.tool 2>/dev/null || curl -s "$BASE/products/?sort=latest"

echo ""
echo "===== 5. CART ====="
curl -s "$BASE/cart/" | python -m json.tool 2>/dev/null || curl -s "$BASE/cart/"

echo ""
echo "===== 6. ORDERS ====="
curl -s "$BASE/orders/" | python -m json.tool 2>/dev/null || curl -s "$BASE/orders/"

echo ""
echo "===== 7. NOTIFICATIONS ====="
curl -s "$BASE/notifications/" | python -m json.tool 2>/dev/null || curl -s "$BASE/notifications/"

echo ""
echo "===== 8. ADMIN DASHBOARD ====="
curl -s "$BASE/admin/dashboard" | python -m json.tool 2>/dev/null || curl -s "$BASE/admin/dashboard"

echo ""
echo "===== 9. ADMIN USERS ====="
curl -s "$BASE/admin/users" | python -m json.tool 2>/dev/null || curl -s "$BASE/admin/users"

echo ""
echo "======================================"
echo "   SMOKE TEST COMPLETE"
echo "======================================"
