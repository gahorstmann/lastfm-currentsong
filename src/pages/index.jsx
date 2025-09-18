import React, { useState, useEffect } from 'react';

/**
 * React component that displays the current song from Last.fm
 * Fetches data from the Cloudflare Pages Function at /api/currentsong
 */
function App() {
  const [songData, setSongData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [lastUpdated, setLastUpdated] = useState(null);

  /**
   * Fetch current song data from the API
   */
  const fetchCurrentSong = async () => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await fetch('/api/currentsong');
      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.error || 'Failed to fetch current song');
      }
      
      setSongData(data);
      setLastUpdated(new Date().toLocaleTimeString());
    } catch (err) {
      setError(err.message);
      console.error('Error fetching current song:', err);
    } finally {
      setLoading(false);
    }
  };

  // Fetch data on component mount and set up auto-refresh
  useEffect(() => {
    fetchCurrentSong();
    
    // Auto-refresh every 60 seconds
    const interval = setInterval(fetchCurrentSong, 60000);
    
    return () => clearInterval(interval);
  }, []);

  /**
   * Get the album cover image URL
   * Last.fm returns an array of images, we want the largest one
   */
  const getAlbumCoverUrl = () => {
    if (!songData?.album_cover || !Array.isArray(songData.album_cover)) {
      return '/placeholder-album.png'; // Fallback image
    }
    
    // Find the largest image or use the last one
    const largeImage = songData.album_cover.find(img => img.size === 'large') || 
                      songData.album_cover.find(img => img.size === 'medium') ||
                      songData.album_cover[songData.album_cover.length - 1];
    
    return largeImage?.['#text'] || '/placeholder-album.png';
  };

  return (
    <div className="app">
      <h1>🎵 Current Song from Last.fm</h1>
      
      {loading && (
        <div className="loading">
          <div className="spinner"></div>
          Loading current song...
        </div>
      )}
      
      {error && (
        <div className="error">
          <h3>❌ Error</h3>
          <p>{error}</p>
          <button className="refresh-button" onClick={fetchCurrentSong}>
            Try Again
          </button>
        </div>
      )}
      
      {songData && !loading && (
        <div className="song-card">
          <img 
            src={getAlbumCoverUrl()} 
            alt={`${songData.album} album cover`}
            className="album-cover"
            onError={(e) => {
              e.target.src = '/placeholder-album.png';
            }}
          />
          
          <h2 className="song-title">{songData.song}</h2>
          <h3 className="artist-name">by {songData.artist}</h3>
          
          {songData.album && songData.album !== 'Unknown Album' && (
            <p className="album-name">from "{songData.album}"</p>
          )}
          
          {songData.song_url && (
            <p>
              <a 
                href={songData.song_url} 
                target="_blank" 
                rel="noopener noreferrer"
                style={{ color: 'white', textDecoration: 'underline' }}
              >
                View on Last.fm
              </a>
            </p>
          )}
        </div>
      )}
      
      <button className="refresh-button" onClick={fetchCurrentSong} disabled={loading}>
        🔄 Refresh
      </button>
      
      <div className="footer">
        <p>Data from Last.fm API • User: {songData?.user || 'gahorstmann'}</p>
        {lastUpdated && <p>Last updated: {lastUpdated}</p>}
        <p>Auto-refreshes every 60 seconds</p>
      </div>
    </div>
  );
}

export default App;