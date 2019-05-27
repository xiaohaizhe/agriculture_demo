import fetch from '../config/fetch'
const prodEnv = require('../../config/dev.env')
const SERVER_URL = prodEnv.LOGIN_SERVER_URL;//映射地址

//获取环境参数图表
export const getChartData = (type,id=504626770) => fetch( SERVER_URL+'/api/device/get_data_in_chart', {id,type});