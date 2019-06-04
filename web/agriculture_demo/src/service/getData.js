import fetch from '../config/fetch'
const prodEnv = require('../../config/dev.env')
const SERVER_URL = prodEnv.LOGIN_SERVER_URL;//映射地址

//获取环境参数图表
//export const getChartData = (type,id=504626770) => fetch( 'strawberry/api/device/get_data_in_chart', {id,type});
export const getChartData = (type,start,end,id=504626770) => fetch( 'strawberry/api/device/get_data_by_time', {type,start,end,id});

//获取病虫害名称（有二级目录）
export const getIllnessData = (first_level,second_level) => fetch( SERVER_URL+'/api/diseases_or_pests/get_names', {first_level,second_level});

//获取病虫害详情（有二级目录）
export const getIllnessDetail = (first_level,second_level,name) => fetch( SERVER_URL+'/api/diseases_or_pests/get_details1', {first_level,second_level,name});

//threejs获取病虫害三级数据
export const get3Data = (second_level) => fetch( SERVER_URL+'/api/diseases_or_pests_3d/third_level', {second_level});

//threejs获取病虫害二级数据
export const get2Data = () => fetch( SERVER_URL+'/api/diseases_or_pests_3d/second_level', {});

//获取病虫害新闻列表
export const getNewsList = (page,number) => fetch( SERVER_URL+'/api/plant_diseases_and_insect_pests/newsList', {page,number});

//获取所有城市温度列表
export const getWeatherList = () => fetch( SERVER_URL+'/api/weather', {});

//获取降雨量前30名城市列表
export const getPrecipitationList = () => fetch( SERVER_URL+'/api/precipitation/list', {});

//获取最新气象预告与评估
export const getAssessment = () => fetch( SERVER_URL+'/api/forecast_and_assessment/get_latest_forecast_and_assessment', {});

//获取苹果期货最新数据
export const getAppleFuturesData  = () => fetch( SERVER_URL+'/api/apple/apple_futures_data', {});

//获取地区价格行情
export const getPriceAnalyse  = () => fetch( SERVER_URL+'/api/apple/get_price_analyse', {});

//获取苹果价格详情列表
export const getPriceDetail  = (sdate,edate,page=1,number=20) => fetch( SERVER_URL+'/api/apple/get_price_detail', {sdate,edate,page,number});

//获取草莓行情新闻列表
export const getStrawberryNews  = (page=1,number=5) => fetch( SERVER_URL+'/api/strawberry_market_news/newsList', {page,number});