<template>
    <el-container class="sub-ad bg-fff">
          <el-header height="130px">
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
          </el-header>
          <el-main>
            <map-chart chartId="mapChart"></map-chart>
          </el-main>
    </el-container>
</template>

<script>
import {getPrecipitationList} from 'service/getData'
import mapChart from 'components/charts/mapChart'

export default {
  name: 'weather',
  data () {
    return {
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
      precipitation:[]
    }
  },
  components:{
      'map-chart':mapChart
  },
  mounted(){
    this.getPrecipitationList();
  },
  methods:{
    pramaChange(index){
      this.paramActive = index;
    },
    async getPrecipitationList(){
      let resp = await getPrecipitationList();
      if(resp.code==0){
        this.precipitation =resp.data;
      }
    }
  }
}
</script>
