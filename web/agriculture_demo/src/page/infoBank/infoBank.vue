<template>
   <el-row :gutter="30" class="height100">
     <el-col :span="16" class="height100">
       <el-container class="sub-ad bg-fff">
              <el-header height="130px">
                  <el-breadcrumb separator-class="el-icon-arrow-right">
                      <el-breadcrumb-item :to="{ name: 'ordinary' }">病虫害信息库</el-breadcrumb-item>
                      <el-breadcrumb-item :to="{ name : pramas[paramActive].id}">{{pramas[paramActive].name}}</el-breadcrumb-item>
                      <el-breadcrumb-item v-if="routeMatch.name=='illDetail'">{{routeMatch.params.data ||routeMatch}}</el-breadcrumb-item>
                  </el-breadcrumb>
                  <el-divider></el-divider>
                  <el-row>
                      <el-col :span="8">
                          <ul class="ad-flex ad-flexBtw mg-top-10">
                              <li v-for="(item,index) in pramas" :key="item.id" class="paramLi" @click="pramaChange(index)">
                                  <i class="paramActive mg-right-10" :style="{'background-color':paramActive==item.index?'#FBB02F':'#fff'}"></i>{{item.name}}</li>
                          </ul>
                      </el-col>
                  </el-row>
              </el-header>
              <el-main>
                  <router-view @updateRoute="updateRoute"></router-view>
              </el-main>
        </el-container>
     </el-col>
     <el-col :span="8">
       <div class="bg-fff">
         <div><i class="news"></i></div>
       </div>
     </el-col>
   </el-row>
 
</template>

<script>
export default {
  name: 'infoBank',
  data () {
    return {
      routeMatch:{},
      paramActive:0,
      pramas:[{
            name:'马铃薯常见病虫害',
            id:'ordinary',
            index:0
        },{
            name:'病虫害数据库',
            id:'base',
            index:1
        }]
    }
  },
  mounted(){
    this.routeMatch = this.$route;
  },
  methods:{
    pramaChange(index){
      this.paramActive = index;
      this.routeMatch = {};
      this.$router.push({name:this.pramas[index].id});
    },
    updateRoute(val){
      this.routeMatch = val;
    }
  }
}
</script>
<style>

</style>

