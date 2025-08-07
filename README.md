# CS50W Commerce - Electronic Auctions Application

An e-commerce auction platform inspired by eBay, built as part of Harvard's **CS50's Web Programming with Python and JavaScript** course. This web application allows registered users to post auction listings, place bids, comment on listings, and manage a personal watchlist.

## 🚀 Features

- **User Authentication:** Complete registration, login, and logout functionalities to ensure secure interactions.
- **Create Listings:** Authenticated users can create new auction listings by providing a title, text description, a starting bid, and an optional image URL or category.
- **Active Listings Page:** The default route displays all currently active auction listings, showing their titles, descriptions, current prices, and photos.
- **Listing Page:** Clicking on a listing takes the user to its dedicated page where they can:
  - View all specific details and the user who posted it.
  - Add or remove the item from their personal **Watchlist**.
  - Place a bid (validated to ensure it is higher than the starting price and all previous bids).
  - Read and post comments regarding the item.
  - **Close the auction:** If the user is the creator of the listing, they can close the auction at any time, making the highest bidder the official winner.
- **Watchlist:** A dedicated space where users can view all the active listings they are currently tracking.
- **Categories:** A filter system that categorizes products dynamically, allowing users to browse listings by specific topics (e.g., Electronics, Fashion, Home).
- **Django Admin Interface:** Full integration with the built-in Django administration panel to add, view, edit, and delete any listings, comments, users, and bids manually.

## 🛠️ Tech Stack

- **Backend:** Python, Django framework
- **Database:** SQLite (managed via Django Object-Relational Mapping - ORM)
- **Frontend:** HTML5, CSS3, Bootstrap framework, JavaScript

## 📦 Installation and Local Setup

Follow these steps to get this project running on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ArturPereira3012/cs50w-commerce.git](https://github.com/ArturPereira3012/cs50w-commerce.git)
   cd cs50w-commerce

2.  **Create and activate a virtual environment (Recommended) **:
Windows:
Bash
python -m venv venv
.\venv\Scripts\activate

Mac/Linux:
Bash
python -m venv venv
source venv/bin/activate

3.Install the required packages:
pip install django


4. Apply database migrations:
Run the following commands to create the database schema and initialize the built-in Django tables:
python manage.py makemigrations
python manage.py migrate


5. Create an admin user (Optional but recommended):
To access the Django Admin panel at /admin and manage database records easily, create a superuser account:
python manage.py createsuperuser

6. Start the development server:
python manage.py runserver


7. Access the application:
Open your preferred web browser and navigate to http://127.0.0.1:8000/.

This project was developed as an academic assignment for the CS50W course, fulfilling all the strict design specifications provided by Harvard University.
   
