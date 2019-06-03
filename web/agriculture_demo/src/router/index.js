import Vue from 'vue'
import Router from 'vue-router'
const index = r => require.ensure([], () => r(require('../page/index/index')), 'index')
const cropManage = r => require.ensure([], () => r(require('../page/cropManage/cropManage')), 'cropManage')
const infoBank = r => require.ensure([], () => r(require('../page/infoBank/infoBank')), 'infoBank')
const weather = r => require.ensure([], () => r(require('../page/weather/weather')), 'weather')
const predict = r => require.ensure([], () => r(require('../page/predict/predict')), 'predict')
const greenhouse = r => require.ensure([], () => r(require('../page/greenhouse/greenhouse')), 'greenhouse')
const envParam = r => require.ensure([], () => r(require('../page/envParam/envParam')), 'envParam')
const plantLog = r => require.ensure([], () => r(require('../page/plantLog/plantLog')), 'plantLog')
const knowledgeBase = r => require.ensure([], () => r(require('../page/infoBank/children/base')), 'knowledgeBase')
const ordinary = r => require.ensure([], () => r(require('../page/infoBank/children/ordinary')), 'ordinary')
const illDetail = r => require.ensure([], () => r(require('../page/infoBank/children/illDetail')), 'illDetail')
const price = r => require.ensure([], () => r(require('../page/predict/children/price')), 'price')
const forecast = r => require.ensure([], () => r(require('../page/predict/children/forecast')), 'forecast')
const supply = r => require.ensure([], () => r(require('../page/predict/children/supply')), 'supply')

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
          redirect: '/index/cropManage'
        },{
          path: "/index/cropManage",
          name:"cropManage",
          component: cropManage,
          meta:{routeFlag:true}
        },{
          path: "/index/infoBank",
          name:"infoBank",
          component: infoBank,
          meta:{routeFlag:false},
          children:[{
            path: '',
            redirect: '/index/infoBank/ordinary'
          },{
            path: "/index/infoBank/knowledgeBase",
            name:"knowledgeBase",
            component: knowledgeBase
          },{
            path: "/index/infoBank/ordinary",
            name:"ordinary",
            component: ordinary
          },{
            path: "/index/infoBank/illDetail/:data",
            name:"illDetail",
            component: illDetail
          }]
        },{
          path: "/index/weather",
          name:"weather",
          component: weather,
          meta:{routeFlag:false} 
        },{
          path: "/index/predict",
          name:"predict",
          component: predict,
          meta:{routeFlag:false},
          children:[{
            path: "",
            redirect: '/index/predict/price'
          },{
            path: "/index/predict/price",
            name:"price",
            component: price
          },{
            path: "/index/predict/supply",
            name:"supply",
            component: supply
          },{
            path: "/index/predict/forecast",
            name:"forecast",
            component: forecast
          }]
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
        },{
          path: "/index/cropManage/plantLog",
          name:"plantLog",
          component: plantLog,
          meta:{routeFlag:false} 
        }
      ]
    }
  ]
})
