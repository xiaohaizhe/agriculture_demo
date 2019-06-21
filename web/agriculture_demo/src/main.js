// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import 'babel-polyfill'
import { Button, Select,Option,Container,Header,Aside,Main,Col,Menu,Submenu,MenuItem,MenuItemGroup,Input,Breadcrumb,BreadcrumbItem,Divider,Form,FormItem,Table,
  TableColumn, Pagination,Row,Progress ,MessageBox,Popover,DatePicker,Message,Carousel,CarouselItem,Icon} from 'element-ui';
import './style/main.css'
import store from './store/store'
import echarts from 'echarts' //引入echarts
Vue.prototype.$echarts = echarts //引入组件

Vue.config.productionTip = false
Vue.use(Button);
Vue.use(Select);
Vue.use(Option);
Vue.use(Container);
Vue.use(Header);
Vue.use(Aside);
Vue.use(Main);
Vue.use(Col);
Vue.use(Menu);
Vue.use(Submenu);
Vue.use(MenuItem);
Vue.use(MenuItemGroup);
Vue.use(Input);
Vue.use(Breadcrumb);
Vue.use(BreadcrumbItem);
Vue.use(Divider);
Vue.use(Form);
Vue.use(FormItem);
Vue.use(Table);
Vue.use(TableColumn);
Vue.use(Pagination);
Vue.use(Row);
Vue.use(Progress);
Vue.use(Popover);
Vue.use(DatePicker);
Vue.use(Carousel);
Vue.use(CarouselItem);
Vue.use(Icon);
Vue.prototype.$alert = MessageBox.alert;
Vue.prototype.$confirm = MessageBox.confirm;
Vue.prototype.$message = Message;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
