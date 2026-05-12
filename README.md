# AI-Powered PR Code Review

Automated first-level code review using Claude AI. Analyzes PRs for:
- Null/undefined checks
- Logic errors and bugs
- Code style issues
- Performance concerns
- Security vulnerabilities
- Test coverage gaps

## Setup Instructions

### 1. Add Claude API Key to GitHub Secrets

1. Go to your GitHub repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `CLAUDE_API_KEY`
4. Value: Your Claude API key from [Anthropic Console](https://console.anthropic.com/keys)
5. Click **Add secret**

### 2. Enable GitHub Actions

1. In your repo, go to **Actions** tab
2. Click **I understand my workflows, go ahead and enable them**
3. Done!

### 3. Test It

1. Create a new branch with some code changes
2. Open a Pull Request
3. The workflow will automatically run and post a review comment
4. Look at the PR for the AI review summary

## How It Works

- **Trigger**: Runs on every PR (opened, synchronized, reopened)
- **Analysis**: Extracts diff and sends to Claude for analysis
- **Output**: Posts findings as a PR comment
- **Result**: Human reviewer gets a summary before doing full review

## Customization

Edit `.github/workflows/pr-review.yml` to:
- Change trigger events (`pull_request` section)
- Adjust analysis criteria in `pr_reviewer.py`
- Filter languages (add `paths` to workflow)

## Cost

- Claude API: ~$0.01-0.05 per PR analysis (varies by diff size)
- GitHub Actions: Free tier includes 2,000 minutes/month
- Total: Essentially free for small teams

## Example Output

The PR comment will look like:

```
🤖 Automated Code Review

- **Null Checks**: Line 45 - Missing null check on user.email
- **Logic Error**: Line 78 - Condition logic appears reversed
- **Performance**: Line 120 - Loop could use early exit
- **Testing**: Consider adding test for edge case on line 50

This is a first-level automated review to speed up human review. Please review the code yourself before approving.
```
