/**
 * Cloudflare Pages Function to fetch current song from Last.fm API
 * Endpoint: /api/currentsong
 */

export async function onRequestGet(context) {
  const { env } = context;
  
  // Get API key from environment variables
  const apiKey = env.LASTFM_API_KEY;
  if (!apiKey) {
    return new Response(JSON.stringify({ 
      error: 'LASTFM_API_KEY not configured' 
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // Fixed username as specified in requirements
  const username = 'gahorstmann';
  
  try {
    // Build Last.fm API request
    const lastfmUrl = new URL('https://ws.audioscrobbler.com/2.0/');
    lastfmUrl.searchParams.set('method', 'user.getrecenttracks');
    lastfmUrl.searchParams.set('user', username);
    lastfmUrl.searchParams.set('api_key', apiKey);
    lastfmUrl.searchParams.set('format', 'json');
    lastfmUrl.searchParams.set('limit', '1');

    // Fetch from Last.fm API
    const response = await fetch(lastfmUrl.toString());
    const data = await response.json();

    // Handle Last.fm API errors
    if (data.error) {
      return new Response(JSON.stringify({
        error: `Last.fm API Error: ${data.message}`
      }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Extract track information
    const track = data.recenttracks?.track?.[0];
    if (!track) {
      return new Response(JSON.stringify({
        error: 'No recent tracks found'
      }), {
        status: 404,
        headers: { 'Content-Type': 'application/json' }
      });
    }

    // Build response object matching the original Python API structure
    const currentSong = {
      user: username,
      artist: track.artist['#text'] || 'Unknown Artist',
      song: track.name || 'Unknown Song',
      song_url: track.url || '',
      album: track.album['#text'] || 'Unknown Album',
      album_cover: track.image || []
    };

    // Return JSON response with CORS headers
    return new Response(JSON.stringify(currentSong), {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Cache-Control': 's-maxage=60' // Cache for 60 seconds
      }
    });

  } catch (error) {
    console.error('Error fetching from Last.fm:', error);
    return new Response(JSON.stringify({
      error: 'Failed to fetch current song'
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}