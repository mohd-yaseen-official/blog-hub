# 📝 Bloghub

**Bloghub** is a fully functional blogging platform built with Django. It supports user authentication, blog creation, editing, deletion, pagination, search, and category filtering. The project follows a modular approach for scalability and easy maintenance.

---

## 🚀 Features

- 🔐 **User Authentication** (Login, Register, Logout)
- ✍️ **Create, Edit, and Delete Blog Posts**
- 🗂 **Category-Based Filtering for Blogs**
- 🔎 **Search Functionality** for blog titles and content
- 📄 **Paginated Blog Listing** for easy navigation
- 🧾 **Admin Panel** for blog management and user control
- 📂 Modular Django Apps: `web`, `users`, `main`, `posts`

---

## 🛠 Tech Stack

- Python 3
- Django
- SQLite (default, but can be switched to PostgreSQL)
- HTML, CSS, JavaScript
---

## 📁 Project Structure

blog-hub/
├── src/
│   ├── bloghub/             # Django project configuration (settings, urls, wsgi)
│   ├── web/                 # Views for the landing page, home, etc.
│   ├── users/               # Authentication logic (login, register, logout)
│   ├── main/                # Core functionality (base views, site settings)
│   └── posts/               # Blog-related views, models, and posts handling
├── templates/
│   ├── blog/
│   ├── users/
│   └── web/
├── static/                # Static files (CSS, JavaScript)
├── media/                 # Uploaded images, media files
├── requirements.txt       # Project dependencies
├── manage.py              # Django management script
└── README.md              # Project documentation


---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/bloghub.git](https://github.com/your-username/bloghub.git)
cd bloghub
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Create a `.env` file in the root directory and add:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DB_NAME=event_ease
DB_USER=postgres
DB_PASSWORD=admin
DB_HOST=localhost
DB_PORT=5432
```
### 5. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Create a superuser (optional but recommended)

```bash
python manage.py createsuperuser
```
### 7. Start the development server
```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the app.

---

## 🔍 Usage Highlights
✨ Home page displays the latest blog posts with pagination.

📑 Filter blogs by category from the navigation bar or sidebar.

🔍 Search by blog title or content using the search bar.

✏️ Authenticated users can create, edit, or delete their blogs.

🧾 Admin panel allows full control over users and blog posts.

## 🤝 Contributing
Feel free to fork the repo and submit a pull request. For major changes, please open an issue first to discuss what you’d like to implement.

---
## ✨ Credits
Developed with ❤️ by Mohamed Yaseen
