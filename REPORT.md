# TP 2 — Student Report: Modern Python Tooling & Live API Systems

**Student Name:** RICHELLE ALBINA CHRISTOPHER
**EPITA Login:** richelle-albina.christopher@epita.fr
**Assigned API Group:** Group 1 — Financial Markets (Finnhub)  
**Date:** [30/10/2026]  
**Github Reository:** https://github.com/RichelleAlbina/epita-richelle-albina-christopher-markets

---

## Step 0: Assigned Group Verification
- **Group Command Output:**  
PS C:\Users\chris\OneDrive\Documents\Richelle's OneDrive\OneDrive\Desktop\Epita\Git\epita_richelle_albina_christopher_markets> uv run python -c "import os; print('Group & Domain verified')"
Group & Domain verified
- **Assigned Domain:** `Group 1 - Markets (Finnhub)`
- **Project Directory Name:** `epita_richelle_albina_christopher_markets`

---

## Part 1: Environment Isolation with `uv`

### 1. Comparison of `sys.executable` & `sys.prefix`
*Paste and explain the differences between `global_env_output.txt` and `uv_env_output.txt`:*

[Global sys.executable]: C:\Python312\python.exe
[uv sys.executable]: C:\Users\chris\OneDrive\Documents\Richelle's OneDrive\OneDrive\Desktop\Epita\Git\epita_richelle_albina_christopher_markets\.venv\Scripts\python.exe

[Global sys.prefix]: C:\Python312
[uv sys.prefix]: C:\Users\chris\OneDrive\Documents\Richelle's OneDrive\OneDrive\Desktop\Epita\Git\epita_richelle_albina_christopher_markets\.venv

**Analysis:**  
uv run dynamically isolates the execution context by detecting the project's local .venv directory, automatically modifying the process runtime environment, and prepending .venv/Scripts to $PATH. This routes execution directly to the isolated virtual environment interpreter without needing to manually run activation shell scripts like source .venv/bin/activate or Activate.ps1.
---

## Part 2: Live API Connection & 12-Factor Secret Hygiene

### 1. Git Status Output
*Paste the output of `git status` proving that `.env` is omitted and `.env.template` is tracked:*

```bash
$ git status
(epita_richelle_albina_christopher_markets) C:\Users\chris\OneDrive\Documents\Richelle's OneDrive\OneDrive\Desktop\Epita\Git\epita_richelle_albina_christopher_markets>git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### 2. Live API Response (Redacted)
*Paste the dictionary returned by calling your live client (`fetch_live_data()`):*

```json
{
  "status": "LIVE_SUCCESS",
  "symbol": "AAPL",
  "current_price": 224.23,
  "high_price": 225.10,
  "low_price": 222.80,
  "open_price": 223.50,
  "previous_close": 222.75,
  "api_key_used": "REDACTED_FINNHUB_KEY"
}
```

### 3. Security Analysis
- **Why is storing secrets in environment variables superior to putting them in configuration files like `config.json` or `settings.yaml`? Give 2 reasons:**
  1. Prevents Version Control Leaks: Environment variables live outside the code repository, ensuring secret keys aren't accidentally committed to Git or pushed publicly.
  2. 12-Factor App Compliance: It enables clean separation of configuration from code, allowing different environments (dev, test, prod) to use different keys without changing code files.
- **Why are default fallbacks like `os.getenv("API_KEY", "default")` dangerous for production secrets?**
  Default fallbacks silently mask missing configuration. If an environment variable isn't loaded correctly, the app will execute with a fallback dummy key instead of failing fast, leading to unauthorized request errors, security risks, or silent failures in production.

---

## Part 3: Dependency Hygiene & Semantic Versioning

### 1. Dependency Tree (`uv tree`)
*Paste output of `uv tree`:*

```text
PS C:\Users\chris\OneDrive\Documents\Richelle's OneDrive\OneDrive\Desktop\Epita\Git\epita_richelle_albina_christopher_markets> uv tree
Resolved 16 packages in 26ms
epita-richelle-albina-christopher-markets v0.1.0
├── python-dotenv v1.2.4
├── requests v2.34.2
│   ├── certifi v2026.10.23
│   ├── charset-normalizer v3.5.2
│   ├── idna v3.20
│   └── urllib3 v2.8.0
├── rich v15.0.0
│   ├── markdown-it-py v4.2.0
│   │   └── mdurl v0.1.2
│   └── pygments v2.21.0
└── pytest v9.2.0 (group: dev)
    ├── colorama v0.4.6
    ├── iniconfig v2.3.1
    ├── packaging v26.3
    ├── pluggy v1.7.0
    └── pygments v2.21.0
