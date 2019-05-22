import fetch from '../config/fetch'
// const prodEnv = require('../../config/dev.env')
// const SERVER_URL = prodEnv.LOGIN_SERVER_URL;//映射地址

//普通用户登录
export const getUser = (name,password) => fetch(  '/api/user/login', {
    name: name,
    password: password
});