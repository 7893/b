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
    
    // 从 R2 获取文件
    const object = await env.BLOG_B.get(path.slice(1));
    
    if (!object) {
      const notFound = await env.BLOG_B.get('404.html');
      if (notFound) {
        return new Response(await notFound.text(), {
          status: 404,
          headers: { 
            'Content-Type': 'text/html; charset=utf-8',
            'Cache-Control': 'no-store, no-cache, must-revalidate'
          }
        });
      }
      return new Response('Not Found', { status: 404 });
    }
    
    // 设置响应头 - 禁用所有缓存
    const contentType = getContentType(path);
    const headers = new Headers({
      'Content-Type': contentType,
      'Cache-Control': 'no-store, no-cache, must-revalidate',
      'Pragma': 'no-cache',
      'Expires': '0',
      'X-Content-Type-Options': 'nosniff',
      'X-Frame-Options': 'SAMEORIGIN',
      'Referrer-Policy': 'strict-origin-when-cross-origin'
    });
    
    return new Response(object.body, { headers });
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
