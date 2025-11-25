---
slug: github-cv
title: Automating a Personal CV Website with Python and Sphinx
repo: justin-napolitano/cv
githubUrl: https://github.com/justin-napolitano/cv
generatedAt: '2025-11-23T08:48:43.170899Z'
source: github-auto
summary: >-
  Explore the infrastructure and automation techniques used to build and
  maintain a personal CV website with integrated machine learning projects.
tags:
  - automation
  - sphinx
  - github-pages
  - machine-learning
  - python
  - backup
  - github pages
  - machine learning
  - data integration
  - web scraping
seoPrimaryKeyword: github cv automation
seoSecondaryKeywords:
  - personal CV website
  - build automation
  - deployment scripts
  - machine learning projects
  - data projects
seoOptimized: true
topicFamily: automation
topicFamilyConfidence: 0.95
topicFamilyNotes: >-
  The post centers on automation of build, deployment, backup, and integration
  workflows using scripts and Makefiles, which aligns closely with the
  'automation' family description and examples. Although it incorporates
  elements of documentation and machine learning, the dominant theme is about
  scripting and automating the deployment and maintenance pipeline.
kind: project
id: github-cv
---

# Technical Overview of the CV Repository

This repository encapsulates the infrastructure and source code for a personal CV website, augmented with a range of documentation and machine learning projects. It is designed with automation and modularity in mind, leveraging Python, Sphinx, and shell scripting to maintain, build, deploy, and backup the site.

## Motivation and Problem Statement

Maintaining a personal CV and associated professional documentation online requires a reliable, reproducible, and automated process. Manual updates and deployments are error-prone and inefficient. This project addresses these issues by integrating build automation, deployment scripts, and backup mechanisms into a cohesive workflow.

Additionally, the repository serves as a hub for related technical projects, including machine learning experiments using TensorFlow, and data projects involving web scraping and data integration. This consolidation facilitates centralized management and documentation.

## Project Architecture and Components

### Build and Deployment Automation

- **Makefile**: Defines build targets, primarily for cleaning and generating HTML documentation.
- **python_build.py**: A Python script that orchestrates dependency installation, build cleaning, HTML generation, git commit, and push operations via subprocess calls.
- **Shell scripts (deploy.sh, deployz.sh, doit.sh, etc.)**: Provide command-line utilities for deployment to GitHub Pages using `ghp-import` and git operations.

### Documentation

- **Sphinx Source (`source/`)**: Contains markdown and reStructuredText files structured into thematic parts such as Machine Learning, Data projects, Bibliography, and Contact.
- **Sphinx Configuration (`conf.py`)**: Configured with extensions like `ablog` for blogging, `myst_nb` for notebook support, and others to enhance documentation capabilities.

### Backup and Maintenance

- **backup_html.py**: A Python script utilizing the Dropbox SDK to upload the built HTML directory to a Dropbox folder. It requires a Dropbox access token and handles API errors such as insufficient space.

### Machine Learning Projects

- Located under `source/parts/ml-ai/tensorflow/`, these projects include TensorFlow-based models for gender recognition and Supreme Court voting behavior prediction.
- Code leverages pandas, TensorFlow, scikit-learn, and visualization libraries like seaborn and matplotlib.
- Data loading, preprocessing, and model training scripts are modularized.

### Data Projects

- Includes web scraping applications and data integration workflows.
- Scripts handle configuration loading, data cleaning, merging, and interfacing with Google Sheets and Drive APIs.

## Implementation Details

- The build pipeline in `python_build.py` runs `make clean` and `make html` commands, followed by git commit and push operations, automating the full build and deployment cycle.
- Deployment scripts use `ghp-import` to push the `build/html` directory to the `gh-pages` branch, enabling GitHub Pages hosting.
- Backup script `backup_html.py` reads the local HTML build directory and uploads it to a specified Dropbox path, ensuring offsite backup.
- The Sphinx documentation is enhanced with blogging and notebook support, allowing integration of narrative content with executable code.
- Machine learning projects are structured to load data, preprocess, split datasets, and train TensorFlow models with monitoring and logging.

## Practical Considerations

- The repository assumes a Unix-like environment for shell scripts and Makefile usage.
- Python scripts require specific versions (3.5+) and dependencies listed in requirements files.
- Dropbox integration necessitates manual insertion of an access token.
- Some scripts and files appear to be works in progress or placeholders, suggesting ongoing development.

## Summary

This repository exemplifies a pragmatic approach to managing a personal CV website and related technical documentation with automation and backup. It integrates machine learning experiments and data projects, providing a centralized platform for professional presentation and technical exploration. The structure supports extensibility and maintainability, with clear separation of concerns between build automation, deployment, backup, and content authoring.

Returning to this project, focus should be placed on refining automation scripts, expanding documentation, and modularizing machine learning components for reuse and clarity.

