"""
SimClass Google Docs 自動同步腳本
用於將 Google 文件中的最新教學腳本、Agent 卡片與架構設定同步至 docs/ 文件庫
"""
import urllib.request
import re
import os
import shutil

DOC_ID = "12Y3odbI0IV6zJBWi_nhHnvx-t64decyDAo4Zbse3PqA"
DOC_HTML_URL = f"https://docs.google.com/document/d/{DOC_ID}/export?format=html"
DOC_TXT_URL = f"https://docs.google.com/document/d/{DOC_ID}/export?format=txt"

def fetch_content():
    print(f"[*] 正在從 Google 文件擷取最新內容 (Doc ID: {DOC_ID})...")
    os.makedirs("docs/assets/images", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    headers = {"User-Agent": "Mozilla/5.0"}
    
    # 抓取 TXT
    req_txt = urllib.request.Request(DOC_TXT_URL, headers=headers)
    with urllib.request.urlopen(req_txt) as resp:
        txt_data = resp.read().decode("utf-8-sig")
    with open("data/gdoc_raw.txt", "w", encoding="utf-8") as f:
        f.write(txt_data)
    print(f"[+] TXT 抓取成功，共 {len(txt_data)} 字元。")

    # 抓取 HTML 與圖片
    req_html = urllib.request.Request(DOC_HTML_URL, headers=headers)
    with urllib.request.urlopen(req_html) as resp:
        html_data = resp.read().decode("utf-8")
    with open("data/gdoc_raw.html", "w", encoding="utf-8") as f:
        f.write(html_data)
    
    img_urls = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html_data)
    print(f"[+] 偵測到 {len(img_urls)} 張圖片，開始同步...")
    
    # 標準命名對照
    img_mapping = {
        0: "agent_cards.png",
        1: "agent_state.png",
        2: "orchestrator_flowchart.jpg"
    }
    
    for i, u in enumerate(img_urls):
        try:
            target_name = img_mapping.get(i, f"gdoc_img_{i+1}.png")
            target_path = os.path.join("docs/assets/images", target_name)
            img_req = urllib.request.Request(u, headers=headers)
            with urllib.request.urlopen(img_req) as img_resp:
                img_bytes = img_resp.read()
                with open(target_path, "wb") as img_file:
                    img_file.write(img_bytes)
            print(f"    - 已儲存圖片: {target_path} ({len(img_bytes)} bytes)")
        except Exception as e:
            print(f"    - 圖片 {i} 下載失敗: {e}")

    print("[OK] Google Doc sync and images updated successfully!")

if __name__ == "__main__":
    fetch_content()
