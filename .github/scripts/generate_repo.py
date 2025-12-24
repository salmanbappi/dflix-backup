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
    # 1. Process Dflix
    with open("apktool.yml", "r") as f:
        apktool = yaml.safe_load(f)
    
    version_info = apktool.get("versionInfo", {})
    version_name = version_info.get("versionName")
    version_code = version_info.get("versionCode")
    
    dflix_apk = f"dflix-v{version_name}.apk"
    
    dflix_item = {
        "name": "Aniyomi: Dflix",
        "pkg": "eu.kanade.tachiyomi.animeextension.all.dflix",
        "apk": dflix_apk,
        "lang": "all",
        "code": int(version_code),
        "version": str(version_name),
        "nsfw": 0,
        "hasReadme": 0,
        "hasChangelog": 0,
        "icon": "https://raw.githubusercontent.com/salmanbappi/dflix/master/res/mipmap-xxxhdpi/ic_launcher.png"
    }
    
    if os.path.exists(dflix_apk):
        dflix_item["size"] = get_apk_size(dflix_apk)
        dflix_item["sha256"] = get_file_sha256(dflix_apk)

    repo_data = [dflix_item]

    # 2. Process DhakaFlix (should be downloaded in current dir by workflow)
    dhaka_apks = [f for f in os.listdir(".") if f.startswith("dhakaflix-v") and f.endswith(".apk")]
    if dhaka_apks:
        dhaka_apk = dhaka_apks[0]
        # Extract version from filename: dhakaflix-v14.42.apk -> 14.42
        dhaka_version = dhaka_apk.replace("dhakaflix-v", "").replace(".apk", "")
        # Extract code from version (assuming BUILD_NUMBER is the suffix)
        dhaka_code = dhaka_version.split(".")[-1]
        
        dhaka_item = {
            "name": "Aniyomi: DhakaFlix",
            "pkg": "eu.kanade.tachiyomi.animeextension.all.dhakaflix",
            "apk": dhaka_apk,
            "lang": "all",
            "code": int(dhaka_code),
            "version": dhaka_version,
            "nsfw": 0,
            "hasReadme": 0,
            "hasChangelog": 0,
            "icon": "https://raw.githubusercontent.com/salmanbappi/dhakaflix/master/res/mipmap-xxxhdpi/ic_launcher.png",
            "size": get_apk_size(dhaka_apk),
            "sha256": get_file_sha256(dhaka_apk)
        }
        repo_data.append(dhaka_item)

    # 3. Save index.min.json
    with open("index.min.json", "w") as f:
        json.dump(repo_data, f, separators=(',', ':'))

if __name__ == "__main__":
    generate()