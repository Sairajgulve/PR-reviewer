#!/usr/bin/env python3
"""
GitHub PR Code Review Analyzer using Google Gemini
Analyzes pull request diffs and generates a first-level review summary
"""

import json
import sys
import os
import google.genai as genai

def analyze_pr_diff(diff_content: str) -> str:
    """
    Analyze PR diff using Google Gemini and return a summary review
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")
    
    client = genai.Client(api_key=api_key)
    
    analysis_prompt = f"""You are a code reviewer. Analyze this pull request diff and provide a FIRST-LEVEL REVIEW summary.

Focus on:
1. Null/undefined checks - Any potential null pointer exceptions?
2. Logic errors - Obvious bugs or wrong logic?
3. Code style - Inconsistencies or violations?
4. Performance - Any obvious inefficiencies?
5. Security - Potential security issues?
6. Testing - Is test coverage adequate?

Keep the review CONCISE and ACTIONABLE. Group findings by category.
If no issues found in a category, skip it.

Format the response as:
- **[CATEGORY]**: List of issues or "No issues found"

---
DIFF:
{diff_content}
"""
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=analysis_prompt
    )
    return response.text

def format_github_comment(review_analysis: str) -> str:
    """
    Format the review analysis as a GitHub comment
    """
    comment = f"""## 🤖 Automated Code Review

{review_analysis}

---
*This is a first-level automated review to speed up human review. Please review the code yourself before approving.*
"""
    return comment

def main():
    # Get PR diff from stdin or environment
    if len(sys.argv) > 1:
        diff_content = sys.argv[1]
    else:
        diff_content = sys.stdin.read()
    
    if not diff_content.strip():
        print("No diff content provided")
        sys.exit(1)
    
    # Analyze the diff
    analysis = analyze_pr_diff(diff_content)
    
    # Format for GitHub
    comment = format_github_comment(analysis)
    
    # Output as JSON for GitHub Actions to use
    output = {
        "analysis": analysis,
        "comment": comment
    }
    
    print(json.dumps(output))

if __name__ == "__main__":
    main()
