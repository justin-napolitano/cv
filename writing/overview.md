---
slug: github-cv-writing-overview
id: github-cv-writing-overview
title: 'My CV Repository: Building a Personal Website'
repo: justin-napolitano/cv
githubUrl: https://github.com/justin-napolitano/cv
generatedAt: '2025-11-24T17:15:44.246Z'
source: github-auto
summary: >-
  I’ve put together a personal CV website that I host at
  [cv.jnapolitano.io](https://cv.jnapolitano.io). This GitHub repository
  contains everything you need to know about it, including the source code,
  build files, and deployment scripts. Whether you're looking to create your own
  CV site or just curious about my process, I hope you find this breakdown
  useful.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: writing
entryLayout: writing
showInProjects: false
showInNotes: false
showInWriting: true
showInLogs: false
---

I’ve put together a personal CV website that I host at [cv.jnapolitano.io](https://cv.jnapolitano.io). This GitHub repository contains everything you need to know about it, including the source code, build files, and deployment scripts. Whether you're looking to create your own CV site or just curious about my process, I hope you find this breakdown useful.

## Why This Exists

I needed a straightforward way to present my CV and some related projects online. There are tons of portfolio generators out there, but I wanted more control over the design and deployment. Plus, I like to tinker with technologies and tools, so it was the perfect project to flex those muscles. 

The result? A static HTML site that auto-generates from a structure based on Sphinx documentation tools. I also wanted some automated processes for deployment and backups so I could focus on the content.

## Key Design Decisions

### The Static Approach

I chose static HTML for a few reasons:

- **Simplicity**: Static sites are fast and easy to host.
- **Control**: I can customize everything without needing to rely on a CMS or third-party services.
- **Performance**: Static sites load faster and are easy on resources.

The choice of Sphinx was another key decision. It offers an elegantly structured way to create documentation, and it easily integrates with a variety of projects. It also allows for clear separation of content, making it easier to maintain.

### Automation with Scripts

To streamline the build and deployment process, I incorporated some shell scripts and a Makefile:

- **Automated Builds**: I use a Makefile to manage the build process, which keeps everything organized.
- **Deployment Scripts**: Shell scripts automate deploying to GitHub Pages and backing up the HTML to Dropbox.
- **Backup Integration**: This ensures that my work is safe without additional manual steps.

## Tech Stack

This project employs a handful of technologies, which I’ve found to work well together:

- **HTML**: For the website layout and content.
- **Python 3.5+**: Handles automation and Dropbox integration.
- **Sphinx**: The backbone of my documentation.
- **Bash**: For all my script needs.
- **TensorFlow**: I integrated some ML projects for good measure.

It’s worth noting that I went a bit heavy on the scripts. I have shell scripts for different purposes, which sometimes leads to confusion. But I’ll get to that in the future improvements section.

## Getting Started

### Prerequisites

If you want to fork and build this yourself, you’ll need a few things set up:

- Python 3.5 or higher
- pip for package management
- Dropbox SDK for Python (`pip install dropbox`)
- GitHub CLI for deployment (`ghp-import`)

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/justin-napolitano/cv.git
   cd cv
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Add your Dropbox access token in `backup_html.py`.

### Building and Deployment

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

The repo structure is straightforward. Here’s a snapshot:

```
cv/
├── deploy.sh               # Deployment script to GitHub Pages
├── backup_html.py          # Python script for Dropbox backup
├── Makefile                # Build automation file
├── source/                 # Sphinx documentation source
│   ├── conf.py             # Sphinx configuration
│   ├── index.md            # Main index file
│   └── ...
└── ...
```

I have lots of scripts, which means there’s a bit of redundancy. Some scripts, like `doit.sh`, `pullit.sh`, and `pushit.sh`, are there but could use some explanation. I had my reasons, but I could definitely trim down and clarify the utility of each script.

## Trade-offs

With any project, there are trade-offs. Choosing a static site means I get speed and simplicity, but I also sacrifice some dynamic features, which might limit interactive elements or complex functionalities.

Script heavy? Absolutely. While automation is fantastic, managing multiple scripts can lead to chaos. Over time, I want to refactor or clean up this aspect for better clarity.

## Future Work / Roadmap

I’ve got a few ideas for improvements:

- **Script Cleanup**: Consolidate and clarify the purpose of my shell scripts.
- **Configuration Management**: Better handling for environment variables and settings.
- **Improved Documentation**: More detailed usage guides would help.
- **Modular ML Projects**: Make my ML projects more reusable.

I’m also considering automated testing for builds and continuous integration to catch issues early on. But hey, one step at a time.

## Stay Updated

If you're interested in following my progress or future updates, I'm pretty active on social media. I'm sharing updates on Mastodon, Bluesky, and Twitter/X, so feel free to connect with me there!

In summary, this CV repository was a personal project that has turned out to be practical for sharing my work. I'm looking forward to enhancing it further, making it leaner and smarter. Hope you find it useful!
