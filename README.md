# Semantic-Music-quiz

## Installation

To launch the application, you'll need a `.env` file containing:

```
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=your_redirect_uri
```

Then, use the python `venv` to install the requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

## Starting

To start the program, use this command:

```bash
./quiz
```
