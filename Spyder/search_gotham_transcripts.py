#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
search_gotham_transcripts.py
Sucht Transkripte aller Videos eines YouTube-Kanals nach bestimmten Stichworten.
Benötigt: yt-dlp, youtube-transcript-api, pandas
Aufruf (Beispiel):
    python search_gotham_transcripts.py "https://www.youtube.com/c/GothamChess/videos"
"""

import sys
import re
import csv
import argparse
from yt_dlp import YoutubeDL
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript
import pandas as pd
from datetime import timedelta

# Default keywords (case-insensitive)
DEFAULT_KEYWORDS = ["sicilian", "kebab", "kebap", "turkish restaurant"]

def seconds_to_hms(seconds: float) -> str:
    # returns HH:MM:SS
    td = timedelta(seconds=int(seconds))
    return str(td)

def fetch_channel_videos(channel_url, max_videos=None):
    """
    Gibt eine Liste von Videos zurück: dicts mit 'id', 'title', 'url'
    Nutzt yt_dlp extract_info (ohne Download).
    """
    ydl_opts = {
        'extract_flat': True,   # nur Metadaten, keine Downloads
        'skip_download': True,
        'quiet': True,
        'ignoreerrors': True,
    }
    videos = []
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)
        if not info:
            return videos
        # Falls Playlist/Uploads
        entries = info.get('entries') or []
        for e in entries:
            if e is None:
                continue
            # each entry may have 'id' and 'url' or 'webpage_url'
            vid_id = e.get('id') or e.get('url')
            url = e.get('url') or e.get('webpage_url') or f"https://www.youtube.com/watch?v={vid_id}"
            title = e.get('title') or e.get('fulltitle') or url
            videos.append({'id': vid_id, 'title': title, 'url': url})
            if max_videos and len(videos) >= max_videos:
                break
    return videos

def search_transcripts(videos, keywords, save_csv="results.csv", languages=None):
    """
    Durchsucht Transkripte und schreibt Treffer in CSV.
    languages: list like ['en', 'de'] to prefer languages (optional)
    """
    kw_pattern = re.compile(r'(' + r'|'.join(re.escape(k) for k in keywords) + r')', re.IGNORECASE)
    rows = []
    total_checked = 0
    for i, v in enumerate(videos, 1):
        vid = v['id']
        title = v['title']
        url = v['url']
        print(f"[{i}/{len(videos)}] Prüfe: {title}  --  {url}")
        total_checked += 1
        try:
            # get_transcript returns a list of {text, start, duration}
            if languages:
                transcript = YouTubeTranscriptApi.get_transcript(vid, languages=languages)
            else:
                transcript = YouTubeTranscriptApi.get_transcript(vid)
        except TranscriptsDisabled:
            print("  -> Transkripte deaktiviert.")
            continue
        except NoTranscriptFound:
            print("  -> Kein Transkript gefunden.")
            continue
        except CouldNotRetrieveTranscript:
            print("  -> Transkript nicht abrufbar (Netzwerk/Rate limit).")
            continue
        except Exception as e:
            print(f"  -> Fehler beim Abrufen des Transkripts: {e}")
            continue

        # Suche in jedem Segment
        for seg in transcript:
            text = seg.get('text', '')
            match = kw_pattern.search(text)
            if match:
                start = seg.get('start', 0.0)
                duration = seg.get('duration', 0.0)
                snippet = text.strip().replace("\n", " ")
                rows.append({
                    'video_id': vid,
                    'title': title,
                    'video_url': url,
                    'match_keyword': match.group(0),
                    'start_seconds': start,
                    'start_hms': seconds_to_hms(start),
                    'duration_seconds': duration,
                    'snippet': snippet
                })
                # Falls du mehrere Treffer pro Video willst, entferne das break.
                # hier lassen wir mehrere Treffer zu (kein break)
    # Speichere CSV
    if rows:
        df = pd.DataFrame(rows)
        df.to_csv(save_csv, index=False, quoting=csv.QUOTE_MINIMAL)
        print(f"\nErgebnisse: {len(rows)} Treffer in {len(videos)} geprüften Videos.")
        print(f"CSV gespeichert als: {save_csv}")
    else:
        print("\nKeine Treffer gefunden.")
    return rows

def main():
    parser = argparse.ArgumentParser(description="Durchsuche YouTube-Transkripte eines Kanals nach Stichworten.")
    parser.add_argument('channel_url', help='YouTube channel videos URL, z.B. https://www.youtube.com/c/GothamChess/videos')
    parser.add_argument('--keywords', nargs='*', default=DEFAULT_KEYWORDS, help='Stichworte (space-getrennt). Standard: adana kebab kebap "turkish restaurant"')
    parser.add_argument('--max', type=int, default=None, help='Maximale Anzahl Videos (optional, für Tests).')
    parser.add_argument('--out', default='results.csv', help='Ausgabe-CSV-Datei.')
    parser.add_argument('--languages', nargs='*', default=None, help='Bevorzugte Sprachen für Transkripte, z.B. en tr (optional).')
    args = parser.parse_args()

    channel_url = args.channel_url
    keywords = args.keywords
    print("Starte Suche nach Stichworten:", keywords)
    print("Hole Videoliste vom Kanal...")
    videos = fetch_channel_videos(channel_url, max_videos=args.max)
    if not videos:
        print("Keine Videos gefunden. Bitte Channel-URL prüfen (z. B. https://www.youtube.com/c/GothamChess/videos oder https://www.youtube.com/@GothamChess/videos).")
        sys.exit(1)

    print(f"Gefundene Videos: {len(videos)} (es werden alle durchsucht, falls --max nicht angegeben).")
    rows = search_transcripts(videos, keywords, save_csv=args.out, languages=args.languages)
    # kurze Console-Ausgabe der ersten Treffer
    if rows:
        print("\nBeispiel-Treffer (max 5):")
        for r in rows[:5]:
            print(f"- {r['title']} @ {r['start_hms']} -> \"{r['snippet']}\" (keyword: {r['match_keyword']})")
    else:
        print("Keine Treffer in den durchsuchten Transkripten.")

if __name__ == "__main__":
    main()
