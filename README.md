# Chess Tournament Manager - OpenClassrooms WPS | P3

This repository contains the completed offline tournament management application developed for Castle Chess and other regional clubs. The program is designed to run without internet access, making it ideal for venues with limited connectivity.

### Features

- Offline tournament management from start to finish
- Player registration and club management
- Round creation, match result entry, and automatic score updates
- Real-time player rankings and final standings
- Tournament reports with match history and final scores
- JSON-based data persistence with autosave after every change
- Clean, maintainable code following PEP 8 standards


### Project Structure

| Folder       | Purpose                                                                  |
| -------------| -------------------------------------------------------------------------|
| Models/      | Core data classes: Player, Club, Tournament, Round, Match                |
| Views/       | CLI views for user interaction and prompts                               |
| Services/    | Business logic and data persistence (e.g. saving/loading tournaments)    |
| data/        | Sample JSON files for clubs and tournaments                              |
| controllers/ | Main application logic and flow control                                  |
| .flake8      | Configuration for linting rules                                          |

*note, this program does not use the Screens or Commands folders from the starter code. 

### Installation & Setup

1. Clone the repository

https://github.com/OpenClassrooms-Student-Center/P3-Application-Developer-Skills-Bootcamp.git

2. 	Create a virtual environment

python -m venv .env

3. 	Activate the environment

- On Windows: .env\Scripts\activate
- On macOS/Linux: source .env/bin/activate

4. Install dependencies

pip install -r requirements.txt

### How to Use the Program

1. Run the main tournament file (this will run the controller)

python manage_tournaments.py

2. 	Follow the CLI prompts

- Select or create a tournament
- Register players from existing clubs
- Advance the round to start the first round
- Enter match results round by round
- View rankings and generate reports

3. 	Data is saved automatically

- Every change (player registration, match result, round advancement) is saved immediately to JSON files

### Code Quality & flake8 Report

This project uses flake8 and black to enforce clean code.

To generate a new flake8 HTML report:

1. Install flake8-html

pip install flake8-html

2. Run flake8 with HTML output

flake8 --format=html --htmldir=flake8-report

3. View the report

- Open flake8-report/index.html in your browser
- This shows all linting issues and file-by-file breakdown


