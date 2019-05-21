import Vue from 'vue'
import Router from 'vue-router'
const index = r => require.ensure([], () => r(require('../page/index/index')), 'index')
const cropManage = r => require.ensure([], () => r(require('../page/cropManage/cropManage')), 'cropManage')
const infoBank = r => require.ensure([], () => r(require('../page/infoBank/infoBank')), 'infoBank')
const weather = r => require.ensure([], () => r(require('../page/weather/weather')), 'weather')
const predict = r => require.ensure([], () => r(require('../page/predict/predict')), 'predict')

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/index/',
      component: index,
      children:[{
          path: "",
          name:"cropManage",
          component: cropManage, 
          meta:{routeFlag:true} 
        },{
          path: "cropManage",
          name:"cropManage",
          component: cropManage,
          meta:{routeFlag:true} 
        },{
          path: "infoBank",
          name:"infoBank",
          component: infoBank,
          meta:{routeFlag:false} 
        },{
          path: "weather",
          name:"weather",
          component: weather,
          meta:{routeFlag:false} 
        },{
          path: "predict",
          name:"predict",
          component: predict,
          meta:{routeFlag:false} 
        }
      ]
    }
  ]
})
