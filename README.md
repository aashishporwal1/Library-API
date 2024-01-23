# Library-API

This is a Django project implementing an API for managing library and associated details using Django Rest Framework.
In this project, there is one admin who can create different genres of books like,fiction, documentary etc. An Author can sign up by adding his name,phone, email, City profile image.
A registered author can add multiple books that belong to him by adding this information: Book name, Genre ,number of pages, book cover image.

# Installations

1. Clone the repository:
   
    Command : 1. git clone https://github.com/aashishporwal1/Library-API.git
			  2. cd Library-API

2. Create virtual environment (optional but recommended):

    Command - python -m venv venv

3. Activate virtual environment:

	On Windows: $.\venv\Scripts\activate
	On macOS/Linux: $source venv/bin/activate

4. Install dependencies:

	Command: pip install -r requirements.txt

5. Apply migrations:

	Command: python manage.py migrate

6. Run the development server:

	Command: python manage.py runserver
