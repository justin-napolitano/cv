---
slug: github-cv-note-technical-overview
id: github-cv-note-technical-overview
title: CV Repository Overview
repo: justin-napolitano/cv
githubUrl: https://github.com/justin-napolitano/cv
generatedAt: '2025-11-24T18:34:24.135Z'
source: github-auto
summary: >-
  This repo is my personal CV website, hosted at
  [cv.jnapolitano.io](https://cv.jnapolitano.io). It's built with HTML and
  Sphinx, plus I’ve added automation with scripts for deployment and backup.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repo is my personal CV website, hosted at [cv.jnapolitano.io](https://cv.jnapolitano.io). It's built with HTML and Sphinx, plus I’ve added automation with scripts for deployment and backup.

### Key Components:
- **HTML** for the CV site
- **Sphinx** for documentation, including blog posts and ML projects
- **Python 3.5+** for build automation
- **Dropbox SDK** for backup support

### Quick Start:
1. Clone the repo:
   ```bash
   git clone https://github.com/justin-napolitano/cv.git
   cd cv
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Build the HTML:
   ```bash
   make html
   ```
4. Deploy to GitHub Pages:
   ```bash
   ./deploy.sh
   ```

### Important Notes:
- Set up your Dropbox token in `backup_html.py` for backup features.
- Some scripts lack clear documentation; read filenames carefully.
