<template>
    <div class="height100">
        <el-container class="bgColor" :class="{bg :$route.meta.routeFlag,}">
            <el-aside width="15%" class="height100">
               <el-col :span="24" class="bg-nav height100">
                   <div class="hiynn"></div>
                  <el-menu router 
                    :default-active="routerName"
                    class="el-menu-vertical-demo"
                    >
                    <el-menu-item index="cropManage" :route="{name:'cropManage'}">
                      <i class="weed nav-icon"></i>
                      <span slot="title">作物管理</span>
                    </el-menu-item>
                    <el-menu-item index="infoBank" :route="{name:'ordinary'}">
                      <i class="info nav-icon"></i>
                      <span slot="title">病虫害信息库</span>
                    </el-menu-item>
                    <el-menu-item index="weather" :route="{name:'weather'}">
                      <i class="weather nav-icon"></i>
                      <span slot="title">天气信息</span>
                    </el-menu-item>
                    <el-menu-item index="predict" :route="{name:'price'}">
                      <i class="predict nav-icon"></i>
                      <span slot="title">行情与预测</span>
                    </el-menu-item>
                  </el-menu>
              </el-col>
            </el-aside>
            <el-container class="ad-right">
                <el-header :class="{clear:!$route.meta.routeFlag}">
                  <ad-header ></ad-header>
                </el-header>
                <el-main id="el-main">
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<script>
  import adHeader from 'components/header/header'
  export default {
    name: 'index',
    data () {
      return {
        routerName:this.$route.path.split('/')[2]
      }
    },
    computed:{
    },
    mounted(){
      // debugger;
      // let a = this.$route;
    },
    components:{
        'ad-header':adHeader
    },
    methods: {

    }

  }
</script>

<style>
</style>
