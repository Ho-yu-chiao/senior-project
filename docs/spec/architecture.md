# 系統架構設計

本章節介紹 **SimClass** 系統的總體軟體架構、技術選型以及多代理人與狀態機之間的資料互動流。

---

## 1. 系統整體架構圖

本系統採用模組化與多代理人分層架構設計，確保各學生 Agent 的獨立運算與課堂 Orchestrator 的協調調度：

```mermaid
graph TD
    subgraph Client["實習教師操作介面 (Frontend)"]
        TeacherUI["Web 課堂互動面板 / 語音輸入模組"]
        Board["虛擬黑板 (題目展示)"]
    end

    subgraph Backend["SimClass 核心後端 (FastAPI / Python)"]
        API["API 路由與 WebSocket 控制器"]
        Orchestrator["Orchestrator 課堂調度中樞"]
        StateEngine["認知狀態轉移引擎 (State Engine)"]
    end

    subgraph AgentPool["AI 學生代理集群 (Multi-Agent Pool)"]
        AgentA["Agent A (高成就主動)"]
        AgentB["Agent B (中程度觀望)"]
        AgentC["Agent C (迷思概念型)"]
        AgentD["Agent D (低成就焦慮)"]
        AgentE["Agent E (分心干擾型)"]
    end

    subgraph DataLayer["資料與配置層 (Data Layer)"]
        PromptDB[("Agent System Prompts")]
        ScenarioDB[("微型教學情境與事件庫")]
        LogDB[("課堂互動記錄 (History JSON)")]
    end

    TeacherUI -->|"1. 教學語句輸入"| API
    API --> Orchestrator
    Orchestrator -->|"2. 狀態查詢"| StateEngine
    StateEngine <-->|"讀取/更新"| LogDB
    PromptDB --> AgentPool
    ScenarioDB --> Orchestrator

    Orchestrator -->|"3. 評估發言權與喚醒"| AgentPool
    AgentPool -->|"4. 學生回應生成 (LLM)"| Orchestrator
    Orchestrator -->|"5. 觸發轉移規則"| StateEngine
    Orchestrator -->|"6. 合成課堂對話流"| API
    API -->|"7. 串流反饋"| TeacherUI
```

---

## 2. 技術選型 (Tech Stack)

| 領域 | 技術 / 工具 | 選型理由 |
| :--- | :--- | :--- |
| **大語言模型 (LLM)** | Google Gemini / OpenAI GPT-4o | 具備高精準語意分析、角色扮演穩定度與極低延遲推論 |
| **後端核心** | Python 3.11+, LangChain / LangGraph | 專為多代理人互動（Multi-Agent）與圖狀狀態機（State Graph）打造 |
| **Web 框架** | FastAPI + WebSockets | 支援即時雙向語音與文字串流，確保微型教學互動之即時感 |
| **文檔與報告平台** | MkDocs Material + GitHub Pages | 支援 Mermaid 圖表、LaTeX 數學式、全文搜尋與 GitHub CI/CD 自動部署 |
| **版本控管** | Git / GitHub Actions | 追蹤每一週之程式與教案演進，保證專案透明度 |

---

## 3. 課堂微型教學互動時序圖

```mermaid
sequenceDiagram
    autonumber
    actor Teacher as 實習教師
    participant UI as 前端互動介面
    participant Orch as Orchestrator 調度器
    participant Agent as 5 位學生 Agents
    participant State as 狀態機 (State Engine)

    Teacher->>UI: 在黑板出題「15 + 5 × 2 = ?」並全班發問
    UI->>Orch: 傳送教師提問內容
    Orch->>State: 讀取全體學生當前 Knowledge & Classroom 狀態
    State-->>Orch: 回傳當前各 Agent 信心度、參與度與迷思標記
    Orch->>Agent: 派發任務：Agent A (搶答)、Agent C (迷思算 40)、Agent E (分心)
    Agent-->>Orch: 各 Agent 生成個性化回應與動作描述
    Orch->>UI: 即時渲染課堂情境（文字/語音播報）
    Teacher->>UI: 介入引導：「先不要急，我們看乘法 5 × 2 是買兩杯飲料…」
    UI->>Orch: 傳送引導語
    Orch->>State: 觸發 RULE_07 (生活情境對質)，更新 Agent C 掌握度與迷思狀態
    State-->>UI: 更新學生狀態儀表板
```
