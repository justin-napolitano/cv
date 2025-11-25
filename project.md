---
slug: github-cv
id: github-cv
title: Automated CV Website with Sphinx and Dropbox Backup
repo: justin-napolitano/cv
githubUrl: https://github.com/justin-napolitano/cv
generatedAt: '2025-11-24T21:34:25.895Z'
source: github-auto
summary: >-
  Explore the setup and features of a personal CV website using HTML, Sphinx,
  and automated deployment scripts.
tags:
  - sphinx
  - html
  - python
  - dropbox
  - makefile
  - tensorflow
  - bash
  - documentation
  - github pages
seoPrimaryKeyword: automated cv website
seoSecondaryKeywords:
  - sphinx documentation
  - html cv generator
  - python build automation
  - dropbox backup integration
  - tensorflow projects
seoOptimized: true
topicFamily: null
topicFamilyConfidence: null
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

This repository contains the source and build files for my personal CV website hosted at [cv.jnapolitano.io](https://cv.jnapolitano.io). It is built primarily using HTML and Sphinx documentation tools, with automated deployment and backup scripts.

## Features

- Static HTML generation of personal CV and related documentation
- Automated build and deployment scripts using Makefile and shell scripts
- Dropbox backup integration for HTML builds
- Sphinx-based documentation with support for blog posts, machine learning projects, and data projects
- TensorFlow machine learning projects integrated as submodules

## Tech Stack

- HTML for the CV website
- Python 3.5+ for build automation and Dropbox API integration
- Sphinx documentation generator with extensions such as ablog, myst_nb, sphinx_copybutton
- TensorFlow for machine learning projects
- Bash shell scripts for deployment and maintenance

## Getting Started

### Prerequisites

- Python 3.5 or higher
- pip package manager
- Dropbox SDK for Python (`pip install dropbox`)
- GitHub CLI for deployment (`ghp-import` tool)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/justin-napolitano/cv.git
cd cv
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Setup Dropbox access token in `backup_html.py` for backup functionality.

### Build and Deploy

- To build the HTML documentation:

```bash
make html
```

- To deploy the built HTML to GitHub Pages:

```bash
./deploy.sh
```

- To backup the HTML build to Dropbox:

```bash
python backup_html.py
```

## Project Structure

```
cv/
├── acp.sh                  # Shell script (purpose unspecified)
├── backup_html.py          # Python script to backup HTML build to Dropbox
├── chtml.sh                # Shell script (purpose unspecified)
├── deploy.sh               # Deployment script to GitHub Pages
├── deployz.sh              # Alternative deployment script
├── doit.sh                 # Shell script (purpose unspecified)
├── install.sh              # Installation script
├── label_list.py           # Python script for reading Sphinx pickle labels
├── latex/                  # LaTeX source files
├── Makefile                # Build automation file
├── pullit.sh               # Git pull script
├── pushit.sh               # Git push script
├── python_build.py         # Python build automation script
├── requirements.txt        # Python dependencies
├── requirements_rocky.txt  # Alternative dependencies
├── requirments.txt         # Possibly duplicate requirements file
├── source/                 # Sphinx documentation source
│   ├── _toc.yml            # Table of contents
│   ├── conf.py             # Sphinx configuration
│   ├── index.md            # Main documentation index
│   ├── parts/              # Documentation parts (ml-ai, data, bibliography, etc.)
│   └── ...
└── uninstall.sh            # Uninstall script
```

## Future Work / Roadmap

- Clean up and consolidate shell scripts for clarity and purpose
- Improve configuration management and environment variable handling
- Enhance documentation structure and add more detailed usage guides
- Expand Dropbox backup functionality with error handling and logging
- Modularize machine learning projects for easier reuse
- Automate testing and continuous integration for builds and deployments

---

*Note: Some scripts and files are present without explicit documentation. Assumptions were made based on filenames and partial code snippets.*
