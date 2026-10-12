# 🔎 SpyTrace

### Uncover the Digital Footprints.

SpyTrace is a Python-based **Open-Source Intelligence (OSINT) toolkit** designed to help users gather and analyze publicly available information through a collection of lightweight reconnaissance modules.

The project combines phone number intelligence, IP intelligence, username footprint scanning, and email breach checking in one command-line tool.

<img src="assets/intro.png" alt="SpyTrace Intro" width="600"/>

## ✨ Features

- 📱 **Phone Number Intelligence** — Retrieve number validation, carrier, geographical description, timezone, and number type.
- 🌐 **IP Intelligence** — Retrieve IP-related information such as country, region, city, ISP, ASN, and other available network details.
- 👤 **Username Footprint Scanner** — Search candidate profile URLs across multiple social media and developer platforms.
- 📧 **Email Breach Checker** — Check whether an email address appears in known data breach records using XposedOrNot.
- 🎨 **Rich CLI Output** — Display formatted terminal output using the Rich library.

<img src="assets/intro2.png" alt="SpyTrace Logo" width="200"/>

## 🛠️ Built With

- Python 3
- [phonenumbers](https://pypi.org/project/phonenumbers/)
- [Requests](https://pypi.org/project/requests/)
- [Rich](https://pypi.org/project/rich/)
- [XposedOrNot](https://pypi.org/project/xposedornot/)

## 📂 Project Structure


```text
SpyTrace/
├── trace.py
├── options.py
├── assets/
│   ├── intro.png
│   └── intro2.png
├── requirements.txt
├── README.md
└── .gitignore
```


*Adjust the filenames above to match your actual project structure.*

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/coding-enthusiast003/SpyTrace.git
cd SpyTrace
```

### 2. Create a virtual environment (recommended)

**Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run SpyTrace

**Linux:**

```bash
python3 spytrace.py
```

If the script has a valid Python shebang and executable permissions, you can also run:

```bash
chmod +x spytrace.py
./spytrace.py
```

**Windows:**

```powershell
python spytrace.py
```

## 🚀 Usage

Launch SpyTrace and select the available module from the command-line interface.

Depending on the selected module, you can:

1. Analyze phone number information.
2. Retrieve IP intelligence.
3. Check candidate username profile URLs.
4. Check email addresses against known breach records.

Follow the prompts displayed in the terminal.

## 🔐 Privacy & Responsible Use

SpyTrace is intended for educational purposes, authorized investigations, and responsible OSINT research.

- Only investigate information you are authorized to access.
- Use email breach checks responsibly and respect other people's privacy.
- Do not use results to harass, impersonate, or target individuals.
- Treat results as indicators, not definitive proof of identity or compromise.
- External APIs may have rate limits, availability restrictions, and their own terms of use.
- A missing result does not guarantee that information has never been exposed.

## ⚠️ Limitations

- Results depend on the data returned by external services.
- Username profile URLs may return false positives or inconclusive results; an HTTP 200 response does not always mean a profile exists.
- IP geolocation is approximate and does not identify a person's exact physical location.
- Phone number metadata does not establish the current location or identity of the owner.
- Email breach checks only cover records known to the selected service.


## 🤝 Contributing

Suggestions, bug reports, and contributions are welcome. Feel free to open an issue or submit a pull request.

## ⚖️ Disclaimer

SpyTrace is provided for educational and legitimate security research purposes. Users are responsible for complying with applicable laws, service terms, and privacy requirements when using this tool.

## 🚧 Future Development

SpyTrace is an evolving project, and more features, modules, and improvements may be added in the future as the toolkit grows.

Stay tuned for upcoming updates! 🚀

## 👨‍💻 Author

**Coding-Enthusiast003**

Explore the project and follow its development on [GitHub](https://github.com/coding-enthusiast003).

---

⭐ If you find SpyTrace useful, consider giving the repository a star.
