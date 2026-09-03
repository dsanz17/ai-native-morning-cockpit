# AI-Native Morning Cockpit

A Streamlit prototype of an AI-enabled CFO cockpit for a European bank. The application converts synthetic banking data into a morning health check, interactive stress testing, forward-looking forecasts, and a conversational financial assistant.

> **Disclaimer**  
> All data, scenarios, thresholds, calculations and outputs in this repository are synthetic and illustrative. They are calibrated only to approximate the scale of a Dutch universal bank.

## Problem

Banking leadership needs rapid, connected insight into capital, liquidity, earnings, balance-sheet movements, and credit risk. Static spreadsheets and fragmented reports can delay decisions and make it difficult to evaluate the interconnected effects of macroeconomic and funding shocks.

## Solution

The AI-Native Morning Cockpit provides:

- A **Morning Health Check** for capital, liquidity, earnings, asset quality, and balance-sheet movements
- A configurable **What-If Engine** for policy-rate, deposit-outflow, and credit-migration shocks
- A named **macroeconomic stress-scenario library** with transparent assumptions and limit assessments
- A **Horizon View** with trend-based forecasts, confidence intervals, and management-target comparisons
- A conversational **AI Financial Partner** that explains verified dashboard outputs and supports CFO-style questions
- Optional Gemini-powered executive narratives grounded only in a compact, verified synthetic-data payload
- A deterministic Python fallback when Gemini is unavailable

## Core Metrics

### Risk and asset quality

- Risk-Weighted Assets (RWA)
- Exposure at Default (EAD)
- Gross Carrying Amount (GCA)
- Provisions and illustrative cost of risk
- Stage 1, Stage 2 and Stage 3 portfolio shares
- Stage 3 / illustrative NPL ratio
- Provision coverage ratio
- RWA density

### Balance sheet

- Loans and loan growth
- Deposits, deposit growth and monthly deposit movements
- Loan-to-deposit ratio
- High-Quality Liquid Assets (HQLA)
- Wholesale funding

### Earnings

- Net Interest Income (NII)
- Net Interest Margin (NIM)
- Operating income and operating costs
- Cost-to-Income ratio
- Pre-tax profit margin

### Capital and liquidity

- CET1 ratio
- Tier 1 ratio
- Total capital ratio
- Leverage ratio
- Liquidity Coverage Ratio (LCR)

## Application Capabilities

| Component | Capability |
|---|---|
| Morning Health Check | Executive KPI snapshot, red/amber/green status indicators, trend charts and latest drivers |
| What-If Engine | User-defined interest-rate shocks, deposit outflows, Stage 2 migration and Stage 3 migration |
| Stress Library | Baseline, moderate recession, severe recession and liquidity-run scenarios with macroeconomic assumptions |
| Horizon View | Linear-trend forecasts for capital, liquidity, earnings and asset quality, including confidence intervals and target lines |
| AI Financial Partner | Grounded explanations of NIM, capital, RWA, liquidity and recommended management options |
| Gemini Narrative Layer | Optional executive-ready summaries based on verified synthetic cockpit facts only |

## Architecture

```text
Synthetic bank data generator
            ↓
Metrics calculation layer
            ↓
Scenario / stress-testing / forecasting engines
            ↓
Streamlit CFO dashboard
            ↓
Deterministic financial assistant and optional Gemini narrative layer
```

The Python calculation modules are the source of truth. The LLM is used only to turn verified, supplied metrics into concise executive language; it is not allowed to calculate banking ratios, create stress-test values, access bank systems, or execute actions.

## Project Structure

```text
AI-Native-Morning-Cockpit/
├── main.py                         # Streamlit application entry point
├── requirements.txt                # Python dependencies
├── .env.example                    # Gemini key template; no real secret
├── .gitignore                      # Excludes secrets and local files
├── data/                           # Optional generated synthetic data
└── src/
    ├── __init__.py
    ├── data_generator.py           # Synthetic bank balance sheet and P&L history
    ├── metrics.py                  # Capital, liquidity, earnings and credit metrics
    ├── scenarios.py                # Custom what-if scenario engine
    ├── stress_scenarios.py         # Named macroeconomic stress scenarios and limits
    ├── forecasting.py              # Linear-trend forecast and confidence intervals
    ├── ai_partner.py               # Deterministic conversational financial assistant
    └── gemini_partner.py           # Optional Gemini narrative integration
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure Gemini (optional)

The deterministic AI Financial Partner works without an API key.

To enable Gemini executive narratives:

1. Copy `.env.example` and rename the copy to `.env`.
2. Add your own API key:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

3. Never commit or share `.env`.

### 5. Run the application

```powershell
streamlit run main.py
```

The app will open locally in your browser, normally at `http://localhost:8501`.

## Usage

### Morning Health Check

Use the first tab for the current executive overview of capital, liquidity, earnings, balance-sheet movements, and asset quality.

### What-If Engine

Use the sliders to test combinations of:

- ECB policy-rate shocks
- Deposit outflows
- Stage 2 migration
- Stage 3 migration

The engine recalculates impacted metrics rather than changing dashboard ratios directly.

### Stress Scenario Library

Select a named scenario to evaluate illustrative macroeconomic shocks, including:

- GDP contraction
- Unemployment increase
- Interest-rate change
- Residential and commercial-property shocks
- Funding spread widening
- Deposit outflow
- PD/LGD severity overlays
- EAD and RWA deterioration

### Horizon View

Select the forecast horizon and historical training window. The dashboard projects key metrics with a linear-trend model and shows a confidence interval around the estimated mean trend.

> The confidence interval is not a full prediction interval, macroeconomic stress range, or validated regulatory forecast.

### AI Financial Partner

Example questions:

```text
Give me the morning briefing
Why did NIM change?
Explain the CET1 ratio and RWA movement
Assess liquidity and deposit movements
Simulate a further 50 bps rate cut
What actions do you recommend?
```

## Model Governance Principles

- **Traceability:** dashboard metrics are derived from transparent Python formulas.
- **Separation of duties:** data generation, metric calculation, scenarios, forecasts, UI and LLM narrative are separated into modules.
- **LLM grounding:** Gemini receives only a restricted verified-facts payload.
- **No autonomous execution:** the assistant provides decision support only and cannot execute banking actions.
- **Fallback control:** deterministic analytical answers remain available when the external LLM is unavailable.
- **Synthetic-data disclosure:** all outputs are clearly labelled as illustrative.

## Limitations

This project is a hackathon prototype and is not a production banking system. It does not include:

- Actual bank or customer data
- Validated regulatory capital, liquidity, IFRS 9, IRRBB or stress-testing calculations
- Approved regulatory minimums or internal risk-appetite limits
- Live market, macroeconomic or news feeds
- Full balance-sheet modelling, behavioural assumptions or hedging models
- Model validation, back-testing, monitoring, audit trails or production access controls
- Production-grade security, identity management or deployment controls

## Suggested Future Enhancements

- Connect approved internal and external data sources through governed pipelines
- Add portfolio segmentation by country, business line and product
- Implement scenario versioning, model monitoring and back-testing
- Introduce IRRBB EVE and NII modelling with behavioural deposit assumptions
- Add scenario-driven forecast distributions and Monte Carlo simulation
- Use controlled LLM function calling to route questions into approved scenario and analytics tools
- Add a news retrieval layer with source citations and explicit data governance

## License

For hackathon and demonstration use only. Confirm your organisation's requirements before publishing, sharing or reusing this repository.
