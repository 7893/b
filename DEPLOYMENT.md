# WordPress to Hugo Migration with Cloudflare Deployment

This project migrates a WordPress site to Hugo static site generator and sets up automated deployment to both GitHub Pages and Cloudflare Pages.

## Project Structure

```
├── .github/workflows/deploy.yml    # GitHub Actions workflow
├── WordPress.2025-10-31.xml        # Original WordPress export
├── content/posts/                  # Converted Hugo content
├── hugo.toml                       # Hugo configuration
├── parse_wordpress_fixed.py        # WordPress to Hugo converter
├── public/                         # Build output directory
├── wrangler.toml                   # Wrangler configuration for Cloudflare
├── package.json                    # Node.js dependencies
└── README.md                       # Project documentation
```

## Deployment Process

1. **Content Migration**: WordPress XML is parsed and converted to Hugo-compatible Markdown with proper frontmatter
2. **Build Process**: Hugo generates static site from content and theme
3. **Deployment**: GitHub Actions deploys to both GitHub Pages and Cloudflare Pages

## Required Secrets

To deploy to Cloudflare Pages, add these secrets to your GitHub repository:

- `CLOUDFLARE_API_TOKEN`: Your Cloudflare API token with Pages permissions
- `CLOUDFLARE_ACCOUNT_ID`: Your Cloudflare Account ID

## Local Development

To run locally:

```bash
# Install Hugo (if not already installed)
# On Ubuntu/Debian:
# sudo snap install hugo

# Build the site
hugo

# Serve locally with hot reload
hugo server -D
```

## WordPress XML Converter

The `parse_wordpress_fixed.py` script handles the conversion from WordPress XML to Hugo format:
- Preserves all content including HTML to Markdown conversion
- Maintains proper categories and tags
- Formats dates correctly for Hugo
- Creates proper frontmatter with title, date, draft status, etc.

## Troubleshooting

If the GitHub Action fails:
1. Check that all secrets are properly set
2. Verify the Cloudflare project name in `deploy.yml` matches your Cloudflare Pages project
3. Ensure the `baseURL` in `hugo.toml` is correct for your deployment target