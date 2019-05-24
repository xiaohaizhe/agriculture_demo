// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { Button, Select,Option,Container,Header,Aside,Main,Col,Menu,Submenu,MenuItem,MenuItemGroup,Input,Breadcrumb,BreadcrumbItem,Divider,Form,FormItem,Table,
  TableColumn, Pagination,Row,Progress ,MessageBox,Popover,DatePicker } from 'element-ui';
import './style/main.css'
import store from './store/store'

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

Vue.prototype.$confirm = MessageBox.confirm;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
