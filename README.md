# 🎭 SauceDemo UI Automation Project

A comprehensive UI automation testing suite for the [SauceDemo](https://www.saucedemo.com/) e-commerce platform. 
This project follows the **Page Object Model (POM)** design pattern to ensure high maintainability, scalability, and readability of test scripts.

---

## 🛠 Tech Stack
* **Python 3.12** — Core programming language.
* **Selenium WebDriver** — Browser automation engine.
* **Pytest** — Advanced testing framework.
* **Allure Report** — Professional visual reporting tool.
* **GitHub Actions** — Continuous Integration (CI) for automated test execution.

## 📁 Project Structure
```
project/
│
├── pages/
│ ├── saucedemo/
│ │ ├── login_page.py
│ │ ├── inventory_page.py
│ │ ├── cart_page.py
│ │ ├── checkout_page.py
│ │ ├── action_bot.py
│ │ ├── base_page.py
│ │ ├── types.py
│
├── tests/
│ ├── saucedemo/
│ │ ├── test_login.py
│ │ ├── test_inventory.py
│ │ ├── test_cart.py
│ │ ├── test_checkout.py
│ │ ├── test_e2e.py
│ │ ├── conftest.py
│
├── utils/
│ ├── chrome_driver.py
│ ├── firefox_driver.py
│ ├── constants.py
│
├── pytest.ini
├── README.md
```

## 📸 Allure Report

### 🔹 Overview
![Allure Overview](screenshots/overview.png)

### 🔹 Test Details
![Test Details](screenshots/overview_1.png)


## 🚀 Getting Started

### 1. Clone the repository:
```bash
git clone [https://github.com/NorayrQA/saucedemo-tests.git](https://github.com/NorayrQA/saucedemo-tests.git)
cd saucedemo-tests
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run tests
```bash
pytest
```

---

## ✅ Test Coverage

1.  **Authentication:** * Positive login with standard user.
    * Error handling for locked-out users.
    * Validation for empty username/password fields.
    * Handling incorrect credentials.
2.  **Inventory & Catalog:**
    * Product sorting logic (A to Z).
    * Verifying item details and counts.
3.  **Shopping Cart:**
    * Adding items to the cart and verifying the badge count.
    * Removing items from the cart.
4.  **Checkout Process:**
    * Successful End-to-End (E2E) purchase flow.
    * Form validation (missing last name or postal code).