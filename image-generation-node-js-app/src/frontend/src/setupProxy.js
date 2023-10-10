
const { createProxyMiddleware } = require('http-proxy-middleware');
const proxy = {
  target: 'https://q45f9ormi0.execute-api.us-east-1.amazonaws.com/',
  changeOrigin: true,
};
module.exports = function (app) {
  app.use('/test', createProxyMiddleware(proxy));
};