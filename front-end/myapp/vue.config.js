const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  lintOnSave: false,
  devServer:{
    port:8999,
    open:true,
    proxy: {
      '/api': {
        target: 'https://api.deepinfra.com/v1/openai/chat/completions',  // 目标API地址
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      },
    },
  }
}
