<template>
    <div class="height100">
        <el-container class="bgColor" :class="{bg :$route.meta.routeFlag}">
            <el-aside width="15%" class="height100">
               <el-col :span="24" class="bg-nav height100">
                   <!-- <div class="hiynn"></div> -->
                   <div class="hiynn">耘农大脑</div>
                  <el-menu router 
                    :default-active="nav"
                    class="el-menu-vertical-demo"
                    active-text-color="#fff"
                    @select="selectNav"
                    >
                    <el-menu-item index="cropManage" :route="{name:'cropManage'}">
                      <i class="weed nav-icon"></i>
                      <span slot="title">数字化种植</span>
                    </el-menu-item>
                    <el-menu-item index="infoBank" :route="{name:'knowledgeBase'}">
                      <i class="info nav-icon"></i>
                      <span slot="title">病虫害知识图谱</span>
                    </el-menu-item>
                    <el-menu-item index="weather" :route="{name:'weather'}">
                      <i class="weather nav-icon"></i>
                      <span slot="title">智慧农情</span>
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
  import {mapState } from 'vuex'

  export default {
    name: 'index',
    data () {
      return {
        // routerName:this.$route.path.split('/')[2]
      }
    },
    computed:{
        ...mapState([
            'nav'
        ])
    },
    watch:{
      routerName(cur,old){
        
      }
    },
    mounted(){
    },
    components:{
        'ad-header':adHeader
    },
    methods: {
        selectNav( index, indexPath){
          this.$store.commit('HANDLE_NAV',index);
        }
    }

  }
</script>

<style>
</style>
