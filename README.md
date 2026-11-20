# Tiny Game

A tiny pygame game for practicing two things in this course:

1. Cloning a repo with `git clone`
2. Installing requirements with `pip install -r requirements.txt`

Use the left and right arrow keys to dodge the red blocks.

## Steps
### 1. Fork

1. Click **Fork** at the top right of this page.
2. Keep the repository name **TinyGame**. Leave  **Copy the main branch only** ticked, and click **Create fork**.

### 2. Clone

```bash
git clone https://github.com/idawaty/TinyGame.git
cd TinyGame
```
### 3. Create a virtual environment

```bash
sudo apt install -y python3.14-venv 
python3 -m venv venv
source venv/bin/activate       
```

### 3. Install requirements

```bash
pip install -r requirements.txt
```

### 4. Run

```bash
python3 game.py
```

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `No module named pygame` | Activate the virtual environment, then run step 3 again |
| `pip: command not found` | Use `python3 -m pip install -r requirements.txt` |
| `fatal: not a git repository` | Run `cd TinyGame` first |
| GUI does not open | pygame needs a desktop display (it won't work over plain SSH) |

#### Your Name
