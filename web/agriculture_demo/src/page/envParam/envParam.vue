<template>
  <el-container class="sub-ad bg-fff">
        <el-header height="80px">
            <el-breadcrumb separator-class="el-icon-arrow-right">
                <el-breadcrumb-item :to="{ name: 'cropManage' }">作物管理</el-breadcrumb-item>
                <el-breadcrumb-item :to="{ name: 'greenhouse' }">马铃薯大棚A-1</el-breadcrumb-item>
                <el-breadcrumb-item>大棚环境参数</el-breadcrumb-item>
            </el-breadcrumb>
            <el-divider></el-divider>
        </el-header>
        <el-main>
            <el-form class="ad-flex" ref="form" :model="form"  label-position="left" label-width="50px">
                <el-form-item label="大棚" class="mg-right-20">
                    <el-select v-model="form.greenhouse">
                    <el-option
                        v-for="item in ghData"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="日期" class="mg-right-20">
                    <el-date-picker
                        v-model="form.time"
                        type="daterange"
                        range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期">
                    </el-date-picker>
                </el-form-item>
            </el-form>
            <el-row>
                <el-col :span="16" style="margin-left: 55px;">
                    <ul class="ad-flex ad-flexBtw mg-top-10">
                        <li v-for="(item,index) in pramas" :key="item.id" class="paramLi" @click="pramaChange(index)">
                            <i class="paramActive mg-right-10" :style="{'background-color':paramActive==item.id?'#FBB02F':'#fff'}"></i>{{item.name}}</li>
                    </ul>
                </el-col>
            </el-row>
            <el-row class="mg-top-50">
                <el-col :span="24">
                    <line-chart ref="lineChart" chartId="abc"></line-chart>
                </el-col>
            </el-row>
        </el-main>
    </el-container>
</template>

<script>

import lineChart from 'components/charts/lineChart'
import {getChartData} from 'service/getData'

export default {
    name: 'envParam',
    data () {
        return {
            paramActive:'airTemperature',
            form:{
                greenhouse:'1',
                time:''
            },
            pramas:[{
                    name:'环境温度',
                    id:'airTemperature',
                },{
                    name:'空气湿度',
                    id:'airHumidity'
                },{
                    name:'光照强度',
                    id:'illuminance'
                },{
                    name:'二氧化碳浓度',
                    id:'CO2'
                },{
                    name:'土壤湿度',
                    id:'soilHumidity'
                },{
                    name:'土壤温度',
                    id:'soilTemperature'
                },{
                    name:'土壤PH值',
                    id:'soilpH '
                }],
            ghData:[{
                    value:'1',
                    label:'马铃薯大棚A-1'
                    },{
                        value:'2',
                        label:'马铃薯大棚A-2'
                    },{
                        value:'3',
                        label:'马铃薯大棚A-3'
                    }]
        }
    },
    components:{
        'line-chart':lineChart
    },
    mounted(){
        // this.$refs.lineChart.drawChart();
        this.getChartData();
    },
    methods:{
        pramaChange(index){
          this.paramActive = this.pramas[index].id;
          this.getChartData();
        },
        async getChartData(){
            let resp = await getChartData(this.paramActive);
            if(resp.code==0){
                this.$refs.lineChart.drawChart(resp.data);
            }else{
                this.$message({
                    type: 'error',
                    message: '获取数据失败!'
                });
            }
        }
    }
}
</script>
<style>

</style>