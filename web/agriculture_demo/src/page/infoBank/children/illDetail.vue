<template>
  <div ref="illDetail">
    
  </div>
</template>

<script>
  import {getIllnessDetail} from 'service/getData'
  export default {
    name: 'illDetail',
    data () {
      return {
        illness:''
      }
    },
    mounted(){
      this.illness = this.$route.params.data;
      this.getIllnessDetail();
    },
    methods:{
      async getIllnessDetail(){
        let resp = await getIllnessDetail('薯类','马铃薯',this.illness);
        if(resp.code==0){
          this.$refs.illDetail.innerHTML=resp.data;
        }
      }
    }
  }
</script>