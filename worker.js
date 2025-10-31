export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    let path = url.pathname;
    
    // 默认首页
    if (path === '/') {
      path = '/index.html';
    }
    
    // 自动添加 .html 后缀
    if (!path.includes('.') && !path.endsWith('/')) {
      path = path + '/index.html';
    } else if (path.endsWith('/')) {
      path = path + 'index.html';
    }
    
    // 检查缓存
    const cache = caches.default;
    const cacheKey = new Request(url.toString(), request);
    let response = await cache.match(cacheKey);
    
    if (response) {
      return response;
    }
    
    // 从 R2 获取文件
    const object = await env.BLOG_B.get(path.slice(1));
    
    if (!object) {
      const notFound = await env.BLOG_B.get('404.html');
      if (notFound) {
        return new Response(await notFound.text(), {
          status: 404,
          headers: { 
            'Content-Type': 'text/html; charset=utf-8',
            'Cache-Control': 'public, max-age=300'
          }
        });
      }
      return new Response('Not Found', { status: 404 });
    }
    
    // 设置响应头
    const contentType = getContentType(path);
    const headers = new Headers({
      'Content-Type': contentType,
      'Cache-Control': getCacheControl(path),
      'X-Content-Type-Options': 'nosniff',
      'X-Frame-Options': 'SAMEORIGIN',
      'Referrer-Policy': 'strict-origin-when-cross-origin'
    });
    
    response = new Response(object.body, { headers });
    
    // 缓存响应（Cloudflare 自动处理压缩）
    ctx.waitUntil(cache.put(cacheKey, response.clone()));
    
    return response;
  }
};

function getContentType(path) {
  const ext = path.split('.').pop();
  const types = {
    'html': 'text/html; charset=utf-8',
    'css': 'text/css; charset=utf-8',
    'js': 'application/javascript; charset=utf-8',
    'json': 'application/json; charset=utf-8',
    'xml': 'application/xml; charset=utf-8',
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'gif': 'image/gif',
    'svg': 'image/svg+xml',
    'ico': 'image/x-icon',
    'woff': 'font/woff',
    'woff2': 'font/woff2',
    'ttf': 'font/ttf'
  };
  return types[ext] || 'application/octet-stream';
}

function getCacheControl(path) {
  // 静态资源长缓存
  if (path.match(/\.(css|js|woff|woff2|ttf|png|jpg|jpeg|gif|svg|ico)$/)) {
    return 'public, max-age=31536000, immutable';
  }
  // HTML 短缓存
  return 'public, max-age=3600, s-maxage=3600';
}
