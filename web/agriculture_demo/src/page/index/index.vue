<template>
    <div class="height100">
        <el-container :class="{bg :$route.meta.routeFlag}">
            <el-aside width="15%" class="height100">
               <el-col :span="24" class="bg-nav height100">
                   <div class="hiynn"></div>
                  <el-menu router 
                    :default-active="$route.name"
                    class="el-menu-vertical-demo"
                    >
                    <el-menu-item index="cropManage" :route="{name:'cropManage'}">
                      <i class="weed ad-icon"></i>
                      <span slot="title">作物管理</span>
                    </el-menu-item>
                    <el-menu-item index="infoBank" :route="{name:'infoBank'}">
                      <i class="info ad-icon"></i>
                      <span slot="title">病虫害信息库</span>
                    </el-menu-item>
                    <el-menu-item index="weather" :route="{name:'weather'}">
                      <i class="weather ad-icon"></i>
                      <span slot="title">天气信息</span>
                    </el-menu-item>
                    <el-menu-item index="predict" :route="{name:'predict'}">
                      <i class="predict ad-icon"></i>
                      <span slot="title">行情与预测</span>
                    </el-menu-item>
                  </el-menu>
              </el-col>
            </el-aside>
            <el-container class="ad-right">
                <el-header :class="{clear:!$route.meta.routeFlag}">
                  <ad-header ></ad-header>
                </el-header>
                <el-main class="bg-fff">
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
      }
    },
    computed:{
    },
    mounted(){
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
