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
        name: 'importChart',
        data () {
            return {
                appleData:{
                    label:['2009', '2010', '2011', '2012', '2013', '2014', '2015','2016','2017'],
                    data1:[5.4, 6.6, 7.7, 6.1, 3.8, 2.8, 8.7,6.7,6.8],
                    data2: [117.18, 112.29, 103.46, 97.58, 99.46, 86.50, 83.30,133.90,132.83],
                    unit:'万吨',
                    title:'2009-2017年鲜苹果进出口贸易统计数据'
                },
                strawberryData:{
                    label:['2006','2007','2008','2009', '2010', '2011', '2012', '2013', '2014', '2015','2016','2017'],
                    data1:[0,0,574,0,0,0,0,0,182,0,341,47584],
                    data2:[2279063,969527,360524,202532,345562,827755,1010572,797264,1291462,1453549,1575214,2286796],
                    unit:'kg',
                    title:'2009-2017年鲜草莓进出口贸易统计数据'
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
                let importChart = this.$echarts.init(document.getElementById(this.chartId));
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
                        data:data.label
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a}<br/>{b}：{c}'+data.unit
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
                    legend: {
                        data: ['进口', '出口'],
                        align: 'left',
                        bottom :0
                    },
                    series: [{
                        data: data.data1,
                        type: 'bar',
                        name:'进口',
                        barMaxWidth :20,
                        itemStyle: {
                            normal: {
                                barBorderRadius :[100,100,0,0],
                                color: new this.$echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [
                                        {offset: 1, color: 'rgba(238,90,90,0)'},
                                        {offset: 0.5, color: 'rgba(244,121,121,0.5)'},
                                        {offset: 0, color: '#F99595'}
                                    ]
                                )
                            },
                        }
                    },{
                        data:data.data2,
                        type: 'bar',
                        name:'出口',
                        barMaxWidth :20,
                        itemStyle: {
                            normal: {
                                barBorderRadius :[100,100,0,0],
                                color: new this.$echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [
                                        {offset: 0, color: '#8FFF20'},
                                        {offset: 0.5, color: 'rgba(158,234,60,0.5)'},
                                        {offset: 1, color: 'rgba(175,210,92,0)'}
                                    ]
                                )
                            },
                        }
                    }
                    ]
                };
                importChart.setOption(option);
                window.addEventListener('resize', function () {
                    importChart.resize();
                })
                
                
                
            }
        }

    }
</script>

<style>
</style>
