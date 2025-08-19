# Lab Website README

---

## Overview

This repository hosts the UBD internship laboratory website, built with Jekyll to provide a fast, maintainable, and data-driven static site. It presents lab details, team members, publications, and project highlights in a responsive, accessible layout. The site leverages Sass for modular styling and YAML data files for content management.

---

## Table of Contents

1. Installation  
2. Usage  
3. Directory Structure  
4. Configuration  
5. Deployment  
6. Contributing  

---

## Installation

To run the site locally, you need Ruby, Bundler, and Jekyll

1. Clone the repository  
2. Install Ruby dependencies:  
   ```bash
   bundle install
   ```  

---

## Usage

After dependencies are installed, start the development server:

```bash
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`. Changes to Markdown, Sass, or templates trigger an automatic rebuild.

---

## Directory Structure

- `_config.yml` — Global configuration for Jekyll (site title, plugins, permalink styles).  
- `Gemfile` & `Gemfile.lock` — Ruby gems and locked versions for Jekyll and plugins.  
- `.gitignore` — Specifies files and directories to ignore in version control.  
- `index.html` — Homepage, uses front matter to select the home layout and include dynamic sections.  

---

### `_data`

Holds YAML files defining structured content:

- `team.yml` — Lists lab members, roles, and profiles.  
- `publications.yml` — Defines publication entries for carousels or lists.  

Add new `.yml` files here to make content available in Liquid loops.

---

### `_includes`

Reusable partials for page components:

- `header.html` — Site navigation and logo.  
- `footer.html` — Contact info and social links.   

Include these with `{% include header.html %}` in layouts or pages.

---

### `_layouts`

Page templates controlling HTML structure:

- `default.html` — Base shell with head, scripts, and footer includes.   

Layouts render front matter variables and include sections.

---

### `_sass`

Modular SCSS partials to build the main stylesheet: 

The central `main.scss` imports these in order.

---

### `assets`

Static files served directly:

- `images/` — Photo assets for team bios, project snapshots.  
- `js/` — Optional JavaScript modules for interactivity (carousels, modals).  
- `css/` — Compiled CSS output (or source map).  

Organize additional asset types as needed.

---

## Configuration

Edit `_config.yml` to adjust site-wide settings:

- `title`, `description`, `url`  
- `permalink` structure  
- Plugin list (e.g., `jekyll-feed`, `jekyll-seo-tag`)  

Front matter options in pages and posts override these defaults.

---

## Deployment

This site is configured for GitHub Pages on the `gh-pages` branch. To deploy:

1. Push changes to `gh-pages`.  
2. GitHub automatically builds and publishes to `https://<username>.github.io/lab_website`.  

For custom domains, update `CNAME` and `url` in `_config.yml`.

---

## Contributing

Contributions are welcome via pull requests. Please follow these guidelines:

- Fork the repo and create a feature branch.  
- Write clear commit messages and document changes in this README.  
- Ensure SCSS compiles without errors and the local site builds successfully.  
- Run a link checker or HTML validator before submitting.  

---
