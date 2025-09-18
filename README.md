# Last.fm Current Song - JAMStack

A modern JAMStack application that displays the current playing song from Last.fm using React frontend and Cloudflare Pages Functions.

## 🏗️ Architecture

- **Frontend**: React application built with Vite
- **Backend**: Cloudflare Pages Function for Last.fm API integration
- **Deployment**: Cloudflare Pages hosting

## 🚀 Quick Start

### Development

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Build for production:
   ```bash
   npm run build
   ```

## ⚙️ Cloudflare Pages Setup

### 1. Environment Variables

Configure the following environment variable in your Cloudflare Pages dashboard:

- **`LASTFM_API_KEY`**: Your Last.fm API key
  - Get it from: https://www.last.fm/api/account/create
  - Go to your Cloudflare Pages project > Settings > Environment variables
  - Add `LASTFM_API_KEY` with your Last.fm API key

### 2. Build Settings

In Cloudflare Pages, use these build settings:

- **Framework preset**: None
- **Build command**: `npm run build`
- **Build output directory**: `dist`
- **Root directory**: `/` (repository root)

### 3. Functions

The application includes a Cloudflare Pages Function at `/functions/currentsong.js` that:
- Fetches current track from Last.fm API
- Returns JSON data for the React frontend
- Handles errors gracefully
- Uses the hardcoded username: `gahorstmann`

## 📡 API Endpoints

### `/api/currentsong`

Returns the current playing song data in JSON format:

```json
{
  "user": "gahorstmann",
  "artist": "Artist Name",
  "song": "Song Title",
  "song_url": "https://www.last.fm/music/...",
  "album": "Album Name",
  "album_cover": [...]
}
```

## 🎵 Features

- **Real-time updates**: Auto-refreshes every 60 seconds
- **Responsive design**: Works on desktop and mobile
- **Album covers**: Displays album artwork when available
- **Error handling**: Graceful error messages and retry functionality
- **Last.fm integration**: Direct links to Last.fm track pages

## 🛠️ Development

### Project Structure

```
/
├── src/
│   ├── pages/
│   │   └── index.jsx          # Main React component
│   ├── main.jsx               # React app entry point
│   └── style.css              # Application styles
├── functions/
│   └── currentsong.js         # Cloudflare Pages Function
├── public/
│   └── placeholder-album.png  # Fallback album cover
├── package.json               # Node.js dependencies
├── vite.config.js             # Vite configuration
└── index.html                 # HTML template
```

### Environment Variables

For local development, you can create a `.env` file (not included in the repository):

```env
LASTFM_API_KEY=your_lastfm_api_key_here
```

Note: Cloudflare Pages Functions use the environment variables configured in the Cloudflare dashboard.

## 🔧 Legacy Version

The previous Python Flask version has been archived. The new JAMStack version provides:

- ✅ Better performance with static hosting
- ✅ Modern React frontend
- ✅ Serverless functions for API calls
- ✅ Easy deployment to Cloudflare Pages
- ✅ Built-in CDN and caching
