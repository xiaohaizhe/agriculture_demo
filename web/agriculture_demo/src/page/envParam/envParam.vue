<template>
  <div class="sub-ad bg-fff">
            <el-breadcrumb separator-class="el-icon-arrow-right">
                <el-breadcrumb-item :to="{ name: 'cropManage' }">作物管理</el-breadcrumb-item>
                <el-breadcrumb-item :to="{ name: 'greenhouse' }">马铃薯大棚A-1</el-breadcrumb-item>
                <el-breadcrumb-item>大棚环境参数</el-breadcrumb-item>
            </el-breadcrumb>
            <el-divider></el-divider>
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
                        type="datetimerange"
                        range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期" @change='dateChange'>
                    </el-date-picker>
                </el-form-item>
            </el-form>
            <el-row>
                <el-col :span="16" style="margin-left: 55px;">
                    <ul class="ad-flex ad-flexBtw mg-top-10">
                        <li v-for="(item,index) in pramas" :key="item.id" class="paramLi" @click="pramaChange(index)">
                            <i class="paramActive mg-right-10" :style="{'background-color':paramActive==item.index?'#FBB02F':'#fff'}"></i>{{item.name}}</li>
                    </ul>
                </el-col>
            </el-row>
            <el-row class="mg-top-50">
                <el-col :span="24">
                    <line-chart ref="lineChart" chartId="abc"></line-chart>
                </el-col>
        </el-row>
    </div>
</template>

<script>

import lineChart from 'components/charts/lineChart'
import {getChartData} from 'service/getData'
import {dateFormat} from 'config/mUtils'

export default {
    name: 'envParam',
    data () {
        return {
            paramActive:0,
            form:{
                greenhouse:'1',
                time:'',
                start:'',
                end:''
            },
            pramas:[{
                    name:'环境温度',
                    id:'airTemperature',
                    index:0,
                    unit:'℃'
                },{
                    name:'空气湿度',
                    id:'airHumidity',
                    index:1,
                    unit:'%'
                },{
                    name:'光照强度',
                    id:'illuminance',
                    index:2,
                    unit:'ppm'
                },{
                    name:'二氧化碳浓度',
                    id:'CO2',
                    index:3,
                    unit:'lux'
                },{
                    name:'土壤湿度',
                    id:'soilHumidity',
                    unit:'℃',
                    index:4
                },{
                    name:'土壤温度',
                    id:'soilTemperature',
                    index:1,
                    unit:'%'
                },{
                    name:'土壤PH值',
                    id:'soilpH',
                    index:5,
                    unit:''
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
        this.form.start = dateFormat(new Date(new Date().getTime() - 24*60*60*1000),' 00:00:00');
        this.form.end = dateFormat(new Date(new Date().getTime() - 24*60*60*1000),' 23:59:59');
        this.form.time = [this.form.start,this.form.end];
        this.getChartData();
    },
    methods:{
        dateChange(date){
            this.form.start = dateFormat(date[0]);
            this.form.end  = dateFormat(date[1]);
            this.getChartData();
        },
        pramaChange(index){
          this.paramActive = index;
          this.getChartData();
        },
        async getChartData(){
            let resp = await getChartData(this.pramas[this.paramActive].id,this.form.start,this.form.end);
            if(resp.code==0){
                this.$refs.lineChart.drawChart(resp.data,this.pramas[this.paramActive].unit);
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