# LogiLight Deploy Key Setup

## ✅ Deploy Key Generated

A dedicated SSH deploy key has been created for the LogiLight repository.

### Public Key (Add this to GitHub)

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGbr9QNzE11AEsPpWrfMoxz5voOJIPVnvmvodTU1imLa logilight-deploy-key
```

---

## 🔧 Setup Instructions

### Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Repository name: `Logitech-Gaming-Keyboard-Mouse-Controls`
3. Description: `Easy RGB lighting control for Logitech gaming peripherals on Linux`
4. **Public** repository
5. **Don't** initialize with README, .gitignore, or license
6. Click **"Create repository"**

### Step 2: Add Deploy Key to Repository

1. Go to your new repository on GitHub
2. Click **Settings** (repository settings, not account settings)
3. Click **Deploy keys** (in the left sidebar under "Security")
4. Click **Add deploy key**
5. Fill in:
   - **Title**: `LogiLight Deploy Key`
   - **Key**: Paste the public key above
   - ☑️ **Allow write access** (check this box!)
6. Click **Add key**

### Step 3: Test SSH Connection

Once the deploy key is added, test the connection:

```bash
cd /home/robert/LogiLight
ssh -T git@github.com-logilight
```

You should see:
```
Hi ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls! You've successfully authenticated, but GitHub does not provide shell access.
```

### Step 4: Push to GitHub

```bash
cd /home/robert/LogiLight
git push -u origin main
```

---

## 🔐 SSH Configuration

The SSH config has been set up at `~/.ssh/config`:

```
# LogiLight Repository Deploy Key
Host github.com-logilight
    HostName github.com
    User git
    IdentityFile ~/.ssh/logilight_deploy
    IdentitiesOnly yes
```

Git remote is configured to use: `git@github.com-logilight:ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls.git`

---

## 🔑 Key Files

- **Private Key**: `~/.ssh/logilight_deploy` (keep secure, don't share!)
- **Public Key**: `~/.ssh/logilight_deploy.pub`
- **SSH Config**: `~/.ssh/config`

---

## ❗ Important Notes

- The private key stays on your system - never share it!
- The public key is added to GitHub as a deploy key
- Deploy keys are repository-specific (more secure than account-wide keys)
- **Allow write access** must be checked to push commits

---

## 🔄 After Push

Once successfully pushed, you can verify on GitHub:
- https://github.com/ProfessorMoose74/Logitech-Gaming-Keyboard-Mouse-Controls

Then configure repository settings:
- Add topics/tags
- Enable Discussions
- Add description in About section

---

Ready to test the connection and push!
