<template>
  <div class="adHeader">
       <div class="ad-flex ad-flexEnd">
           <!-- <el-input placeholder="搜索" prefix-icon="el-icon-search" v-model="search" style="width:290px"></el-input> -->
           <div class="subhead ad-flex ad-flexCenter">
               <i class="msg"></i>
               <i class="config"></i>
               <i class="wechat"></i>
               <i class="headIcon"></i>
               <span class="ad-white">农场主test</span>
           </div>
       </div>
  </div>
</template>

<script>
  export default {
    name: 'adHeader',
    data () {
      return {
          search:''
      }
    }
  }
</script>
