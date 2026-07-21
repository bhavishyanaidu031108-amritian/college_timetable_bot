# 📅 College Timetable Chat Bot

A Python-based chatbot that automatically sends the daily college timetable as a notification at a scheduled time. 
The bot also sends notification of saturday timetable that changes every week and some saturdays were holidays then we get a notification like "today is a holiday". 

---

# 📌 Overview

The College Timetable Chat Bot is designed to help students stay organized by automatically sending the day's class schedule without requiring them to check the timetable  everyday manually. The bot runs every day at a predefined time using GitHub Actions, making it accessible even when your personal computer is turned off. which saves time.

---

# ✨ Features

* 📅 Sends the daily timetable automatically.
* ⏰ Scheduled notifications at a fixed time every day.
* 📖 Supports different timetables for each day of the week.
* 🔄 Handles alternate Saturday schedules.
* ☁️ Runs automatically using GitHub Actions.
* 🤖 Telegram Bot integration for instant notifications.
* 🔒 Uses GitHub Secrets to securely store the Bot Token and Chat ID.

---

# 🛠️ Technologies Used

* Python 3
* Telegram Bot API
* GitHub Actions
* GitHub Secrets
* JSON
* Python-dotenv

---

# 📂 Project Structure

```text
## 📂 Project Structure

```text
College_TimeTable_Bot/
│
├── .github/
│   └── workflows/
│       └── timetable.yml          # GitHub Actions workflow
│
├── data/
│   └── timetable.xlsx             # Academic calendar & weekly timetable
│
├── src/
│   ├── excel_reader.py            # Reads timetable from Excel
│   ├── formatter.py               # Formats the timetable message
│   └── telegram_sender.py         # Sends Telegram notifications
│
├── main.py                        # Main program entry point
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables (local only)
├── .gitignore                     # Files ignored by Git
└── README.md                      # Project documentation
```
> **Note:** The `.env` file is used only for local development and is **not** uploaded to GitHub.  
> In GitHub Actions, `BOT_TOKEN` and `CHAT_ID` are stored securely as **GitHub Secrets**.
# ⚙️ How It Works

1. The timetable is stored in a JSON file.
2. GitHub Actions runs the workflow automatically every day at the scheduled time.
3. The bot checks the current day.
4. It retrieves the corresponding timetable.
5. The timetable is sent to your Telegram account using the Telegram Bot API.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

## 2. Move into the project folder

```bash
cd YOUR_REPOSITORY
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Create a `.env` file

```env
BOT_TOKEN=your_bot_token
CHAT_ID=your_chat_id
TIMEZONE=Asia/Kolkata
```

## 5. Run the bot

```bash
python main.py
```

---

# ⏰ Automation with GitHub Actions

The project uses **GitHub Actions** to execute the bot automatically at a scheduled time every day.

Benefits include:

* No need to keep your laptop running.
* Automatic execution in the cloud.
* Easy schedule customization using cron expressions.

---

# 📅 Timetable Format

Example:

```json
{
  "Monday": [
    "9:00 AM -Modelling simulation Analysis ",
    "9:50 AM - Data Structure and Algorithms",
    "10:25 AM-Object oriented programming"
    
  ]
}
```

---

# 📌 Future Improvements

* Multiple timetable support
* Holiday detection
* Exam timetable notifications
* Attendance reminders
* Assignment deadline reminders
* Custom notification times
* Web dashboard for editing the timetable

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 📄 License

This project is created for educational purposes.

---

# 👩‍💻 Author

**Bhavishya Pasumarthi**

AI & Data Science Student

GitHub: https://github.com/bhavishyanaidu031108-amritian

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!
# college_timetable_bot
