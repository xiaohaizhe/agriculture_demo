//mutation.js

// const HANDLE_TYPE = 'HANDLE_TYPE'
const HANDLE_VG = 'HANDLE_VG'

export default{
    // [HANDLE_TYPE](state,value){
    //     state.type = value;
    // },
    [HANDLE_VG](state,value){
        state.vegetable = value;
        console.log(value);
    }
}