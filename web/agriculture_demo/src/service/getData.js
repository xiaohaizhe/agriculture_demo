import fetch from '../config/fetch'
const prodEnv = require('../../config/dev.env')
const SERVER_URL = prodEnv.LOGIN_SERVER_URL;//映射地址

//获取环境参数图表
export const getChartData = (type,id=504626770) => fetch( SERVER_URL+'/api/device/get_data_in_chart', {id,type});

//获取病虫害名称（有二级目录）
export const getIllnessData = (first_level,second_level) => fetch( SERVER_URL+'/api/diseases_or_pests/get_names', {first_level,second_level});

//获取病虫害详情（有二级目录）
export const getIllnessDetail = (first_level,second_level,name) => fetch( SERVER_URL+'/api/diseases_or_pests/get_details1', {first_level,second_level,name});

//threejs获取病虫害三级数据
export const get3Data = (second_level) => fetch( SERVER_URL+'/api/diseases_or_pests_3d/third_level', {second_level});

//threejs获取病虫害二级数据
export const get2Data = () => fetch( SERVER_URL+'/api/diseases_or_pests_3d/second_level', {});