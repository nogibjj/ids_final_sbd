# Spotify Podcast Analytics Microservice
[![Install](https://github.com/nogibjj/ids_final_sbd/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/ids_final_sbd/actions/workflows/install.yml)
[![Install](https://github.com/nogibjj/ids_final_sbd/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/ids_final_sbd/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/ids_final_sbd/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/ids_final_sbd/actions/workflows/test.yml)
[![Install](https://github.com/nogibjj/ids_final_sbd/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/ids_final_sbd/actions/workflows/lint.yml)


This microservice provides analytics for the top 200 Spotify podcasts in the US. It utilizes Flask for web interaction and Pandas for data processing. The data is obtained through the Spotify API and transformed into insightful analytics where the user selects alternative Top 10 filters that are not avaiable on the official Spotify Charts. The web app was is available at: [https://alterschart.azurewebsites.net/](https://alterschart.azurewebsites.net/)

## Table of Contents

- Installation
- Usage
- Microservice
- Load Test
- Data Engineering
- Infrastructure as Code (IaC)
- Continuous Integration and Continuous Delivery (CI/CD)
- Architectural Diagram
- GitHub Configurations
- Teamwork Reflection
- License

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

## Microservice

The microservice is built using Flask, providing a web interface to explore podcast analytics. It reads data from a preprocessed dataset (top_200.parquet) containing information about the top 200 Spotify podcasts in the US.

### Development Environment
- Language: Python
- Framework: Flask

## Load Test

The microservice is capable of handling 10,000 requests per second. The load test is included to verify this performance.

IMAGE GOES HERE


## Data Engineering

The project involves the use of Pandas for data engineering. It retrieves information about the top 200 Spotify podcasts and their episodes from the Spotify API. This dataset is used in the microservice. 

## Infrastructure as Code (IaC)


A CI/CD pipeline includes actions for installation, linting, testing, and formatting (review the badges on top of this readme).


## Architectural Diagram

DIAGRAM GOES HERE

## GitHub Configurations
The GitHub repository includes GitHub Actions and a .devcontainer configuration for GitHub Codespaces. This ensures the local version of the project is reproducible. GitHub Action build badges for install, lint, test, and format actions are also present.

## Teamwork Reflection

Each team member should submit a separate 1-2 page management report reflecting on the team's functioning. The report includes a reflection on teamwork principles, a peer evaluation with three positive attributes and three areas for improvement, and the outcome of the feedback session with the team.



