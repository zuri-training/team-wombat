# How to Contribute to this Project

Clone the project

```bash
git clone https://github.com/zuri-training/team-wombat.git
```

Go to the project directory

```bash
cd team-wombat
```

---

## For the backend developers
<details><summary>Run Locally</summary>

Create a virtual environment and install needed dependencies in it

```bash
py -m venv venv 
```

Activate the virtual environment

```bash
 venv/bin/activate
```
```ubuntu
virtualenv venv
```
Actiavte the virtual environtment

```ubuntu
source venv/Scripts/activate
```
Activate the virtual environment
</details>

*If you'll just be working on the front-end, the *running locally* section is optional. All your `HTML`, `CSS`, and `JavaScript` files should go into the [`templates`](https://github.com/zuri-training/team-wombat/tree/main/wombat/wombat/templates) directory.* **Will be updated later**

---

Create a branch to make your changes to.

```bash
git branch <your-github-username_feature>
```

Switch into your branch

```bash
git checkout <your-github-username_feature>
```
  
Set Upstream branch

```bash
git push --set-upstream origin <your-github-username_feature>
```

Commit and push your changes to your branch.

```bash
  git add . || git add --all || git add -A
  git commit -m <commit-message>
  git push
```

> You can also just *fork* the repository and make your changes to that fork.

**Create a pull request** on the [GitHub Repository](https://github.com/zuri-training/team-wombat). [Learn How](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

**Request a review for your pull request** from [Hope Damilola Yakubu](https://github.com/Hopeee619)

Your changes will be merged into the `main` branch when they are approved by the reviewers.

<!-- ## Major packages used at the moment (list will be updated as we progress)
