# Automated Comment Filtering System

This project is an **Automated Comment Filtering System** designed to identify and block vulgar or inappropriate comments in ecommerce website. Clean comments are allowed to be posted, while flagged comments are stored for admin review. The project uses a SQLite database for storing flagged comments and a dataset of vulgar words for filtering.

## Features

- **Real-Time Comment Filtering:** Automatically checks comments for vulgar words and blocks inappropriate ones.
- **Admin Dashboard:** View and manage flagged comments.
- **Database Integration:** Stores flagged comments with their corresponding flagged words in a SQLite database.
- **User-Friendly Interface:** Simplified form for users to submit their comments or reviews.

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML
- **Libraries:** Pandas, Flask

## Directory Structure
vulnerability-detection/ 
├── app.py  # Main Flask application 
├── sample.py  # Utility script to check column names 
├── cleaned_vulgar_words.csv  # Dataset of vulgar words 
├── db.sqlite3   # SQLite database file 
├── templates/ 
├── comment_form.html  # HTML form for submitting comments  
├── admin_dashboard.html  # Admin dashboard for flagged comments 
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Usage
**Submit Comments:
Visit the homepage and enter your comment or review.
Clean comments will be displayed; flagged comments will be blocked.

**Admin Review:
Navigate to /admin to view flagged comments.
Delete inappropriate comments as necessary.

## Future Enhancements
1. Add CSS for improved UI.
2. Implement email notifications for admins.
3. Extend support for multiple languages.


## License
This project is licensed under the MIT License.


