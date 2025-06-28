# 🏃‍♀️ Personal Fitness & Calorie Tracker

This is a Django-based web application that allows users to:

- Add and view calorie intake and burn data
- Track daily net calories
- Download entries as a CSV file
- Visualize entries with a clean, user-friendly interface

## 💻 Tech Stack

- Python 3
- Django Framework
- HTML5 & CSS3 (with external stylesheet)
- SQLite3 (default Django database)
- Bootstrap-like modern styling (via custom CSS)
- Git for version control

## 🛠 Features

- Add food intake or workout (burn) entries
- View totals for intake, burn, and net calories
- Delete individual entries
- Export your data as a downloadable CSV file
- Responsive, mobile-friendly design

## 🚀 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/fitness-tracker.git
   cd fitness-tracker
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

6. Open in your browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📁 Project Structure

- `tracker/` – App containing models, views, templates
- `templates/` – HTML templates
- `static/` – CSS files
- `db.sqlite3` – SQLite database (not recommended to push to GitHub)
- `.gitignore` – To ignore compiled and environment files

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Happy tracking!