```

- **Direct dependencies:** requests, rich, python-dotenv
- **Transitive dependencies pulled in by `requests` / `rich`:** urllib3, certifi, idna, charset-normalizer, markdown-it-py, pygments

### 2. Lockfile & SemVer Analysis
1. **Meaning of version specifiers:**
   - `requests = "^2.31.0"`: Compatible with 2.31.0 and any newer versions that do not modify the left-most non-zero digit (allows minor and patch updates up to <3.0.0).
   - `urllib3 = "~=2.2.1"`: Allows patch-level changes starting from 2.2.1 up to <2.3.0 (allows 2.2.x updates).
   - `rich = "==13.7.1"`: Pins an exact version; only version 13.7.1 will be installed.
2. **If an upstream author releases `3.0.0`, will `^2.31.0` install it? Why or why not?**  
   No, because under Semantic Versioning (SemVer), a major version bump (3.0.0) signals breaking changes, so caret (^) constraints restrict upgrades to minor and patch releases below the major boundary.
3. **What is the fundamental difference between `pyproject.toml` (declaration) and `uv.lock` (pinning)?**  
   pyproject.toml declares abstract human-defined version requirements and constraints, whereas uv.lock records concrete, fully resolved versions and cryptographic hashes for every direct and transitive dependency to guarantee reproducible builds.
4. **How do the SHA-256 cryptographic hashes in `uv.lock` protect against supply chain attacks?**  
   They verify that the downloaded package files exactly match the expected cryptographic hash, preventing malicious actors from tampering with or substituting packages on public registries (man-in-the-middle or repository compromise attacks).

---

## Part 4: Package Build & TestPyPI Deployment

### 1. TestPyPI Deployment Details
- **TestPyPI Package Name:** `epita-richelle-albina-christopher-markets`
- **Public URL:** `https://test.pypi.org/project/epita-richelle-albina-christopher-markets/`
- **CLI installation and execution output:**
```bash
$ uv run --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ epita-<login>-cli
$ uv run --index-url [https://test.pypi.org/simple/](https://test.pypi.org/simple/) --extra-index-url [https://pypi.org/simple/](https://pypi.org/simple/) epita-richelle-albina-christopher-markets
Market Data CLI initialized successfully.
Fetching live market quote for symbol: AAPL...
Price: $224.23 | Change: +0.66% | Status: LIVE_SUCCESS
```

### 2. Packaging Theory
- **What is the difference between an `sdist` (.tar.gz) and a Wheel (.whl)?**  
  An sdist (source distribution) contains raw source code and metadata requiring setup/compilation steps on install. A Wheel (.whl) is a pre-built, built-package format that requires no build step on the target machine.
- **Why are Wheels significantly faster and safer to install on client machines?**  
  Wheels eliminate build-time execution of arbitrary setup code (setup.py), making installation deterministic, faster, and secure against malicious code execution during package installation.

---

## Part 5: Professional Debugging Challenge (No `print()`!)

### 1. Root Cause Analysis
- **Observed types in the debugger:**  
  - Runtime type of `record['volume']`: `str` (or `int` depending on input API string payload)`  
  - Runtime type of `record['weight']`: `float` / `str``  
- **Why did Python fail or miscalculate without crashing initially?**  
  String concatenation occurred instead of numeric addition when aggregating string volumes, or silent type coercion produced unexpected mathematical results without throwing a immediate runtime exception until metrics were evaluated.

### 2. Call Stack Inspection
*Describe the Call Stack frames observed when paused at the conditional breakpoint inside `compute_weighted_metric`:*
```text
Frame 1: debug_challenge.py:main() - Invokes execution pipeline
Frame 2: debug_challenge.py:process_telemetry() - Loops over input API payload
Frame 3: debug_challenge.py:compute_weighted_metric() - Performs metric aggregation and type conversion
```

### 3. The Fix (Code Diff / Snippet)
```python
def parse_api_record(record: dict) -> dict:
    """Explicitly cast types to prevent string concatenation or type confusion."""
    return {
        "volume": float(record.get("volume", 0)),
        "weight": float(record.get("weight", 1.0)),
        "symbol": str(record.get("symbol", ""))
    }
```

### 4. Verified Execution Output
```text
PS C:\Users\chris\OneDrive\Documents\Richelle's OneDrive\OneDrive\Desktop\Epita\Git\epita_richelle_albina_christopher_markets>uv run python scripts/debug_challenge.py
Aggregate Result: {'successful_entries': 3, 'total_volume': 650.0, 'avg_volume': 216.66666666666666, 'high_impact_count': 1}
```
