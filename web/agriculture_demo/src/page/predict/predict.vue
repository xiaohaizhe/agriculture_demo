<template>
  <el-row :gutter="30" class="height100">
    <el-col :span="16" class="height100">
      <div class="sub-ad bg-fff">
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{name:'predict'}">行情与预测</el-breadcrumb-item>
            <el-breadcrumb-item>{{pramas[paramActive].name}}</el-breadcrumb-item>
        </el-breadcrumb>
        <el-divider></el-divider>
        <el-row>
            <el-col :span="24">
                <ul class="ad-flex ad-flexEnd mg-top-10 ">
                    <li v-for="(item,index) in pramas" :key="item.routeId" class="paramLi mg-right-10" @click="pramaChange(index)">
                        <i class="paramActive mg-right-10" :style="{'background-color':paramActive==item.index?'#FBB02F':'#fff'}"></i>{{item.name}}</li>
                </ul>
                <ul class="ad-flex ad-flexEnd mg-top-20" style="padding-left:20px">
                    <li v-for="(item,index) in analyses" :class="{analyseActive:analyseActive==item.index}" :key="item.id" class="paramLi mg-right-10" style="margin:15px 30px 15px 0" @click="analyseChange(index)" >{{item.name}}</li>
                </ul>
            </el-col>
        </el-row>
        <router-view></router-view>
      </div>
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
                  <span class="ad-gray">{{news.title}}</span>
                  <span class="ad-lightgray">{{news.date}}</span>
                </li>
              </ul>
          </div>
        
       </div>
     </el-col>
  </el-row>
    
</template>

<script>
import {getStrawberryNews} from 'service/getData'
export default {
  name: 'predict',
  data () {
    return {
      paramActive:0,
      analyseActive:0,
      newList:[],
      pramas:[{
          name:'苹果',
          id:'apple',
          index:0
        },{
          name:'草莓',
          id:'strawberry',
          index:1
        },{
          name:'青椒',
          id:'pepper',
          index:2
        }],
      analyses:[{
        name:'价格',
        id:'price',
        index:0
      },{
        name:'供需',
        id:'supply',
        index:1
      },{
        name:'行业预测',
        id:'forecast',
        index:2
      }]
    }
  },
  mounted(){
    this.getStrawberryNews();
  },
  methods:{
    pramaChange(index){
      this.paramActive = index;
      this.$router.push('/index/predict/'+this.analyses[this.analyseActive].id);
    },
    analyseChange(index){
      this.analyseActive = index;
      this.$router.push('/index/predict/'+this.analyses[index].id);
    },
    async getStrawberryNews(){
        let resp = await getStrawberryNews();
        if(resp.code==0){
            this.newList = resp.data;
        }
    }
  }
}
</script>
