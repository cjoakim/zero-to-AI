# Part 1, Session 1 - Git and GitHub


## Preamble

- There are some things we don't think about much with modern technology 
  - They just work, but they're amazing and complex
  - Like, how do cell phones work?
  - Like, how does the Internet work?
  - Like, how do we coordinate the changes of many people working on the same codebase?
  - **Git was created by Linus Torvalds for the development of Linux**
    - To more easily manage the many contributions by a worldwide Dev Team
    - It just works, beautifully
    - It is so much better that what came before it (CVS, SVN, VSS, Panvalet, etc.)

## Description

- **Git** is a **distributed** and modern Source Control System (DSCM)
- It does not use a **locking** model
- It has some amazing **merge** functionality
  - Allows several developers to concurrently work on the same file
- It creates versions of each file, with incremental changes
  - Allows you to revert to a previous version of the code
  - Allows you to see a **diff** of the changes between two versions of the code
- **GitHub is a cloud-based PaaS (platform as a service) for Git**
  - GitLab, BitBucket, and others
- Git can be used locally on your workstation without GitHub
- The .gitignore file
  - Is used to specify the files and paths shouldn't be stored in git
  - secrets, passwords, URLs, credentials, etc.
  - binary files produced in the compilation and build process 
  - output files from the execution of the program
  - the python virtual environment directory
- Branches
  - The **main** branch is deployed to production
  - Developers create **feature branches** then **merge** these changes into the main Branch
  - You can **rebase** a feature branch to catch it up with the main branch
- Pull Requests (i.e. - PRs)
  - Area peer requests to review and merge a feature branch into the main branch
  - There are many ways to do this - approver lists, workflows, CI/CD DevOps, etc.
  - This is out-of-scope for this series

## Installation

This is required for this series, so that you can clone the Series GitHubrepository.

 -[Download](https://git-scm.com/install/)
 -[macOS Homebrew](https://formulae.brew.sh/formula/git)

## GitHub Account Creation

This is optional for this series, but strongly recommended for your career.

 -[Account Creation](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github)
 -[Types of Accounts](https://docs.github.com/en/get-started/learning-about-github/types-of-github-accounts)

## Configuration

Configure your user.name and user.email.

```
git config --help 

git config --list 

git config --global user.name  "Jane Smith"
git config --global user.email "jane.smith@gmail.com"
```

## Authentication

- Password and SSH (secure shell protocol)
 -[GitHub Authentication Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)

## Git Commands

See the [docs](https://git-scm.com/docs) for more information on the following commands.

This [Git Cheat Sheet](https://git-scm.com/cheat-sheet) is useful for reference.

- [git help](https://git-scm.com/docs/git-branch) - create a new branch
- [git clone](https://git-scm.com/docs/git-clone) - copy a remote repository to your local machine
- [git ls-files](https://git-scm.com/docs/git-ls-files) - see a list of the files in the repository
- [git status](https://git-scm.com/docs/git-status) - see the status of the repository
- [git pull](https://git-scm.com/docs/git-pull) - fetch and merge changes from a remote repository
- [git push](https://git-scm.com/docs/git-push) - push changes to a remote repository
- [git checkout](https://git-scm.com/docs/git-checkout) - switch to a different branch
- [git commit](https://git-scm.com/docs/git-commit) - commit changes to the repository

### Cloning a Repository, and keeping it up to date

These are the only git commands you'll need to do in this series.

### First, copy the remote GitHub repository to your local machine

```
git clone https://github.com/cjoakim/zero-to-AI.git
```

### Then, keep it up-to-date each week 

I plan on updating the repository each week, on Sundays, with new content
for the next week's sessions.

```
git pull
```

### Creating a Branch 

This is for your information only; you won't have to do this in this series.

```
cd  <github project root directory>
git checkout main                      # navigate to the main branch of development
git pull                               # pull the latest code from GitHub
git branch cj-8822                     # create a local branch (a feature branch, JIRA item 8822) for your work
git checkout cj-8822                   # change to that local branch
git push -u origin cj-8822             # push that branch to the remote repository

... edit with the code on your local machine ...

git add <file>
git commit -m "A description of the changes"
git push                               # push the committed local changes to the remote repository

... work with the code on your local machine some more ...

git add --all
git commit -m "A description of the changes"
git push                               # pushes the committed local changes to the remote repository
```

Then optionally create a "Pull Request" in the GitHub UI to request a peer review and approval.
There are many ways to do this - approver lists, workflows, CI/CD DevOps, etc.
This is out-of-scope for this series.


## GitHub Desktop UI

 -[Installation](https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop)

<p align="center">
   <img src="img/github-desktop.png" width="95%">
</p>


## Pro Tip: Aliases I use

- Added to ~/.bash_profile (macOS) or Windows 11 Profile as functions
- gb = what branch am I on?
- gls = list files in the repository
- gs = git status
- gup = git pull, reset, gc, branch
- gurl = get the remote origin url

```
alias gb='git branch'
alias gls='git ls-files'
alias gs='git status'
alias gup='git status ; git reset --hard ; git pull ; git gc ; git branch'
alias gurl='git config --get remote.origin.url'
```

### Windows PowerShell Profile Functions 

```
function gb {
    git branch
}

function gls {
    git ls-files
}

function grh {
    git reset --hard
}

function gs {
    git status
}

function gup {
    git status ; git reset --hard ; git pull ; git gc ; git branch
}

function gurl {
    git config --get remote.origin.url
}
```

## References

- [Linux Torvalds on Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds)
