# SimClass - 國小數學微型教學 AI 學生模擬系統

[![Documentation](https://img.shields.io/badge/Docs-Live%20Website-blue?style=for-the-badge&logo=materialformkdocs)](https://ho-yu-chiao.github.io/senior-project/)
[![Deploy Status](https://github.com/Ho-yu-chiao/senior-project/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/Ho-yu-chiao/senior-project/actions/workflows/deploy-docs.yml)
[![Google Doc Sync](https://img.shields.io/badge/Google%20Doc-Connected-34A853?style=for-the-badge&logo=googledocs)](https://docs.google.com/document/d/12Y3odbI0IV6zJBWi_nhHnvx-t64decyDAo4Zbse3PqA/edit?usp=sharing)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

本儲存庫為畢業專題 **SimClass** 的官方專案庫，包含微型教學多代理人系統實作、規格文檔、教案腳本以及每週向指導教授匯報的進度報告。

---

## 🌐 線上公開文檔網站

> 🔗 **專題公開文檔網站**：[https://ho-yu-chiao.github.io/senior-project/](https://ho-yu-chiao.github.io/senior-project/)

本網站由 GitHub Actions 自動建置與發布，內容涵蓋：
- **SimClass 核心設計**：
  - 微型教學教案與 10–15 分鐘課堂情境腳本（整數四則混合運算）
  - 5 位異質性 AI 學生規格（Agent Cards 與 JSON 認知狀態結構）
  - 8 大課堂突發事件與狀態轉移規則 (Transition Rules)
  - Orchestrator 協調調度器流程架構與課堂對話範例
- **專案工程規劃**：需求規格書、系統架構圖 (Mermaid Diagrams) 與時程甘特圖
- **每週進度與會議紀錄**：歷次週報與指導教授會議記錄追蹤

---

## 🔄 Google 文件動態同步機制

本專案已串接 [Google 文件共享版本](https://docs.google.com/document/d/12Y3odbI0IV6zJBWi_nhHnvx-t64decyDAo4Zbse3PqA/edit?usp=sharing)。當文件內容更新時，有以下兩種同步方式：

1. **GitHub 線上一鍵同步**：進入 GitHub 的 **Actions** 分頁 $\rightarrow$ 點擊 **Sync Google Doc** $\rightarrow$ 按下 **Run workflow**，系統將自動抓取並發布最新版網站。
2. **本地執行同步**：
   ```bash
   python scripts/sync_gdoc.py
   git add .
   git commit -m "docs: 更新 Google 文件內容"
   git push origin main
   ```

---

## 📁 目錄結構

```text
senior-project/
├── .github/
│   └── workflows/
│       ├── deploy-docs.yml     # GitHub Actions 自動部署網站
│       └── sync-gdoc.yml       # Google 文件定時與手動同步工作流
├── data/                       # Google 文件原始備份資料
├── docs/                       # 專案文檔原始 Markdown 與圖表
│   ├── index.md                # 文檔網站首頁
│   ├── assets/images/          # 架構圖、Agent Cards 圖片
│   ├── simclass/               # SimClass 核心設計專區
│   │   ├── overview.md         # 系統總覽
│   │   ├── pedagogy.md         # 教案與 15 分鐘情境腳本
│   │   ├── agents.md           # 5 位 AI 學生 Agent Cards
│   │   ├── events.md           # 課堂事件與轉移規則
│   │   └── orchestrator.md     # Orchestrator 調度機制
│   ├── spec/                   # 工程規範 (需求、架構、時程)
│   ├── progress/               # 每週進度週報
│   └── meetings/               # 會議紀錄與範本
├── scripts/
│   └── sync_gdoc.py            # Google 文件自動抓取轉換腳本
├── mkdocs.yml                  # MkDocs 網站設定檔
├── requirements.txt            # Python 相依套件
└── README.md                   # 專案首頁說明
```

---

## 💻 本地端預覽文檔 (Local Development)

```bash
# 1. 安裝相依套件
pip install -r requirements.txt

# 2. 啟動本機即時預覽伺服器
python -m mkdocs serve
```

開啟瀏覽器前往 [http://127.0.0.1:8000](http://127.0.0.1:8000) 即可即時預覽。
