<template>
    <div>
        <!-- <p class="center" v-show="!hasData" style="height:50px;line-height:50px;">暂无数据</p> -->
        <div :id="chartId" style="height:500px"></div>
    </div>
    
</template>

<script>
    // let echarts = require('echarts/lib/echarts')
    // require('echarts/lib/chart/bar');
    // // 提示框
    // require('echarts/lib/component/tooltip')
    // require('echarts/lib/component/legend')

    export default {
        name: 'consumeChart',
        data () {
            return {
                appleData:{
                    label:['2009', '2010', '2011', '2012', '2013', '2014', '2015','2016','2017'],
                    data:[2935.72, 3059.30, 3271.52, 3489.92, 3534.20, 3651.70, 3815.35,3912.13,4013.04],
                    title:'2009-2017年苹果的表观消费量数据'
                },
                strawberryData:{
                    label:['2006','2007','2008','2009', '2010', '2011', '2012', '2013', '2014', '2015','2016','2017'],
                    data:[187.34,187.08,200.00,220.57,232.96,249.01,275.99,299.72,311.17,347.75,341.84,399.77],
                    title:'2009-2017年草莓的表观消费量数据'
                }
            }
        },
        props: {
            chartId:{
                type:String
            }
        },
        mounted(){
        },
        methods: {
            async drawChart(type){
                let data= {}
                if(type=="apple"){
                    data=this.appleData;
                }else{
                    data= this.strawberryData;
                }
                let consumeChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                    title: {
                            text: data.title,
                            left: 'center'
                        },
                    xAxis: {
                        type: 'category',
                        axisLine :{
                            show:false,
                        },
                        axisTick:{
                            show:false,
                        },
                        data: data.label
                    },
                    tooltip: {
                        trigger: 'axis',
                        formatter: '{b}消费：<br/>{c}万吨'
                    },
                    yAxis: {
                        type: 'value',
                        axisLine :{
                            show:false,
                        },
                        axisTick:{
                            show:false,
                        }
                    },
                    series: [{
                        data: data.data,
                        type: 'bar',
                        barMaxWidth :20,
                        itemStyle: {
                            normal: {
                                barBorderRadius :[100,100,0,0],
                                color: '#B19BC8'
                            },
                        }
                    }]
                };
                consumeChart.setOption(option);
                window.addEventListener('resize', function () {
                    consumeChart.resize();
                })
                
                
                
            }
        }

    }
</script>

<style>
</style>
