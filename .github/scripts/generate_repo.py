import json
import yaml
import os
import hashlib
import urllib.request

def get_apk_size(file_path):
    return os.path.getsize(file_path)

def get_file_sha256(file_path):
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def get_external_repo_data(url):
    try:
        # Use a timeout and a user-agent to ensure we get the data
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Warning: Could not fetch external repo data from {url}: {e}")
        return []

def generate():
    # 1. Process current repo (Dflix)
    with open("apktool.yml", "r") as f:
        apktool = yaml.safe_load(f)
    
    version_info = apktool.get("versionInfo", {})
    version_name = version_info.get("versionName")
    version_code = version_info.get("versionCode")
    
    version_suffix = f"v{version_name}"
    apk_name = f"dflix-{version_suffix}.apk"
    
    dflix_item = {
        "name": "Aniyomi: Dflix",
        "pkg": "eu.kanade.tachiyomi.animeextension.all.dflix",
        "apk": apk_name,
        "lang": "all",
        "code": int(version_code),
        "version": str(version_name),
        "nsfw": 0,
        "hasReadme": 0,
        "hasChangelog": 0,
        "icon": "https://raw.githubusercontent.com/salmanbappi/dflix/master/res/mipmap-xxxhdpi/ic_launcher.png"
    }
    
    if os.path.exists(apk_name):
        dflix_item["size"] = get_apk_size(apk_name)
        dflix_item["sha256"] = get_file_sha256(apk_name)

    # 2. Fetch or Add DhakaFlix data
    dhaka_data = get_external_repo_data("https://raw.githubusercontent.com/salmanbappi/dhakaflix/repo/index.min.json")
    
    repo_data = [dflix_item]
    for item in dhaka_data:
        # Update external APK path to be absolute so Anikku knows where to download it from
        if not item["apk"].startswith("http"):
            item["apk"] = f"https://raw.githubusercontent.com/salmanbappi/dhakaflix/repo/{item['apk']}"
        # Avoid duplicates
        if item["pkg"] != dflix_item["pkg"]:
            repo_data.append(item)

    # 3. Save combined index.min.json
    with open("index.min.json", "w") as f:
        json.dump(repo_data, f, separators=(',', ':'))

    # 4. Save repo.json
    repo_info = {
        "meta": {
            "name": "SalmanBappi Extensions",
            "shortName": "salmanbappi",
            "website": "https://github.com/salmanbappi/dflix",
            "signingKeyFingerprint": "c7ebe223044970f2f9738f600dc25c180d3ed03994e088aaf5709338c57b93af"
        }
    }
    with open("repo.json", "w") as f:
        json.dump(repo_info, f, indent=2)

if __name__ == "__main__":
    generate()