# 畢業專題專案庫 (Senior Project)

[![Documentation](https://img.shields.io/badge/Docs-Live%20Website-blue?style=for-the-badge&logo=materialformkdocs)](https://ho-yu-chiao.github.io/senior-project/)
[![Deploy Documentation](https://github.com/Ho-yu-chiao/senior-project/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/Ho-yu-chiao/senior-project/actions/workflows/deploy-docs.yml)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

本儲存庫為畢業專題的官方專案庫，包含完整的系統實作程式碼、規格文檔以及向指導教授每週匯報的開發進度報告。

---

## 🌐 線上公開文檔網站

> 🔗 **專題公開文檔網站**：[https://ho-yu-chiao.github.io/senior-project/](https://ho-yu-chiao.github.io/senior-project/)

本網站由 GitHub Actions 自動建置與發布，內容涵蓋：
- 系統需求規格與架構流程圖 (Mermaid Diagrams)
- 專案開發甘特圖與里程碑進度 (Roadmap)
- 每週開發進度匯報 (Weekly Reports)
- 與指導老師的歷次會議紀錄 (Meeting Minutes)

---

## 📁 目錄結構

```text
senior-project/
├── .github/
│   └── workflows/
│       └── deploy-docs.yml     # GitHub Actions 自動部屬工作流
├── docs/                       # 專案文檔原始 Markdown 檔案
│   ├── index.md                # 文檔網站首頁
│   ├── spec/                   # 規格與架構 (需求、架構、時程)
│   ├── progress/               # 每週進度週報
│   └── meetings/               # 會議紀錄與範本
├── .gitignore                  # Git 忽略設定
├── mkdocs.yml                  # MkDocs 網站設定檔
├── requirements.txt            # Python 相依套件
└── README.md                   # 專案首頁說明
```

---

## 💻 本地端預覽文檔 (Local Development)

若要在本機端即時預覽文檔網站編輯效果，請依照以下步驟操作：

### 1. 安裝必要套件

確保已安裝 Python 3.10+，然後執行：

```bash
pip install -r requirements.txt
```

### 2. 啟動本機伺服器

```bash
mkdocs serve
```

啟動後，請在瀏覽器中開啟 [http://127.0.0.1:8000](http://127.0.0.1:8000) 即可即時檢視文檔並支援熱重載（Hot Reload）。

---

## 🚀 部署流程

本專案已完全自動化！每當將更動推送到 `main` 分支時：
```bash
git add .
git commit -m "docs: 更新進度報告"
git push origin main
```
GitHub Actions 將自動觸發並於 1~2 分鐘內將最新的文檔發布至 GitHub Pages 網站。
