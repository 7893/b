# b

Static blog powered by Hugo + Cloudflare Workers + R2

## Tech Stack

- **Static Generator**: Hugo v0.146.0 with PaperMod theme
- **Storage**: Cloudflare R2 (bucket: blog-b)
- **CDN**: Cloudflare Workers
- **URL**: https://b.53.workers.dev
- **CI/CD**: GitHub Actions

## Content

21 articles migrated from WordPress (6ki.org) with:
- Categories and tags preserved
- Original publish dates maintained
- SEO optimized metadata

## Features

- ✅ Responsive design
- ✅ Dark/Light theme
- ✅ RSS feed
- ✅ Sitemap (SEO)
- ✅ robots.txt
- ✅ Automatic deployment via GitHub Actions
- ✅ Categories and tags taxonomy
- ✅ Full-text search (Pagefind)
- ✅ Comments system (Giscus)
- ✅ CDN caching (Cloudflare Workers)
- ✅ Optimized cache headers
  - Static assets: 1 year cache
  - HTML: 1 hour cache
- ✅ Security headers

## Local Development

```bash
# Build
hugo --minify

# Preview (requires Hugo)
hugo server
```

## Deployment

Automatic deployment on push to `main` branch via GitHub Actions:
1. Build Hugo site
2. Upload to R2
3. Deploy Worker

Manual deployment:
```bash
# Upload to R2
aws s3 sync public/ s3://blog-b/ --endpoint-url $R2_ENDPOINT --delete

# Deploy Worker
wrangler deploy
```

## SEO

- Sitemap: https://b.53.workers.dev/sitemap.xml
- RSS: https://b.53.workers.dev/index.xml
- robots.txt: https://b.53.workers.dev/robots.txt
