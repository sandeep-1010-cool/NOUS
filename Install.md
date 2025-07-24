Great! Here's a **complete step-by-step guide** to help you **set up Python (without admin rights)**, install **`pip`**, and then set up **Claude AI using Git Bash on Windows**.

---

# ✅ FULL GUIDE: Claude AI Setup with Python & Git Bash (No Admin)

---

## 🔹 PART 1: Install Python Without Admin Rights

### ✅ Step 1: Download Python Installer

* Go to: [https://www.python.org/downloads/windows](https://www.python.org/downloads/windows)
* Download the latest **64-bit executable installer** (e.g., `python-3.13.5-amd64.exe`)

---

### ✅ Step 2: Install Python for Current User

1. Run the installer [Custom installation]

2. On the **"Optional Features"** screen:

   * ✅ Check: `pip`
   * ✅ Check: `py launcher`
   * ❌ Leave "for all users" **unchecked**
   * All others (documentation, IDLE) are optional

3. On the **"Advanced Options"** screen:

   * ✅ Leave **"Install for all users" unchecked**
   * ✅ Check: `Create shortcuts`
   * ❌ Do NOT check `Add Python to environment variables` (needs admin)
   * Install to:

     ```
     C:\Users\<YourUser>\AppData\Local\Programs\Python\Python313\
     ```

4. Click **Install**

---

### ✅ Step 3: Verify Python & pip in Git Bash

Open **Git Bash**, then:

```bash
'/c/Users/<YourUser>/AppData/Local/Programs/Python/Python313/python.exe' --version
'/c/Users/<YourUser>/AppData/Local/Programs/Python/Python313/Scripts/pip.exe' --version
```

If you see Python and pip versions, ✅ it’s working.

---

### ✅ Step 4: Optional – Add Aliases

To make `python` and `pip` work globally in Git Bash:

```bash
nano ~/.bashrc
```

Add these lines (replace your actual path):

```bash
alias python='/c/Users/346527/AppData/Local/Programs/Python/Python313/python.exe'
alias pip='/c/Users/346527/AppData/Local/Programs/Python/Python313/Scripts/pip.exe'
```

Save and reload:

```bash
source ~/.bashrc
```

Now you can run `python` and `pip` directly.

---

## 🔹 PART 2: Install Claude AI SDK

### ✅ Step 5: Install Claude SDK

Run:

```bash
pip install anthropic
```

---

### ✅ Step 6: Get Claude API Key

1. Go to: [https://console.anthropic.com](https://console.anthropic.com)
2. Sign in (or sign up)
3. Go to **API Keys** section
4. Click **Create Key**, copy it

---

### ✅ Step 7: Export Claude API Key (Temporary)

In Git Bash:

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

This allows your scripts to authenticate with Claude.

---

## 🔹 PART 3: Test Claude AI from Git Bash

### ✅ Step 8: Create a Claude Chat Script

Run:

```bash
nano claude_test.py
```

Paste:

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello Claude, how are you?"}
    ]
)

print(response.content[0].text)
```

Save: `Ctrl+O → Enter → Ctrl+X`

---

### ✅ Step 9: Run the Script

```bash
python claude_test.py
```

🎉 You should see a response from Claude right in your terminal!

---

## 🧩 Optional (Secure + Convenient)

| Task                      | Command                                           |
| ------------------------- | ------------------------------------------------- |
| Store API Key permanently | Add `export ANTHROPIC_API_KEY=...` to `~/.bashrc` |
| Use `.env` securely       | Use `python-dotenv` library                       |
| CLI integration           | Build simple `chat.py` CLI to query Claude        |

---

## ✅ Final Result

You now have:

* ✅ Python 3.13.5 (no admin)
* ✅ pip working
* ✅ Claude SDK installed
* ✅ Claude AI callable via Git Bash

---