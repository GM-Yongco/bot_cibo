#!/bin/bash
set -e  # stop on first error
LOG="$HOME/git/bot_cibo/autostart/autostart_cibo_backend.log"
exec > >(tee -a "$LOG") 2>&1

tmux new -d -s cibo_backend || true # wont stop if tmux session notif already exists
tmux send-keys -t cibo_backend "cd ~"  C-m
tmux send-keys -t cibo_backend "source venv_api/bin/activate"  C-m
tmux send-keys -t cibo_backend "cd ~/git/bot_cibo/backend" C-m
tmux send-keys -t cibo_backend "python3 main.py" C-m
