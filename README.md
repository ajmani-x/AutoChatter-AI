# AutoChatter-AI

An AI-powered WhatsApp automation bot that reads incoming messages and responds using Cohere’s language model.

## 📋 Features
- Reads incoming WhatsApp messages using screen automation
- Gets smart replies using Cohere AI
- Sends auto-generated replies via PyAutoGUI
- Simple, lightweight, and runs locally

## ⚠️ Note on Compatibility
This script uses **hardcoded screen coordinates**, optimized for a specific display layout (e.g., my MacBook screen).  
To run it on another system, you may need to:
- Update the coordinates manually
- OR use dynamic detection like `pyautogui.locateOnScreen()` (recommended for cross-platform compatibility)

## 🚀 How to Use

1. **Install required libraries**:
   ```bash
   pip install pyautogui pyperclip cohere