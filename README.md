<h1 align="center">
  <br>
  <img src="https://i.imgur.com/6vGHWMd.png" alt="Telegram File Proxy Bot" width="200">
  <br>
  Telegram File Proxy Bot 🚀
  <br>
</h1>

<h4 align="center">A lightning-fast proxy for downloading and streaming Telegram files without storage! ⚡</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

<p align="center">
  <img src="https://i.imgur.com/sXe7qTI.gif" alt="Telegram File Proxy Bot Demo">
</p>

## Key Features

* 🔥 Lightning Fast Downloads
* 🎥 Stream Video and Audio
* 🔐 No File Storage - Enhanced Privacy
* 🌈 Beautiful Web Interface
* 📱 Fully Responsive Design
* 🚀 Easy Deployment with Docker
* 🔧 Highly Customizable

<p align="center">
  <img src="https://i.imgur.com/QvkZhiG.png" alt="Features" width="600">
</p>

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) (which comes with [pip](https://pip.pypa.io/en/stable/)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/yourusername/telegram-file-proxy-bot.git

# Go into the repository
$ cd telegram-file-proxy-bot

# Install dependencies
$ pip install -r requirements.txt

# Run the app
$ uvicorn app.main:app --reload
```

> **Note**
> Don't forget to set up your `.env` file with your Telegram Bot Token!

## Download

You can [download](https://github.com/yourusername/telegram-file-proxy-bot/archive/main.zip) the latest version of Telegram File Proxy Bot for Windows, macOS and Linux.

## Credits

This software uses the following open source packages:

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [python-telegram-bot](https://python-telegram-bot.org/)
- [Tailwind CSS](https://tailwindcss.com/)

## License

MIT

---

> GitHub [@yourusername](https://github.com/yourusername) &nbsp;&middot;&nbsp;
> Twitter [@yourusername](https://twitter.com/yourusername)

<p align="center">
  <img src="https://i.imgur.com/LcMz9Uj.gif" alt="Star Animation" width="100">
  <br>
  <a href="#" id="star-button" onclick="this.innerHTML = parseInt(this.innerHTML) + 1 + ' ⭐️'">0 ⭐️</a>
  <br>
  <sub>Give this project a star if you found it useful!</sub>
</p>

<style>
  @keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
    100% { transform: translateY(0px); }
  }
  
  img[alt="Telegram File Proxy Bot"] {
    animation: float 6s ease-in-out infinite;
  }
  
  #star-button {
    display: inline-block;
    padding: 10px 20px;
    background-color: #f3f4f6;
    color: #1f2937;
    border-radius: 5px;
    text-decoration: none;
    transition: all 0.3s ease;
  }
  
  #star-button:hover {
    background-color: #e5e7eb;
    transform: translateY(-2px);
  }
</style>

<script>
  document.getElementById('star-button').addEventListener('click', function(e) {
    e.preventDefault();
    let stars = parseInt(this.innerHTML);
    this.innerHTML = (stars + 1) + ' ⭐️';
  });
</script>
