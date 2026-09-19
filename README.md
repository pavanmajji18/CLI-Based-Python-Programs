# Python CLI Applications Suite

A comprehensive collection of 5 modular, Object-Oriented Python CLI programs built with clean architecture, robust input validation, custom exception hierarchies, and standardized logging.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Projects Overview](#-projects-overview)
  - [1. Cab Booking System](#1-cab-booking-system)
  - [2. E-Commerce Shopping Cart](#2-e-commerce-shopping-cart)
  - [3. E-Learning Platform](#3-e-learning-platform)
  - [4. Game Character System](#4-game-character-system)
  - [5. Online Food Ordering System](#5-online-food-ordering-system)
- [Key Design Patterns & Architecture](#-key-design-patterns--architecture)
- [Prerequisites & Installation](#-prerequisites--installation)
- [How to Run](#-how-to-run)
- [Summary Matrix](#-summary-matrix)

---

## 📌 Overview

This repository demonstrates practical implementations of core Object-Oriented Programming (OOP) concepts in Python. Each project is structured as a self-contained Python package with modular components, typed method contracts, input validation, custom error handling, and demo scripts using Python's standard `logging` library.

---

## 📁 Repository Structure

```directory
CLI based python programs/
├── Cab_Booking_System/
│   ├── cab_booking/
│   │   ├── __init__.py
│   │   ├── booking.py
│   │   └── vehicles.py
│   └── main.py
├── E-Commerce Shopping Cart/
│   ├── ecommerce/
│   │   ├── __init__.py
│   │   ├── cart.py
│   │   ├── exceptions.py
│   │   └── product.py
│   └── main.py
├── E-Learning Platform/
│   ├── elearning/
│   │   ├── __init__.py
│   │   ├── exceptions.py
│   │   └── models/
│   │       ├── __init__.py
│   │       ├── course.py
│   │       └── user.py
│   └── main.py
├── Game_Character_System/
│   ├── game_system/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── characters.py
│   └── main.py
└── Online Food Ordering System/
    ├── ordering/
    │   ├── __init__.py
    │   ├── exceptions.py
    │   ├── models.py
    │   └── service.py
    └── main.py
```

---

## 🚀 Projects Overview

### 1. Cab Booking System
📁 Path: `Cab_Booking_System/`

A ride-hailing simulation model featuring fleet registration, distance-based fare calculation, and ride dispatching across different vehicle types.

- **Key Classes**:
  - `Vehicle` (Base class with input validation & fare calculation)
  - `Car` (Derived class with default rate ₹20/km)
  - `Bike` (Derived class with default rate ₹10/km)
  - `BookingService` (Fleet and ride dispatch manager)
- **Features**:
  - Distance validation (must be > 0)
  - Registration lookup & non-existent vehicle handling
  - Detailed logging for trip initialization and receipts

```bash
cd "Cab_Booking_System"
python main.py
```

---

### 2. E-Commerce Shopping Cart
📁 Path: `E-Commerce Shopping Cart/`

An inventory-aware e-commerce shopping cart system with stock management, item removal, and checkout calculation.

- **Key Classes**:
  - `Product` (Item attributes, stock level, price in ₹)
  - `ShoppingCart` (Cart state, stock checking, subtotal/total calculation)
- **Custom Exception Hierarchy**:
  - `CartError` (Base exception)
    - `OutOfStockError`
    - `ProductNotFoundError`
    - `InvalidQuantityError`
- **Features**:
  - Stock auto-deduction upon successful checkout
  - Error recovery for out-of-stock or invalid operations
  - Dynamic cart summaries formatted in tabular log output

```bash
cd "E-Commerce Shopping Cart"
python main.py
```

---

### 3. E-Learning Platform
📁 Path: `E-Learning Platform/`

A domain-driven e-learning management platform showcasing user role inheritance, course creation, enrollment, and progress tracking.

- **Key Classes**:
  - `User` (Base class with profile representation & email validation)
  - `Instructor` (Derived class; creates and manages courses)
  - `Student` (Derived class; enrolls in courses & tracks progress percentage)
  - `Course` (Represents platform course metadata)
- **Custom Exceptions**:
  - `ELearningError`, `DuplicateEnrollmentError`, `CourseNotFoundError`, `InvalidInputError`
- **Features**:
  - Polymorphic user handling
  - Email format validation using regular expressions
  - Progress percentage boundary checks (0.0% - 100.0%)

```bash
cd "E-Learning Platform"
python main.py
```

---

### 4. Game Character System
📁 Path: `Game_Character_System/`

An RPG combat interaction framework highlighting inheritance, method overrides, resource management (arrows, mana, shield), and turn-based combat states.

- **Key Classes**:
  - `Character` (Base class with level, health, and combat methods)
  - `Warrior` (High defense, shield damage mitigation)
  - `Archer` (Ranged combat with finite arrow inventory)
  - `Wizard` (Magic user consuming mana per strike)
- **Custom Exceptions**:
  - `GameSystemError`, `InvalidAttributeError`, `CharacterDefeatedError`
- **Features**:
  - Automatic defeat state prevention (cannot attack or take damage when defeated)
  - Attribute guard rules (health > 0, level >= 1)
  - Damage mitigation calculation per character archetype

```bash
cd "Game_Character_System"
python main.py
```

---

### 5. Online Food Ordering System
📁 Path: `Online Food Ordering System/`

A restaurant ordering workflow service managing menus, customers, orders, item pricing in INR (₹), and itemized billing summaries.

- **Key Classes**:
  - `FoodItem` (Menu item with ID, name, category, and price)
  - `Restaurant` (Menu repository and lookup engine)
  - `Customer` (Customer profile & phone validation)
  - `Order` (Receipt generator & subtotal computation)
  - `FoodOrderingService` (Order processor)
- **Custom Exceptions**:
  - `FoodOrderingError`, `InvalidInputError`, `ItemNotFoundError`
- **Features**:
  - Mobile phone number validation (10-digit check)
  - Dynamic receipt generation with itemized lists
  - Graceful error handling for invalid menu item selection

```bash
cd "Online Food Ordering System"
python main.py
```

---

## 🛠️ Key Design Patterns & Architecture

1. **Inheritance & Polymorphism**: Used in `Vehicle`, `User`, and `Character` hierarchies to reuse common properties while overriding specialized behaviors.
2. **Custom Exception Hierarchies**: Every application defines application-specific custom exceptions inheriting from standard `Exception` to distinguish validation failures from unexpected runtime faults.
3. **Encapsulation & Validation**: Private/protected attributes with strict input assertion guards on object initialization.
4. **Structured Logging**: Built-in Python `logging` module is configured with custom formatters (`datefmt`, `levelname`, logger name) instead of simple print statements.
5. **Clean Modular Structure**: Separate package folders with `__init__.py` files allowing clean imports (`from package import Component`).

---

## 💻 Prerequisites & Installation

- **Python**: Version 3.8 or higher
- **Dependencies**: No third-party packages required! All programs use standard Python libraries (`logging`, `re`, `abc`, `typing`).

---

## ⚡ How to Run

Navigate to any project directory and run `main.py` with Python:

```bash
# Example 1: Run Cab Booking Demo
python "Cab_Booking_System/main.py"

# Example 2: Run E-Commerce Demo
python "E-Commerce Shopping Cart/main.py"

# Example 3: Run E-Learning Platform Demo
python "E-Learning Platform/main.py"

# Example 4: Run Game Character System Demo
python "Game_Character_System/main.py"

# Example 5: Run Food Ordering System Demo
python "Online Food Ordering System/main.py"
```

---

## 📊 Summary Matrix

| Application | Primary OOP Concepts | Custom Exceptions | Unique Mechanics |
| :--- | :--- | :--- | :--- |
| **Cab Booking System** | Inheritance, Composition | `ValueError` assertions | Rate-based fare calculation per KM |
| **E-Commerce Shopping Cart** | Encapsulation, State Management | `CartError`, `OutOfStockError` | Inventory deduction upon checkout |
| **E-Learning Platform** | Polymorphism, Domain Models | `ELearningError`, `DuplicateEnrollmentError` | Dynamic progress updates & email regex |
| **Game Character System** | Abstract Methods, State Logic | `GameSystemError`, `CharacterDefeatedError` | Resource consumption (Arrows/Mana) & Defeat tracking |
| **Online Food Ordering System** | Composition, Service Layer | `FoodOrderingError`, `InvalidInputError` | Phone validation & itemized receipt summary |
