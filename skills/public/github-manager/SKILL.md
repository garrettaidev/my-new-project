---
name: github-manager
description: Manage GitHub repositories and actions, including creating repos, pushing code, and other repository controls. Use when the user asks to interact with their GitHub account (e.g., create a new repository, push a file, list repositories).
---

# GitHub Manager Skill

This skill allows me to interact with your GitHub account using the GitHub CLI (`gh`).

## Available Actions:

### Create a new repository
To create a new repository, I will use the `gh repo create` command.

### Push files to a repository
To push files to a repository, I will need to:
1. Initialize a local git repository if one doesn't exist.
2. Add the GitHub repository as a remote.
3. Add the files.
4. Commit the changes.
5. Push the changes to the remote repository.

## Important Notes:

- I will use your pre-authenticated GitHub CLI (`gh`) for all operations.
- For sensitive operations or when in doubt, I will ask for your confirmation.
- Ensure the PAT you provided has the necessary scopes for the requested actions.
