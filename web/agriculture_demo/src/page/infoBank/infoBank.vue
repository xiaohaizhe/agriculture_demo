<template>
   <el-row :gutter="30" class="height100">
     <el-col :span="16" class="height100">
       <el-container class="sub-ad bg-fff">
              <el-header height="130px">
                  <el-breadcrumb separator-class="el-icon-arrow-right">
                      <el-breadcrumb-item :to="{ name : pramas[paramActive].routeId}">病虫害信息库</el-breadcrumb-item>
                      <el-breadcrumb-item :to="{ name : pramas[paramActive].routeId}">{{pramas[paramActive].name}}</el-breadcrumb-item>
                      <el-breadcrumb-item v-if="routeMatch.name=='illDetail'">{{routeMatch.params.data ||routeMatch}}</el-breadcrumb-item>
                  </el-breadcrumb>
                  <el-divider></el-divider>
                  <el-row>
                      <el-col :span="12">
                          <ul class="ad-flex ad-flexEnd mg-top-10 ">
                              <li v-for="(item,index) in pramas" :key="item.routeId" class="paramLi mg-right-10" @click="pramaChange(index)">
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
         <div>
           <el-carousel trigger="click" height="250px">
            <el-carousel-item v-for="item in 3" :key="item">
              <i class="news"></i>
            </el-carousel-item>
          </el-carousel>
          </div>
          <div style="padding:25px">
              <div class="ad-flex ad-flexBtw ad-flexCenter mg-bot-10">
                <div>
                  <i class="el-icon-chat-line-square ad-green font-18"></i>
                  <span class="ad-gray font-18">最新消息</span>
                </div>
                <!-- <el-button type="text" class="ad-lightgray textRight">查看更多></el-button> -->
              </div>
              <ul>
                <li v-for="news in newList" :key="news._id" class="ad-flex ad-flexBtw mg-bot-20">
                  <a :href="news.link" class="ad-gray" target="_blank">{{news.title}}</a>
                  <span class="ad-lightgray">{{news.date}}</span>
                </li>
              </ul>
          </div>
        
       </div>
     </el-col>
   </el-row>
 
</template>

<script>
import {getNewsList} from 'service/getData'

export default {
  name: 'infoBank',
  data () {
    return {
      routeMatch:{},
      paramActive:0,
      pramas:[{
            name:'马铃薯常见病虫害',
            routeId:'ordinary',
            index:0
        },{
            name:'病虫害数据库',
            routeId:'knowledgeBase',
            index:1
        }],
      newList:[]
    }
  },
  mounted(){
    this.routeMatch = this.$route;
    if(this.routeMatch.name=="knowledgeBase"){
      this.paramActive = 1;
    }
    this.getNewsList();
  },
  methods:{
    async getNewsList(){
      let resp = await getNewsList(1,5);
      if(resp.code==0){
        this.newList = resp.data;
      }
    },
    pramaChange(index){
      this.paramActive = index;
      this.routeMatch = {};
      this.$router.push({name:this.pramas[index].routeId});
    },
    updateRoute(val){
      this.routeMatch = val;
    }
  }
}
</script>
<style>

</style>

