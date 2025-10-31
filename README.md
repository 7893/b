# b

Static blog powered by Hugo + Cloudflare Workers + R2

## Tech Stack

- **Static Generator**: Hugo with PaperMod theme
- **Storage**: Cloudflare R2 (bucket: blog-b)
- **CDN**: Cloudflare Workers
- **URL**: https://b.53.workers.dev

## Content

21 articles migrated from WordPress (6ki.org)

## Build

```bash
hugo --minify
```

## Deploy

```bash
# Upload to R2
aws s3 sync public/ s3://blog-b/ --endpoint-url $R2_ENDPOINT

# Deploy Worker
wrangler deploy
```
