# Simple Contact Management System

This project is a basic Contact Management System built with Django, allowing users to store, view, update, and delete contact information.

## Features

1. **Add Contact**  
   - Users can add new contacts via a form with fields for:
     - First Name
     - Last Name
     - Email
     - Phone Number
     - Address

2. **View Contacts**  
   - Homepage lists all saved contacts showing:
     - First Name
     - Email
     - Phone Number
   - Clicking on a contact's name opens a detailed view with full information.

3. **Edit Contact**  
   - Users can update their contact details.
   - The edit page pre-fills the form with the contact’s current details.

4. **Delete Contact**  
   - Users can delete any contact from the system.

5. **Search Contacts**  
   - Users can search contacts by name or email.

6. **Superuser Login**  
   - Admin credentials:
     - Username: `admin`
     - Password: `123`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nozibuddowla/contact_management_system.git
   cd contact_management_system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
   Provide the username `admin` and password `123` as credentials.

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open the application in your browser:
   ```
   http://127.0.0.1:8000/contacts/
   ```

## Project Structure

```
contact_management_system/
│-- contacts/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│-- contact_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│-- db.sqlite3
│-- manage.py
│-- requirements.txt
│-- README.md
```

## Usage

- Navigate to the homepage to see the contact list.
- Add new contacts via the "Add Contact" button.
- Edit or delete existing contacts using the respective buttons.

## License

This project is licensed under the MIT License.

---

Developed with ❤️ by Md. Nozib Ud dowla

