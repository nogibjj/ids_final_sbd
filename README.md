# Spotify Podcast Analytics Microservice
[![Install](https://github.com/nogibjj/ids_final_sbd/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/ids_final_sbd/actions/workflows/install.yml)
[![Install](https://github.com/nogibjj/ids_final_sbd/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/ids_final_sbd/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/ids_final_sbd/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/ids_final_sbd/actions/workflows/test.yml)
[![Install](https://github.com/nogibjj/ids_final_sbd/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/ids_final_sbd/actions/workflows/lint.yml)

![alt text](https://github.com/nogibjj/ids_final_sbd/blob/main/images_rm/preview_app.png?raw=true)
The Spotify Podcast Analytics Microservice is a Flask-based web application designed to analyze and present insights into the top 200 Spotify podcasts in the US. This microservice focuses on providing information about the top 10 podcasts based on different criteria, allowing users to explore alternative rankings. The web app is available at: [https://alterschart.azurewebsites.net/](https://alterschart.azurewebsites.net/)


### Features
#### Filtering Options:
- Users can filter podcasts based on three criteria: Spotify ranking, longest average time of episodes, or episode count.
The filter is applied through radio buttons for each criterion.
#### Top 10 Podcasts Display:
- The microservice displays the top 10 podcasts based on the selected filter criteria.
- Podcast details include the show name, total number of episodes, average length of episodes, an external link to the podcast, and a brief description.
#### Episode Previews:
  - Users can preview the last three episodes of each podcast using embedded audio players.
  - The audio files are sourced from the provided URLs.


## Video presentation
Watch the video presentation [here](https://youtu.be/KZIzitQN4ss) 


## Microservice

The microservice is built using Flask, providing a web interface to explore podcast analytics. It reads data from a preprocessed dataset (top_200.parquet) containing information about the top 200 Spotify podcasts in the US. The microservice is successfully deployed via Azure Web App to a public endpoint. It is hosted on [Azure Web App URL](https://alterschart.azurewebsites.net/). The Docker container for the microservice is hosted on DockerHub. 

### Code Overview
- #### Flask Application Setup:
The microservice is initialized as a Flask application.
The top 200 Spotify podcasts dataset is loaded from a Parquet file (data/top_200.parquet).
- #### Routing and Filtering:
The / route handles both GET and POST requests.
Users can select a ranking type (Spotify, time, or episodes) through a form and apply the filter.
- #### Data Engineering
The project involves the use of Pandas for data engineering. It retrieves information about the top 200 Spotify podcasts and their episodes from the Spotify API. This dataset is used as the datasource in  the microservice. The microservice reads data from a Parquet dataset, ensuring efficient data retrieval and presentation abd the top 10 podcasts are filtered based on the user's selected ranking type. A dictionary (shows_and_data) is constructed to store information about each podcast, including URLs for episode previews.
- #### HTML Rendering:
The web interface is rendered using the render_template function, with the HTML template located at templates/index3.html.
The template includes sections for filtering, podcast details, and episode previews.

### Development Environment
- Language: Python
- Framework: Flask

## Load Test

The microservice is capable of handling 1341 requests per second.

![alt text](https://github.com/nogibjj/ids_final_sbd/blob/main/images_rm/load_test1.png?raw=true)



## Infrastructure as Code (IaC)

A CI/CD pipeline includes actions for installation, linting, testing, and formatting (review the badges on top of this readme).


## Architectural Diagram

![image](https://github.com/nogibjj/ids_final_sbd/assets/143829673/3c60f0ba-8e69-4a60-af33-2e61d846cbfb)


## GitHub Configurations
The GitHub repository includes GitHub Actions and a .devcontainer configuration for GitHub Codespaces. This ensures the local version of the project is reproducible. GitHub Action build badges for install, lint, test, and format actions are also present.

## Teamwork Reflection

Each team member should submit a separate 1-2 page management report reflecting on the team's functioning. The report includes a reflection on teamwork principles, a peer evaluation with three positive attributes and three areas for improvement, and the outcome of the feedback session with the team.

## Installation

- Clone the repository to your local machine:
```
git clone [https://github.com/nogibjj/ids_final_sbd](https://github.com/nogibjj/ids_final_sbd)
```
- Install the required dependencies:
```
pip install -r requirements.txt
```
## Usage
(Ensure you have the required environment variables set for Spotify API access.)
Run the main data retrieval script:
```
python main.py
```
Run the Flask web application:
```
python app3.py
```

Visit http://localhost:5000/ in your web browser to explore the analytics.


