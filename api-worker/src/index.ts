interface Env {
	LASTFM_API_KEY: string;
}

export default {
	async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
		const url = new URL(request.url);
		const user = url.searchParams.get('user');

		const headers = {
			'Content-Type': 'application/json',
			'Access-Control-Allow-Origin': '*', // permite acesso de qualquer origem
			'Access-Control-Allow-Methods': 'GET, OPTIONS',
		};

		if (request.method === 'OPTIONS') {
			return new Response(null, { headers });
		}

		if (!user) {
			return new Response(JSON.stringify({ error: "O parâmetro 'user' é obrigatório." }), {
				status: 400,
				headers: { 'Content-Type': 'application/json' },
			});
		}

		const apiKey = env.LASTFM_API_KEY;
		const apiUrl = `https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=${user}&api_key=${apiKey}&format=json&limit=1`;

		try {
			const res = await fetch(apiUrl);
			if (!res.ok) {
				return new Response(JSON.stringify({ error: `Erro ao acessar API do Last.fm` }), {
					status: res.status,
					headers: { 'Content-Type': 'application/json' },
				});
			}

			const data = await res.json();

			if (!data.recenttracks?.track?.length) {
				return new Response(JSON.stringify({ error: 'Nenhuma música encontrada.' }), {
					status: 404,
					headers: { 'Content-Type': 'application/json' },
				});
			}

			const track = data.recenttracks.track[0];
			const nowPlaying = track['@attr']?.nowplaying === 'true';

			const result = {
				artist: track.artist['#text'],
				name: track.name,
				album: track.album['#text'],
				image: track.image.pop()['#text'],
				nowPlaying,
			};

			return new Response(JSON.stringify(result), {
				headers: { 'Content-Type': 'application/json' },
			});
		} catch (err: any) {
			return new Response(JSON.stringify({ error: 'Erro interno', details: err.message }), {
				status: 500,
				headers: { 'Content-Type': 'application/json' },
			});
		}
	},
};
