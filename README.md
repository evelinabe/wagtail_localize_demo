# Wagtail Localize Demo

This is a basic demo project to showcase the capabilities of Wagtail Localize.

## Requirements

- Python 3.8+
- Django 4.2+
- Wagtail 6.2+
- wagtail-localize

## Installation

1. **Clone the repository**:

   ```sh
   git clone https://github.com/evelinabe/wagtail_localize_demo.git
   cd wagtail_localize_demo

  ```

2. **Create and activate a virtual environment**:
  ```sh
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 ```

3. **Install the dependencies**:

  ```sh
  pip install -r requirements.txt
  ```

4. **Apply migrations**:

  ```sh
  python manage.py migrate
  ```

5. **Create a superuser**:

  ```sh
  python manage.py createsuperuser
  ```

6. **Run the development server**:

  ```sh
  python manage.py runserver
  ```
