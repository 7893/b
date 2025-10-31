#!/bin/bash
# Deployment script for WordPress to Hugo migration

echo "Starting Hugo site build process..."

# Build the site
hugo --minify

if [ $? -eq 0 ]; then
    echo "✓ Site built successfully!"
    echo "Output directory: public/"
    echo ""
    echo "To deploy manually to Cloudflare Pages:"
    echo "1. Ensure you have wrangler installed: npm install -g wrangler"
    echo "2. Run: cd public && wrangler pages deploy --project-name=b"
    echo ""
    echo "The GitHub Actions workflow will automatically deploy on pushes to main branch."
else
    echo "✗ Build failed!"
    exit 1
fi