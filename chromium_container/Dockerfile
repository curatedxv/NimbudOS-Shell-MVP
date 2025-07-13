FROM zenika/alpine-chrome

ENTRYPOINT ["chromium", "--headless", "--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage", "--enable-features=WebRTC", "--remote-debugging-address=0.0.0.0", "--remote-debugging-port=9222", "https://boosteroid.com/"]
