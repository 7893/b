# WordPress to Hugo Migration

This repository contains the migration of a WordPress site to Hugo static site generator. The original content was exported from WordPress in XML format and converted to Hugo-compatible Markdown files.

## Structure

- `content/posts/` - Contains all blog posts converted from WordPress
- `.github/workflows/deploy.yml` - GitHub Actions workflow for automated deployment
- `hugo.toml` - Hugo configuration file
- `parse_wordpress.py` - Python script to convert WordPress XML to Hugo format

## Deployment

The site is automatically deployed to:
- GitHub Pages
- Cloudflare Pages

## Secrets Required

For the GitHub Actions to work, the following secrets need to be configured in the repository:
- `CLOUDFLARE_API_TOKEN` - Cloudflare API token for deployment
- `CLOUDFLARE_ACCOUNT_ID` - Cloudflare account ID