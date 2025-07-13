# NimbusOS Shell MVP 🚀

**NimbudOS Shell MVP** is an early-stage, minimal desktop shell built with Python and PyQt5. It provides a **cloud-first** user interface that serves as a simple launcher for web-based applications, using an embedded browser (WebView). The project is a personal proof-of-concept aiming to evolve into a lightweight operating system shell optimized for cloud apps and requiring minimal local resources.

## 🚀 Features

- **Basic Launcher UI**  
  Clean, launcher-style interface with buttons for key web apps (Boosteroid, Google Docs, Sheets, Slides).

- **Embedded WebView Shell**  
  Web apps run inside the shell in fullscreen via PyQt5’s built-in browser component—no external browser needed.

- **Cloud-First Design**  
  Heavy workloads are offloaded to the cloud. The shell itself stays lightweight, ideal for low-power hardware.

- **Flexible Deployment**  
  Run as a standalone desktop app, replace your system shell, or launch inside a Docker container (`chromium_container/` included).

---

## 🛠️ Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/curatedxv/NimbudOS-Shell-MVP.git
   cd NimbudOS-Shell-MVP
2. **(Optional) Create & activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Linux/Mac
   # venv\Scripts\activate       # Windows
3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
4. **(Optional) Docker container mode**  
   ```bash
   cd chromium_container
   chmod +x start.sh
   ./start.sh
   This will build & run a headless Chromium container with DevTools enabled on port 9222.
---

## 🔮 Future Plans

- **Develop a full operating system (NimbusOS)**  
  Evolve this shell into a complete, installable OS desktop environment for Linux.

- **Seamless cloud integration**  
  Offload demanding workloads (gaming, office suites, media editing) to a containerized cloud backend, ensuring smooth performance on any device.

- **Global accessibility**  
  Implement multilingual support, low-bandwidth modes, and offline fallbacks to serve users in all regions.

---

## 🤝 Contributing

Contributions welcome!  
- **Issues:** Report bugs or request features.  
- **Pull Requests:** Fork the repo, implement improvements, and submit a PR.  

---

## 📄 License

Licensed under the **MIT License**. See the `LICENSE` file for full terms.



