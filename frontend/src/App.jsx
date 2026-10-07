import React, { useState } from "react";
import "./App.css";

const products = [
  {
    id: 1,
    name: "Premium Wireless Headphones",
    category: "Electronics",
    price: 5999,
    stock: 24,
    icon: "🎧",
  },
  {
    id: 2,
    name: "Smart Watch Pro",
    category: "Electronics",
    price: 7999,
    stock: 18,
    icon: "⌚",
  },
  {
    id: 3,
    name: "Mechanical Keyboard",
    category: "Accessories",
    price: 4499,
    stock: 12,
    icon: "⌨️",
  },
  {
    id: 4,
    name: "Premium Backpack",
    category: "Lifestyle",
    price: 2999,
    stock: 31,
    icon: "🎒",
  },
  {
    id: 5,
    name: "Running Shoes",
    category: "Fashion",
    price: 3499,
    stock: 15,
    icon: "👟",
  },
];

function App() {
  const [activePage, setActivePage] = useState("Dashboard");

  const stats = [
    {
      title: "Total Users",
      value: "6",
      change: "12%",
      icon: "👥",
    },
    {
      title: "Total Products",
      value: "5",
      change: "8%",
      icon: "📦",
    },
    {
      title: "Total Orders",
      value: "0",
      change: "5%",
      icon: "🛍️",
    },
    {
      title: "Total Sales",
      value: "₹59,990",
      change: "15%",
      icon: "₹",
    },
  ];

  const menuItems = [
    { name: "Dashboard", icon: "⌂" },
    { name: "Products", icon: "▣" },
    { name: "Cart", icon: "🛒" },
    { name: "Orders", icon: "▤" },
    { name: "Notifications", icon: "🔔" },
    { name: "Admin", icon: "⚙" },
  ];

  return (
    <div className="app-container">

      {/* SIDEBAR */}
      <aside className="sidebar">

        <div className="brand">
          <div className="brand-logo">S</div>
          <div>
            <h2>SmartCart</h2>
            <p>E-Commerce Platform</p>
          </div>
        </div>

        <div className="menu-title">MAIN MENU</div>

        <nav className="sidebar-menu">
          {menuItems.map((item) => (
            <button
              key={item.name}
              className={`menu-item ${
                activePage === item.name ? "active" : ""
              }`}
              onClick={() => setActivePage(item.name)}
            >
              <span className="menu-icon">{item.icon}</span>
              <span>{item.name}</span>
            </button>
          ))}
        </nav>

        <div className="sidebar-profile">
          <div className="profile-avatar">G</div>
          <div>
            <strong>Ganesh</strong>
            <span>Administrator</span>
          </div>
        </div>

      </aside>

      {/* MAIN CONTENT */}
      <main className="main-content">

        {/* HEADER */}
        <header className="top-header">

          <div>
            <h1>{activePage}</h1>
            <p>
              {activePage === "Dashboard"
                ? "Welcome back! Here's what's happening today."
                : `Manage your ${activePage.toLowerCase()} here.`}
            </p>
          </div>

          <div className="header-right">

            <button className="notification-button">
              🔔
              <span className="notification-count">3</span>
            </button>

            <div className="header-user">
              <div className="header-avatar">G</div>
              <div>
                <strong>Ganesh</strong>
                <span>Admin</span>
              </div>
            </div>

          </div>

        </header>

        {/* DASHBOARD */}
        {activePage === "Dashboard" && (
          <>

            {/* STAT CARDS */}
            <section className="stats-grid">

              {stats.map((stat) => (
                <div className="stat-card" key={stat.title}>

                  <div className="stat-card-top">
                    <div>
                      <p className="stat-title">{stat.title}</p>
                      <h2>{stat.value}</h2>
                    </div>

                    <div className="stat-icon">
                      {stat.icon}
                    </div>
                  </div>

                  <p className="stat-change">
                    ↑ {stat.change} this month
                  </p>

                </div>
              ))}

            </section>

            {/* LOWER CONTENT */}
            <section className="content-grid">

              {/* POPULAR PRODUCTS */}
              <div className="panel products-panel">

                <div className="panel-header">
                  <div>
                    <h2>Popular Products</h2>
                    <p>Top products in your store</p>
                  </div>

                  <button className="view-button">
                    View all →
                  </button>
                </div>

                <div className="products-list">

                  {products.slice(0, 4).map((product) => (
                    <div className="product-row" key={product.id}>

                      <div className="product-icon">
                        {product.icon}
                      </div>

                      <div className="product-info">
                        <strong>{product.name}</strong>
                        <span>{product.category}</span>
                      </div>

                      <strong className="product-price">
                        ₹{product.price.toLocaleString("en-IN")}
                      </strong>

                      <span className="stock-badge">
                        In Stock
                      </span>

                    </div>
                  ))}

                </div>

              </div>

              {/* QUICK ACTIONS */}
              <div className="panel actions-panel">

                <div className="panel-header">
                  <div>
                    <h2>Quick Actions</h2>
                    <p>Manage your platform</p>
                  </div>
                </div>

                <div className="quick-actions">

                  <button onClick={() => setActivePage("Products")}>
                    <span>＋</span>
                    Add / View Products
                  </button>

                  <button onClick={() => setActivePage("Orders")}>
                    <span>▣</span>
                    Manage Orders
                  </button>

                  <button
                    onClick={() => setActivePage("Notifications")}
                  >
                    <span>🔔</span>
                    View Notifications
                  </button>

                  <button onClick={() => setActivePage("Admin")}>
                    <span>⚙</span>
                    Admin Dashboard
                  </button>

                </div>

              </div>

            </section>
          </>
        )}

        {/* PRODUCTS PAGE */}
        {activePage === "Products" && (
          <section className="page-section">

            <div className="page-title-row">
              <div>
                <h2>Products</h2>
                <p>Manage all products in your store.</p>
              </div>

              <button className="primary-button">
                + Add Product
              </button>
            </div>

            <div className="full-products-grid">

              {products.map((product) => (
                <div className="product-card" key={product.id}>

                  <div className="large-product-icon">
                    {product.icon}
                  </div>

                  <h3>{product.name}</h3>
                  <p>{product.category}</p>

                  <div className="product-card-bottom">
                    <strong>
                      ₹{product.price.toLocaleString("en-IN")}
                    </strong>

                    <span className="stock-badge">
                      {product.stock} in stock
                    </span>
                  </div>

                </div>
              ))}

            </div>

          </section>
        )}

        {/* CART PAGE */}
        {activePage === "Cart" && (
          <section className="empty-page">

            <div className="empty-icon">🛒</div>
            <h2>Your Cart</h2>
            <p>
              No products have been added to the cart yet.
            </p>

          </section>
        )}

        {/* ORDERS PAGE */}
        {activePage === "Orders" && (
          <section className="empty-page">

            <div className="empty-icon">📦</div>
            <h2>Orders</h2>
            <p>
              No orders have been placed yet.
            </p>

          </section>
        )}

        {/* NOTIFICATIONS PAGE */}
        {activePage === "Notifications" && (
          <section className="page-section">

            <div className="page-title-row">
              <div>
                <h2>Notifications</h2>
                <p>Recent platform notifications.</p>
              </div>
            </div>

            <div className="notification-card">
              <span>🔔</span>
              <div>
                <strong>Welcome to SmartCart</strong>
                <p>
                  Your e-commerce administration platform is ready.
                </p>
              </div>
            </div>

            <div className="notification-card">
              <span>📦</span>
              <div>
                <strong>Products Updated</strong>
                <p>
                  Product inventory has been successfully updated.
                </p>
              </div>
            </div>

            <div className="notification-card">
              <span>👥</span>
              <div>
                <strong>User Activity</strong>
                <p>
                  New users have registered on the platform.
                </p>
              </div>
            </div>

          </section>
        )}

        {/* ADMIN PAGE */}
        {activePage === "Admin" && (
          <section className="page-section">

            <div className="admin-box">

              <div className="admin-avatar">
                G
              </div>

              <h2>Admin Dashboard</h2>

              <p>
                Welcome, <strong>Ganesh</strong>.
              </p>

              <div className="admin-details">

                <div>
                  <span>Role</span>
                  <strong>Administrator</strong>
                </div>

                <div>
                  <span>Platform</span>
                  <strong>SmartCart</strong>
                </div>

                <div>
                  <span>Access</span>
                  <strong>Full Access</strong>
                </div>

              </div>

            </div>

          </section>
        )}

      </main>

    </div>
  );
}

export default App;