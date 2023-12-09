import requests
import pandas as pd
import numpy as np
import urllib.parse
import spotipy.util as util
import PIL.Image
from pylab import *
from dotenv import load_dotenv
import os
import time
from datetime import datetime


# scrap spotify top 100 us podcast to obtain list of podcasts and uri
headers = {
    "Referer": "https://podcastcharts.byspotify.com/us",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

params = {
    "region": "us",
}

response = requests.get(
    "https://podcastcharts.byspotify.com/api/charts/top", params=params, headers=headers
)

response_100 = response.json()

# transform json to pandas and add relevant columns
top_100 = pd.DataFrame(response_100)
top_100["showUri"] = top_100["showUri"].str.replace("spotify:show:", "")
top_100["rank"] = range(1, len(top_100) + 1)
top_100["chart_date"] = datetime.today().strftime("%Y-%m-%d")


# token for API
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
username = os.getenv("USERNAME")
scope = "user-library-read user-top-read"
redirect_uri = "https://developer.spotify.com/dashboard/applications/edd85240c1604b1e89a3e01deb19b7e2"
token = util.prompt_for_user_token(
    username=username,
    scope=scope,
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
)

"""get uri and umber of episodes of top 200 shows and build data frame with info using token and spotipy"""

# episodes per podcast
podcast_list = []
market = "US"

# Read
for i, pod in enumerate(top_100["showUri"]):
    # Create query
    query = "https://api.spotify.com/v1/shows/"
    query += f"{pod}?&market={market}"

    # Search
    response = requests.get(
        query,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    while (
        response.status_code != 200
    ):  # If query encounters error, sleep then try again
        # Sleep
        if "Retry-After" in response.headers:
            sleep_time = int(response.headers["Retry-After"]) + 10
        else:
            sleep_time = 30
        print(
            "Error at podcast",
            i + 1,
            "of",
            len(top_100),
            "! Will wait for",
            sleep_time,
            "seconds then try again...",
        )
        time.sleep(sleep_time)

        # Try again
        response = requests.get(
            query,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )

    # Save
    response_json = response.json()
    podcast_list.append(response_json)

print("Completed.\n")

top_100_n_eps = pd.DataFrame()

# Combine data from each podcast into the DataFrame
for pod in podcast_list:
    top_100_n_eps = pd.concat(
        [top_100_n_eps, pd.json_normalize(pod)], ignore_index=True
    )

#  Add ranking and date of rank
top_100_n_eps["ranking"] = range(1, len(top_100) + 1)
top_100_n_eps["chart_date"] = datetime.today().strftime("%Y-%m-%d")


"""Get jsons of all episodes from top 200 shows"""

# setup
episodes_list = []
podcastsID_list = []
market = "US"
limit = 50
offset = 0
episode_counter = 1  #

# Read
for i, row in top_100_n_eps[["id", "total_episodes"]].iterrows():
    pod = row["id"]
    episode_total = row["total_episodes"]

    while episode_counter <= episode_total:
        # Query
        query = f"https://api.spotify.com/v1/shows/{pod}/episodes?"
        query += f"market={market}&offset={offset}&limit={limit}"

        # Search
        response = requests.get(
            query,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )
        while (
            response.status_code != 200
        ):  # If query encounters error, sleep then try again
            # Sleep
            if "Retry-After" in response.headers:
                sleep_time = int(response.headers["Retry-After"]) + 10
            else:
                sleep_time = 30
            print(
                "Error at podcast",
                i + 1,
                "of",
                len(top_100_n_eps),
                "for episode",
                episode_counter,
                "of",
                episode_total,
                "! Will wait for",
                sleep_time,
                "seconds then try again...",
            )
            time.sleep(sleep_time)

            # Try again
            response = requests.get(
                query,
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/json",
                },
            )

        # Save
        response_json = response.json()
        episodes_list.append(response_json)
        podcastsID_list.append(pod)

        # Update for next batch of episodes
        episode_counter += 50
        offset += 50

    # Reset for next podcast
    episode_counter = 1
    offset = 0

print("Completed.\n")

# Combine
episodes_info_dataset = pd.json_normalize(
    episodes_list[0]
)  # Create DataFrame structure using 1st episodes batch
episodes_info_dataset["show_id"] = podcastsID_list[0]
for i in range(1, len(episodes_list)):
    episodes_info_dataset = pd.concat(
        [episodes_info_dataset, pd.json_normalize(episodes_list[i])], ignore_index=True
    )
    episodes_info_dataset.loc[i, "show_id"] = podcastsID_list[i]

    """extract json info from each row and build dataframe of all episodes info"""
episodes_dataset = pd.json_normalize(
    episodes_info_dataset.loc[0, "items"]
)  # Use a temporary DataFrame as an intermediary
episodes_dataset["show_id"] = episodes_info_dataset.loc[
    0, "show_id"
]  # Create DataFrame structure using 1st batch of episodes

for i in range(1, len(episodes_info_dataset)):
    temp_df = pd.json_normalize(episodes_info_dataset.loc[i, "items"])
    temp_df["show_id"] = episodes_info_dataset.loc[i, "show_id"]
    episodes_dataset = pd.concat([episodes_dataset, temp_df], ignore_index=True)


"""build top 100 master dataset to merge with episodes dataset"""

top_100_s = top_100[
    [
        "showUri",
        "chartRankMove",
        "showName",
        "showPublisher",
        "showImageUrl",
        "showDescription",
    ]
]
top_100_s = top_100_s.rename(columns={"chartRankMove": "showChartRankMove"})

top_100_n_eps_s = top_100_n_eps[
    [
        "id",
        "available_markets",
        "languages",
        "explicit",
        "ranking",
        "chart_date",
        "episodes.total",
        "external_urls.spotify",
    ]
]


top_100_n_eps_s = top_100_n_eps_s.rename(
    columns={
        "available_markets": "showAvailable_markets",
        "languages": "showLlanguages",
        "explicit": "show_explicit",
        "ranking": "show_ranking",
        "chart_date": "show_chart_date",
        "episodes.total": "show_episodes.total",
        "external_urls.spotify": "show_external_url",
    }
)

episodes_master = pd.merge(
    top_100_n_eps_s,
    top_100_s,
    how="left",
    left_on="id",
    right_on="showUri",
)
episodes_master = episodes_master.drop(columns="id")
episodes_master = episodes_master.rename(columns={"showUri": "show_id"})

"""merge top 100 dataset with episodes dataset"""

episodes_dataset = episodes_dataset.rename(
    columns={
        "audio_preview_url": "ep_audio_preview_url",
        "description": "ep_description",
        "duration_ms": "ep_duration_ms",
        "explicit": "ep_explicit",
        "href": "ep_href",
        "html_description": "ep_html_description",
        "id": "ep_id",
        "images": "ep_images",
        "is_externally_hosted": "ep_is_externally_hosted",
        "is_playable": "ep_is_playable",
        "language": "ep_language",
        "languages": "ep_languages",
        "name": "ep_name",
        "release_date": "ep_release_date",
        "release_date_precision": "ep_release_date_precision",
        "type": "ep_type",
        "uri": "ep_uri",
        "external_urls.spotify": "ep_external_urls",
        "restrictions.reason": "ep_restrictions.reason",
    }
)

top_200 = pd.merge(episodes_dataset, episodes_master, how="left", on="show_id")

# calculte average duration of episodes within show
top_200 = top_200.rename(columns={"show_ranking": "ranking_spotify"})
top_200["ep_duration_ms"] = top_200["ep_duration_ms"].astype(str)
top_200["ep_duration_ms"] = top_200["ep_duration_ms"].str.rstrip(".0").astype(float)
top_200["average_ep_duration_ms"] = top_200.groupby("showName")[
    "ep_duration_ms"
].transform("mean")
top_200["average_ep_duration_minutes"] = (
    top_200["average_ep_duration_ms"] / 60000
).astype(int)

# add rankings
df_rank_time = top_200.drop_duplicates(
    subset=["showName", "average_ep_duration_minutes"]
)
df_rank_time = df_rank_time[["showName", "average_ep_duration_minutes"]].sort_values(
    by="average_ep_duration_minutes", ascending=False
)
df_rank_time = df_rank_time.reset_index(drop=True)
df_rank_time["ranking_time"] = range(1, len(df_rank_time) + 1)

df_rank_eps = top_200.drop_duplicates(subset=["showName", "show_episodes.total"])
df_rank_eps = df_rank_eps[["showName", "show_episodes.total"]].sort_values(
    by="show_episodes.total", ascending=False
)
df_rank_eps = df_rank_eps.reset_index(drop=True)
df_rank_eps["ranking_episodes"] = range(1, len(df_rank_time) + 1)

ranks = df_rank_time.merge(right=df_rank_eps, how="left")
ranks = ranks.drop(columns=["average_ep_duration_minutes", "show_episodes.total"])
top_200 = top_200.merge(right=ranks, how="left", on="showName")

# save to parquet

top_200.to_parquet("top_200.parquet")

if __name__ == "__main__":
    main()