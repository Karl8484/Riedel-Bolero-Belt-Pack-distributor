# Beltpack O'matic

A Python script for a Raspberry Pi that gets the belt pack long names from Riedel (via RRCS) and shows them full screen on a display at the belt pack shelf, so technicians can find their belt pack.

## What it does

- Requests the belt pack names from the RRCS server
- Sorts them by belt pack number
- Shows them on screen in the same layout as the shelf
- Refreshes every minute

## Requirements

- Python 3 with `requests` and Tkinter
- Network access to the RRCS server


## Setup

1. Put these files in the same folder: `BPOmatic.py`, `request.xml`, `image2.png` (background image).
2. In `BPOmatic.py`, replace the RRCS address with your own.
3. Name belt packs like this in Director: `BP <number> <name>` (for example `BP 12 John`).


Press **q** to quit.

Enjoy
