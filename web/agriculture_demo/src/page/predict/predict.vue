<template>
    <el-container class="sub-ad bg-fff">
          <el-header height="130px">
              <el-breadcrumb separator-class="el-icon-arrow-right">
                  <el-breadcrumb-item :to="{name:'predict'}">行情与预测</el-breadcrumb-item>
                  <el-breadcrumb-item>{{pramas[paramActive].name}}</el-breadcrumb-item>
              </el-breadcrumb>
              <el-divider></el-divider>
              <el-row>
                  <el-col :span="12">
                      <ul class="ad-flex ad-flexEnd mg-top-10 ">
                          <li v-for="(item,index) in pramas" :key="item.routeId" class="paramLi mg-right-10" @click="pramaChange(index)">
                              <i class="paramActive mg-right-10" :style="{'background-color':paramActive==item.index?'#FBB02F':'#fff'}"></i>{{item.name}}</li>
                      </ul>
                      <ul class="ad-flex ad-flexEnd mg-top-10" style="padding-left:20px">
                          <li v-for="(item,index) in analyses" :class="{analyseActive:analyseActive==item.index}" :key="item.id" class="paramLi mg-right-10" @click="analyseChange(index)" >{{item.name}}</li>
                      </ul>
                  </el-col>
              </el-row>
          </el-header>
          <el-main>
          </el-main>
    </el-container>
</template>

<script>
export default {
  name: 'predict',
  data () {
    return {
      paramActive:0,
      analyseActive:0,
      pramas:[{
          name:'马铃薯',
          index:0
        },{
          name:'番茄',
          index:1
        },{
          name:'青椒',
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
        id:'predict',
        index:2
      }]
    }
  },
  methods:{
    pramaChange(index){
      this.paramActive = index;
    },
    analyseChange(index){
      this.analyseActive = index;
    },
  }
}
</script>
