export default {
  async fetch(request, env) {
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
          headers: { 'Content-Type': 'text/html; charset=utf-8' }
        });
      }
      return new Response('Not Found', { status: 404 });
    }
    
    // 设置正确的 Content-Type
    const contentType = getContentType(path);
    
    return new Response(object.body, {
      headers: {
        'Content-Type': contentType,
        'Cache-Control': 'public, max-age=3600'
      }
    });
  }
};

function getContentType(path) {
  const ext = path.split('.').pop();
  const types = {
    'html': 'text/html; charset=utf-8',
    'css': 'text/css',
    'js': 'application/javascript',
    'json': 'application/json',
    'xml': 'application/xml',
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
