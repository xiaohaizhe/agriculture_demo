//mutation.js

const HANDLE_NAV = 'HANDLE_NAV'
const HANDLE_VG = 'HANDLE_VG'

export default{
    [HANDLE_NAV](state,value){
        state.nav = value;
        console.log(value);
    },
    [HANDLE_VG](state,value){
        state.vegetable = value;
        console.log(value);
    }
}