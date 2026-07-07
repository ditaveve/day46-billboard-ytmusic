# Time Travel Playlist 🎵

A "travel in time" app: type in a date, and it builds a YouTube Music playlist of that day's Billboard Hot 100 songs, so you can relive the charts from any point in history.

## How it works

1. You enter a date (`YYYY-MM-DD`).
2. It scrapes the Billboard Hot 100 for that date from [appbrewery.github.io/bakeboard-hot-100](https://appbrewery.github.io/bakeboard-hot-100).
3. It logs into your YouTube Music account and creates a new playlist named `{date} Billboard 100`.
4. For each song, it searches YouTube Music and adds the best match to the playlist.

## Setup

### 1. Install dependencies

```bash
pip3 install requests beautifulsoup4 ytmusicapi
```

### 2. Create your `browser.json`

This project needs `browser.json` to authenticate with your YouTube Music account. It's **not included in this repo** (it contains your personal auth cookies), so you need to generate your own:

1. Open [music.youtube.com](https://music.youtube.com) in your browser and make sure you're logged in.
2. Open DevTools → **Network** tab, then reload the page (or scroll your library) so requests fire.
3. Filter for a request to an endpoint containing `browse` (e.g. `/youtubei/v1/browse`). Click it, and copy the **raw request headers** from the Headers section.
4. In your terminal, run:
   ```bash
   python3 -c "import ytmusicapi; ytmusicapi.setup(filepath='browser.json')"
   ```
5. Paste the headers you copied when prompted, then press Enter (Ctrl+D on Mac if it doesn't submit automatically).

This generates a `browser.json` file in the project folder, which `main.py` reads to authenticate.

**Note:** the auth cookie in `browser.json` expires periodically (usually after a few weeks, or if you log out elsewhere). If you start getting auth errors, just redo this step.

## Usage

```bash
python3 main.py
```

You'll be prompted for a date in `YYYY-MM-DD` format, and the script will create and populate the matching playlist in your YouTube Music library.
