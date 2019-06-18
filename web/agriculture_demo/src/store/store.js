import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import getters from './getters'
import actions from './actions'

Vue.use(Vuex);
const state = {
	vegetable:{
		name:'苹果',
		id:'apple'
	},
	nav:'cropManage'
	// type:'price'
}

export default new Vuex.Store({
    state,
	getters,
	actions,
	mutations,
});