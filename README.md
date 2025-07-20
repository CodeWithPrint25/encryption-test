# 🔒 Voldemort.py — My File Locking Project

Hi! I’m 10 years old and I made this so I can learn how to lock and unlock files with Python. It’s just for fun and learning — not for being mean or hacking!

---

## Important stuff you gotta know:

- You run `voldemort.py` to lock your files.
- It makes a secret key file called `thekey.key` by itself.
- Don’t delete the `thekey.key` or you won’t be able to unlock your files later!
- Don’t run `decrypt.py` by itself — it won’t work right. Only run it from `voldemort.py`!

---

## How it works:

1. Run `voldemort.py`
2. It looks for files and locks them with a secret key.
3. It asks you for a secret phrase.
4. If you type the right phrase, it runs `decrypt.py` and unlocks your files again.

---

## Why no key on GitHub?

Because every time you run `voldemort.py`, it makes a new secret key! That way everyone gets their own secret code, like a real spy.

---

## This is just for fun and learning!

Don’t run it on important files or stuff you care about.  
If you don’t understand something, ask a grown-up or a teacher to help you.

---

## What’s in the project?

- `voldemort.py` — The main script that locks and asks for the secret phrase  
- `decrypt.py` — The file that unlocks stuff (but only run it from `voldemort.py`!)  
- `thekey.key` — The secret key that helps unlock files (created when you run `voldemort.py`)

---

## Remember!

- Don’t run this on files you need!  
- Keep your secret key safe and don’t share it with others.  
- Always run `decrypt.py` only from `voldemort.py`.

---

Thanks for checking out my project! Happy coding! 🐍😄
