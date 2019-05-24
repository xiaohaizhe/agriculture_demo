import Vue from 'vue'
import Router from 'vue-router'
const index = r => require.ensure([], () => r(require('../page/index/index')), 'index')
const cropManage = r => require.ensure([], () => r(require('../page/cropManage/cropManage')), 'cropManage')
const infoBank = r => require.ensure([], () => r(require('../page/infoBank/infoBank')), 'infoBank')
const weather = r => require.ensure([], () => r(require('../page/weather/weather')), 'weather')
const predict = r => require.ensure([], () => r(require('../page/predict/predict')), 'predict')
const greenhouse = r => require.ensure([], () => r(require('../page/greenhouse/greenhouse')), 'greenhouse')
const envParam = r => require.ensure([], () => r(require('../page/envParam/envParam')), 'envParam')

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/index/cropManage'
    },
    {
      path: '/index',
      component: index,
      children:[{
          path: "",
          component: cropManage, 
          meta:{routeFlag:true}
        },{
          path: "/index/cropManage",
          name:"cropManage",
          component: cropManage,
          meta:{routeFlag:true}
        },{
          path: "/index/infoBank",
          name:"infoBank",
          component: infoBank,
          meta:{routeFlag:false} 
        },{
          path: "/index/weather",
          name:"weather",
          component: weather,
          meta:{routeFlag:false} 
        },{
          path: "/index/predict",
          name:"predict",
          component: predict,
          meta:{routeFlag:false} 
        },{
          path: "/index/cropManage/greenhouse",
          name:"greenhouse",
          component: greenhouse,
          meta:{routeFlag:false} 
        },{
          path: "/index/cropManage/envParam",
          name:"envParam",
          component: envParam,
          meta:{routeFlag:false} 
        }
      ]
    }
  ]
})
