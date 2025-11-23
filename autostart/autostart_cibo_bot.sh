#!/bin/bash
set -e  # stop on first error
LOG="$HOME/.config/autostart/autostart_cibo_bot.log"
exec > >(tee -a "$LOG") 2>&1

tmux new -d -s cibo_bot | true
tmux send-keys -t cibo_bot "cd ~"  C-m
tmux send-keys -t cibo_bot "source venv_discord/bin/activate"  C-m
tmux send-keys -t cibo_bot "cd ~/git/bot_cibo/bot" C-m
tmux send-keys -t cibo_bot "python3 main.py" C-m