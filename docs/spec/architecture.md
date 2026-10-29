# 系統架構設計

本章節介紹系統的總體架構、技術選型以及模組間的資料流向。

---

## 1. 系統整體架構圖

本專案採用分層式架構設計，確保各模組職責清晰且具備高可維護性：

```mermaid
graph TD
    subgraph UI["呈現層 (Presentation Layer)"]
        WebUI["Web / Dashboard 介面"]
        CLI["命令列介面 (CLI)"]
    end

    subgraph Service["業務邏輯層 (Service Layer)"]
        API["API 閘道 / 控制器"]
        CoreEngine["核心演算推論引擎"]
        DataPipeline["資料前處理管道"]
    end

    subgraph Data["資料與基礎設施層 (Data & Infrastructure)"]
        DB[("資料庫 / 儲存體")]
        External[("外部資料來源 / 設備傳感器")]
    end

    WebUI --> API
    CLI --> API
    API --> DataPipeline
    DataPipeline --> CoreEngine
    CoreEngine --> DB
    External --> DataPipeline
```

---

## 2. 技術選型 (Tech Stack)

| 領域 | 技術 / 工具 | 選型理由 |
| :--- | :--- | :--- |
| **程式語言** | Python 3.11+ | 擁有豐富的科學運算庫與良好的跨平台支援 |
| **文檔系統** | MkDocs Material | Markdown 原生支援、搜尋功能強大、便於學術成果展示 |
| **版本控管與 CI/CD** | Git / GitHub Actions | 自動化測試與文檔部署，落實現代軟體工程規範 |
| **環境管理** | Virtualenv / Poetry | 確保團隊成員與伺服器環境相依版本一致 |

---

## 3. 資料處理流程圖

```mermaid
sequenceDiagram
    autonumber
    actor User as 使用者/測試員
    participant System as 系統前端
    participant Engine as 運算核心
    participant Store as 結果儲存庫

    User->>System: 提交輸入資料/執行指令
    System->>Engine: 發送前處理請求
    Engine->>Engine: 執行特徵提取與邏輯運算
    Engine->>Store: 寫入運算日誌與成果數據
    Engine-->>System: 回傳分析報表與視覺化數值
    System-->>User: 於介面呈現即時結果
```
