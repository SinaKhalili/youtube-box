import requests
import os

gh_api_key = os.environ["GH_TOKEN"]
yt_api_key = os.environ["YT_API_KEY"]
gist_id = os.environ["GIST_ID"]
yt_channel_id = os.environ["CHANNEL_ID"]

yt_base_url = "https://www.googleapis.com/youtube/v3"
gh_base_url = "https://api.github.com"


def update_gist_for_youtube(base_url, gist_id, api_key, text_name, md_name, content):
    """
    Updates a gist with two files, one for video titles, other is links
    to the videos in a markdown file.

    content is a list of tuples
    file_links is expected to be a markdown file (end in .md).
    """
    video_titles_content = "\n".join([item[0] for item in content])
    video_md_file_content = "\n\n".join(
        [f"[{item[0]}](https://www.youtube.com/watch?v={item[1]})" for item in content]
    )
    data = {
        "description": "My Latest YouTube videos 👇",
        "files": {
            text_name: {"content": video_titles_content},
            md_name: {"content": video_md_file_content},
        },
    }
    req = requests.patch(
        url=f"{base_url}/gists/{gist_id}",
        headers={"Authorization": f"token {api_key}", "Accept": "application/json"},
        json=data,
    )
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return "Error retrieving data"


def get_recent_videos(base_url, api_key, upload_id):
    """
    Gets the 25 most recent videos of a playlist

    Returns the videos as a list of [(TITLE, id)] tuples
    """
    req = requests.get(
        url=f"{base_url}/playlistItems",
        params={
            "part": "snippet",
            "maxResults": 25,
            "playlistId": upload_id,
            "key": api_key,
        },
        headers={"Accept": "application/json"},
    )
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return "Error retrieving data"

    video_snippets = req.json()
    video_titles = [item["snippet"]["title"] for item in video_snippets["items"]]
    video_ids = [
        item["snippet"]["resourceId"]["videoId"] for item in video_snippets["items"]
    ]
    return list(zip(video_titles, video_ids))


def get_upload_id(base_url, api_key, channel_id):
    """
    Get the `upload` playlist of the channel to get the recent uploads

    Unfortunately there isn't an endpoint for `recent videos`
    """
    req = requests.get(
        url=f"{base_url}/channels",
        params={"part": "contentDetails", "id": f"{channel_id}", "key": api_key},
        headers={"Accept": "application/json"},
    )
    try:
        req.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return "Error retrieving data"

    channel_info = req.json()
    upload_id = channel_info["items"][0]["contentDetails"]["relatedPlaylists"][
        "uploads"
    ]
    return upload_id


if __name__ == "__main__":
    upload_id = get_upload_id(yt_base_url, yt_api_key, yt_channel_id)
    videos = get_recent_videos(yt_base_url, yt_api_key, upload_id)
    update_gist_for_youtube(
        gh_base_url, gist_id, gh_api_key, "latest_videos", "latest_videos.md", videos
    )
