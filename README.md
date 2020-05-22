# youtube-box
▶ Update a pinned gist to show your latest YouTube videos - if a user clicks on the gist, another gist is below it linking to the videos [(example)](https://gist.github.com/SinaKhalili/dc3d0f7a3cd13207770a4debbb902d1d) 🤗 

<p align="center">
  <img width="400" src="https://raw.githubusercontent.com/SinaKhalili/youtube-box/master/images/youtube-box.png">
  <h3 align="center">youtube-box</h3>
  <p align="center">Update a pinned gist to show your latest YouTube videos</p>
</p>

---

> 📌✨ For more pinned-gist projects like this one, check out: https://github.com/matchai/awesome-pinned-gists

## Setup

### Prep work

1. Create a new public GitHub Gist (https://gist.github.com/), create two files named `latest_videos` and `latest_videos.md`
1. Create an access token with the `gist` scope and copy it. (https://github.com/settings/tokens/new)
1. Get a YouTube API key - follow these [steps](https://developers.google.com/youtube/v3/getting-started) note that you don't need an Oauth scope for this.

### Project setup

1. Fork this repo
1. Edit the environment variables in `.github/workflows/main.yml`:

   - **CHANNEL_ID:** The ID portion of your YouTube channel url: `https://www.youtube.com/channel/`**`UCrVWVOBoBu7W-aXbApDEuyQ`**
   - **GIST_ID:** The ID portion of your gist url: `https://gist.github.com/matchai/`**`6d5f84419863089a167387da62dd7081`**.

1. Go to the repo **Settings > Secrets**
1. Add the following environment variables:
   - **GH_TOKEN:** The GitHub access token generated above.
   - **YT_API_KEY** The YouTube API key generated above.
