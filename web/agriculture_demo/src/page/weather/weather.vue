<template>
    <div class="sub-ad bg-fff">
              <el-breadcrumb separator-class="el-icon-arrow-right">
                  <el-breadcrumb-item :to="{name:'weather'}">天气信息</el-breadcrumb-item>
                  <el-breadcrumb-item>{{pramas[paramActive].name}}</el-breadcrumb-item>
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
          <div id="weather">
            <map-chart chartId="mapChart" ref="mapChart" v-if="paramActive==0" :style="{height:height}"></map-chart>
            <div v-if="paramActive==1" class="ad-flex ad-flexCenter ad-justifyCenter">
              <img :src="precipitation" alt="降雨量图片">
            </div>
            <div v-if="paramActive==2" class="textCenter" style="padding: 0 10%;">
              <p class="font-24 mg-bot-10">{{assessment.title}}</p>
              <p class="font-18 mg-bot-10" v-for="item in assessment.subhead" :key="item">{{item}}</p>
              <p class="mg-bot-10">{{assessment.author}} {{assessment.date}}</p>
              <p v-for="item in assessment.content" :key="item._id" class="textLeft mg-bot-10">{{item}}</p>
              <img v-for="item in assessment.image_urls" :key="item" :src="item"/>
            </div>
          </div>
    </div>
</template>

<script>
import {getPrecipitationList,getAssessment,getWeatherList} from 'service/getData'
import mapChart from 'components/charts/mapChart'

export default {
  name: 'weather',
  data () {
    return {
      height:'500px',
      paramActive:0,
      pramas:[{
          name:'平均气温',
          index:0
        },{
          name:'降水情况',
          index:1
        },{
          name:'农业气象影响预报与评估',
          index:2
        }],
      precipitation:[],
      assessment:{}
    }
  },
  components:{
      'map-chart':mapChart
  },
  mounted(){
    this.height = document.getElementById("el-main").clientHeight-200+"px";
    this.getWeatherList();
  },
  methods:{
    pramaChange(index){
      this.paramActive = index;
      switch(index){
        case 0:this.getWeatherList();break;
        case 1:this.getPrecipitationList();break;
        case 2:this.getAssessment();break;
      }
    },
    //
    async getWeatherList(){
      let resp = await getWeatherList();
      if(resp.code==0){
        this.$refs.mapChart.drawChart(resp)
      }
    },
    //获取降雨量前30名城市列表
    async getPrecipitationList(){
      let resp = await getPrecipitationList();
      if(resp.code==0){
        this.precipitation = resp.data[0].image_url;
        
      }
    },
    //获取最新气象预告与评估
    async getAssessment(){
      let resp = await getAssessment();
      if(resp.code==0){
        this.assessment = resp.data[0];
      }
    }
  }
}
</script>
