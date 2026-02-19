FocusList 📋
A modular Django-based task management system featuring custom request analysis and user authentication.


**🏗 Project Structure**
This project uses a decoupled architecture to keep logic organized:

core/: Project configuration (using split settings for base, local, and production).

task/: Main CRUD logic for task management and categories.

users/: Custom user profiles, signals, and authentication flow.

request_analysis/: Middleware-based tracking and admin statistics.


🚀 Getting Started

**1. Clone and Environment**
git clone https://github.com/your-username/FocusList.git
cd FocusList

**2. Configure Environment Variables**
**Copy the example template and fill in your local secrets:**

cp .env.example .env
Open .env and ensure SECRET_KEY is set and DEBUG=True for local development.

**3. Install Dependencies**
pip install -r requirements.txt

**4. Database Setup**
python manage.py migrate
python manage.py createsuperuser

**5. Run the Server**
python manage.py runserver


**🛠 Features**
Signals: Automatic profile creation and task notifications

Custom Middleware: Request analysis tracking via the request_analysis app

Dynamic Templates: Modular UI using base.html inheritance

Environment Safety: Sensitive Data is kept out of source control via .env