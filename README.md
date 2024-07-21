# Django Project: Blog, Gift Card Shop, and Udemy Course Search

This Django project integrates a blog, an online shop for selling gift card codes or combos, and a search engine for free courses on Udemy.

## Features

- **Blog**:
  - Create, edit, and delete blog posts.
  - Comment on blog posts.
  - Browse through a collection of insightful articles.

- **Gift Card Shop**:
  - Purchase gift card codes or combos securely.
  - Add items to the cart and complete transactions.
  - Explore various gift card options.

- **Udemy Course Search Engine**:
  - Search for free courses on Udemy by keyword or category.
  - View course details and direct links to Udemy for enrollment.
  - Stay updated with the latest free courses available.

## Usage

Explore the functionalities of this project:

- **Blog**: Visit `/blog` to read and contribute blog posts.
- **Gift Card Shop**: Browse the shop at `/shop` to purchase gift card codes.
- **Udemy Course Search**: Use the search at `/courses` to find free courses on Udemy.

## Installation

Follow these steps to set up and run the Django project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/AyyoubSghuri/django-project.git
   cd django-project
   ```
Set up a virtual environment (optional but recommended):

```bash
python -m venv env
source env/bin/activate  # On Windows: `env\Scripts\activate`
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open http://localhost:8000/ in your web browser to access the project.
