# Git Tutorial: From Staging to CI/CD Pipeline

Welcome to the comprehensive Git tutorial! In this guide, we will cover everything you need to know about Git, from the basics of version control to integrating with a CI/CD pipeline.

## Table of Contents

- [Git Tutorial: From Staging to CI/CD Pipeline](#git-tutorial-from-staging-to-cicd-pipeline)
  - [Table of Contents](#table-of-contents)
  - [Introduction to Git](#introduction-to-git)
  - [Setting Up Git](#setting-up-git)

## Introduction to Git

Git is a distributed version control system that helps you manage and track changes to your codebase over time. It allows multiple collaborators to work on a project simultaneously and maintain a history of changes.

## Setting Up Git

1. Install Git: Download and install Git from [https://git-scm.com/](https://git-scm.com/).

2. Configure Git: Set your name and email using these commands:
   ```sh
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"

3. Basic Git Workflow
   1. Initializing a Repository: Create a new repository or clone an existing one.
   ```sh
    git init            # Initialize a new repository
    git clone <URL>      # Clone an existing repository
    ```
   2. Staging Area and Committing:
   ```sh
    git add <file(s)>   # Stage specific file(s)
    git add .           # Stage all changes
   ```
4. Branching and Merging
    1. Create a new branch:
    ```sh
    git checkout -b new-feature    # Create and switch to a new branch
    ```
    2. Switching Between Branches:
    ```sh
    git checkout <branch-name>      # Switch to an existing branch
    ```
    3. Merge a branch into the current branch
    ```sh
    git merge <branch-name>
    ```


