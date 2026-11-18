# GTA VI Discord Rich Presence

A simple Python script that displays **Grand Theft Auto VI** as your current Discord activity.

## Features

- Shows Grand Theft Auto VI on your Discord profile
- Displays a custom activity description
- Shows an elapsed time counter
- Closes the Rich Presence connection when stopped

## Discord Accounts

- `fewnice`
- `oll.a`

## Requirements

- Python 3.9 or newer
- Discord Desktop running on your computer
- An active internet connection for installing the dependency

The Discord web version does not support local Rich Presence connections.

## Installation

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Install the dependency:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the script:

   ```bash
   python main.py
   ```

On Windows, you can also run `start.bat`.

## Stop the Script

Press `Ctrl+C` in the terminal to stop the activity.

## Safety and Disclaimer

- This project uses Discord Rich Presence through the local Discord Desktop client.
- It does not ask for your Discord password, account token, or bot token.
- It changes your Discord activity only. It does not launch GTA VI or mean that the game is actually running.
- This is an unofficial fan-made project and is not affiliated with Rockstar Games, Take-Two Interactive, or Discord.

## Built With

- Python
- [pypresence](https://github.com/qwertyquerty/pypresence)
