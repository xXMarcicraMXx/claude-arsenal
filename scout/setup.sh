#!/bin/bash
set -euo pipefail

ARSENAL_DIR="$HOME/claude-arsenal"

echo "=== Claude Arsenal Scout Setup ==="

if [ ! -d "$ARSENAL_DIR" ]; then
    git clone git@github.com:xXMarcicraMXx/claude-arsenal.git "$ARSENAL_DIR"
fi

cd "$ARSENAL_DIR/scout"

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

if [ -z "${GITHUB_TOKEN:-}" ]; then
    echo "NOTE: GITHUB_TOKEN not set (optional, 60 req/h without, 5000 with)"
    echo "Create at https://github.com/settings/tokens (public_repo scope only)"
fi

CRON_CMD="cd $ARSENAL_DIR/scout && .venv/bin/python scout.py >> /var/log/arsenal-scout.log 2>&1"
(crontab -l 2>/dev/null | grep -v "arsenal-scout" ; echo "0 6 * * 1 $CRON_CMD") | crontab -

sudo touch /var/log/arsenal-scout.log
sudo chown "$(whoami)" /var/log/arsenal-scout.log

echo ""
echo "=== Setup complete ==="
echo "Test with: source .venv/bin/activate && python scout.py --dry-run --verbose"
echo "Cron registered: every Monday at 06:00 UTC"
