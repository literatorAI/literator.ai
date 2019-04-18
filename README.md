# This is the web project of [literator.ai](http://literator.ai)

[literator.ai](http://literator.ai) is a website which AI create some literatures.

Let's start with [couplet](http://literator.ai/#/couplet)!

this Project is created from [flask-vuejs-template](https://github.com/gtalarico/flask-vuejs-template)

The [couplet](http://literator.ai/#/couplet) model is trained by [seq2seq-couplet](https://github.com/wb14123/seq2seq-couplet) by now.

Poem creation will be added to this project shortly.

# install and run
## config
Add config.js or remove 'vue-ba'
Add `config.js` file in `src`,which contains following code 
```
var baiduKey = 'xxx'
export default {
  baiduKey: baiduKey
}
```
replace `xxx` with your own code, which can be applied in [百度统计](http://tongji.baidu.com)

## yarn install
```
yarn install
```

## get model
put model and vocab in `data` dir
