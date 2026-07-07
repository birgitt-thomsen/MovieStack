# 🎬 MovieStack

MovieStack is a Flask web application that allows users to build and manage their own collection of favorite movies.

Users can create personal movie lists, search for movies using the OMDb API, and keep their collections up to date through an intuitive web interface.

## Features

- Create and manage multiple users
- Add movies to a user's collection
- Automatically retrieve movie information from the OMDb API
- Edit movie titles
- Delete movies from a collection
- Responsive card-based interface built with HTML and CSS
- SQLite database using SQLAlchemy ORM

## Technologies

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML5
- CSS3
- Requests
- OMDb API

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd MovieStack
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file containing your OMDb API key:

```text
API_KEY=your_api_key_here
```

Run the application:

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

## Project Structure

```
MovieStack/
│
├── data/
│   └── moviestack.db
│
├── static/
│   ├── style.css
│   └── images/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── movies.html
│
├── app.py
├── data_manager.py
├── models.py
├── movie_service.py
├── requirements.txt
└── README.md
```

## Future Improvements

- Display movie genres and IMDb ratings
- Add movie search suggestions
- Pagination for large collections
- Sort and filter movie lists
- - User authentication

## Credits

Movie information provided by the OMDb API.

---

Developed by Birgitt Thomsen using Flask, SQLAlchemy, and the OMDb API.