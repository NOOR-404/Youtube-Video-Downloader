#!/data/data/com.termux/files/usr/bin/python3.13
# -*- coding: utf-8 -*-
import os, sys, time
from yt_dlp import YoutubeDL

P = '\033[35m'; R = '\033[0m'

def progress_hook(d):
    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0; downloaded = d.get('downloaded_bytes', 0)
        if total > 0: percent = int(downloaded / total * 100); downloaded_mb = downloaded / (1024 * 1024); total_mb = total / (1024 * 1024); width = 15; filled = int(width * percent // 100); bar = (P + '━' * filled + R + '━' * (width - filled)); sys.stdout.write(f"\r[~] Fetching: {bar} {percent}% ({downloaded_mb:.1f}/{total_mb:.1f}MB)"); sys.stdout.flush()
    elif d['status'] == 'finished': sys.stdout.write("\r" + " " * 60 + "\r"); sys.stdout.flush()

def download_media():
    os.system('clear'); print(f"\n{60*'-'}\n[~] Developer ==> NOOR-404\n[~] Tool Type ==> Yt Mp4,Mp3 Downloader\n{60*'-'}"); print("[1] Single Mp3, Mp4 Download\n[2] Multiple Mp3, Mp4 Download"); print(f"{60*'-'}"); mode = input("[?] Choice Mode ==> ").strip(); print(f"{60*'-'}"); urls = []; available_heights = set()
    if mode == '2':
        try: count = int(input("[?] How much video/audio you want to download ==> ").strip())
        except ValueError: count = 1
        print(f"{60*'-'}")
        for i in range(1, count + 1):
            url = input(f"[{i}] Enter Link ==> ").strip()
            if url:
                urls.append(url)
                try:
                    with YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl: info = ydl.extract_info(url, download=False); print(f"[~] Title ==> {info.get('title', 'Unknown Title')}\n{60*'-'}"); formats = info.get('formats', [])
                    for f in formats:
                        if f.get('vcodec') != 'none' and f.get('height'): available_heights.add(f['height'])
                except Exception as e: print(f"[~] Title ==> Error fetching title ({e})\n{60*'-'}")
    else:
        url = input("[?] Enter Link ==> ").strip()
        if url:
            urls.append(url)
            try:
                with YoutubeDL({'quiet': True, 'no_warnings': True}) as ydl: info = ydl.extract_info(url, download=False);print(f"[~] Title ==> {info.get('title', 'Unknown Title')}\n{60*'-'}");formats = info.get('formats', [])
                for f in formats:
                    if f.get('vcodec') != 'none' and f.get('height'): available_heights.add(f['height'])
            except Exception as e: print(f"[~] Title ==> Error fetching title ({e})\n{60*'-'}")
    if not urls: return
    print(f"[1] Video Mp4\n[2] Audio Mp3\n{60*'-'}"); choice = input("[?] Choice ==> ").strip(); download_path = '/data/data/com.termux/files/home/storage/shared/Download/NOOR-YT'
    if not os.path.exists(download_path): os.makedirs(download_path)
    ydl_opts = {'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'), 'quiet': True, 'no_warnings': True, 'progress_hooks': [progress_hook], 'ffmpeg_location': '/data/data/com.termux/files/usr/bin/'}
    if choice == '1':
        all_resolutions = [{'label': '144p', 'height': 144, 'format_id': 'bestvideo[height<=144]+bestaudio/best'}, {'label': '240p', 'height': 240, 'format_id': 'bestvideo[height<=240]+bestaudio/best'}, {'label': '360p', 'height': 360, 'format_id': 'bestvideo[height<=360]+bestaudio/best'}, {'label': '720p', 'height': 720, 'format_id': 'bestvideo[height<=720]+bestaudio/best'}, {'label': '1080p', 'height': 1080, 'format_id': 'bestvideo[height<=1080]+bestaudio/best'}, {'label': '4k', 'height': 2160, 'format_id': 'bestvideo[height<=2160]+bestaudio/best'}, {'label': '8k', 'height': 4320, 'format_id': 'bestvideo[height<=4320]+bestaudio/best'}]; menu_options = []
        for res in all_resolutions:
            if any(h >= res['height'] for h in available_heights): menu_options.append(res)
        if not menu_options: return
        print(f"{60*'-'}")
        for index, res in enumerate(menu_options, start=1): print(f"[{index}] {res['label']}")
        try: res_choice = int(input(f"{60*'-'}\n[?] Select Resolution Pick [1-{len(menu_options)}] ==> ").strip()); selected_resolution = menu_options[res_choice - 1]; ydl_opts['format'] = selected_resolution['format_id']; ydl_opts['merge_output_format'] = 'mp4'
        except (ValueError, IndexError): ydl_opts['format'] = 'bestvideo+bestaudio/best'; ydl_opts['merge_output_format'] = 'mp4'
    else: ydl_opts['format'] = 'bestaudio/best'; ydl_opts['postprocessors'] = [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]
    print(f"{60*'-'}\n[~] Install Process Has Been Started...")
    for index, target_url in enumerate(urls, start=1):
        try:
            if len(urls) > 1: print(f"[~] Downloading [{index}/{len(urls)}]...")
            with YoutubeDL(ydl_opts) as ydl: ydl.download([target_url])
        except Exception as e: print(f"\nError: {e}")
    print("[~] Successfully Downloaded On Your Download/NOOR-YT Folder"); print(f"{60*'-'}"); time.sleep(1.5); print("[~] Thanks For Using "); time.sleep(1); print(f"{60*'-'}")

try: download_media()
except Exception as e: print(e)