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
        name: 'outputChart',
        data () {
            return {
                apple:{
                    label:['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017'],
                    data1:[0,0,3047.49,3164.91,3367.28,3581.36,3629.81,3735.39,3889.9,4039.33,4139],
                    data2:[0,1992.26,2049.11,2139.94,2177.32,2231.35,2272.2,2272.2,2328.3,2323.8,0]
                },
                strawberry:{
                    label:['2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017'],
                    data1:[187.57,187.18,200.04,220.6,233,249.1,276.1,299.8,311.3,347.9,342,400],
                    data2:[79.3,79.4,83.3,90.1,91.2,95.9,100.5,109.94,113.4,129.3,129.71,230]
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
                    data=this.apple;
                }else{
                    data= this.strawberry;
                }
                let outputChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
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
                        formatter: '{a}<br/>{b}：{c}'
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
                        data: ['产量（万吨）', '种植面积（千公顷）'],
                        align: 'left',
                        bottom :0
                    },
                    series: [{
                        data: data.data1,
                        type: 'bar',
                        name:'产量（万吨）',
                        barMaxWidth :20,
                        itemStyle: {
                            normal: {
                                barBorderRadius :[100,100,0,0],
                                color: new this.$echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [
                                        {offset: 1, color: 'rgba(90,135,238,0)'},
                                        {offset: 0.5, color: 'rgba(120,163,244,0.5)'},
                                        {offset: 0, color: '#95BDF9'}
                                    ]
                                )
                            },
                        }
                    },{
                        data: data.data2,
                        type: 'bar',
                        name:'种植面积（千公顷）',
                        barMaxWidth :20,
                        itemStyle: {
                            normal: {
                                barBorderRadius :[100,100,0,0],
                                color: new this.$echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [
                                        {offset: 0, color: '#38CEB9'},
                                        {offset: 0.5, color: 'rgba(78,208,181,0.5)'},
                                        {offset: 1, color: 'rgba(92,210,178,0)'}
                                    ]
                                )
                            },
                        }
                    }
                    ]
                };
                outputChart.setOption(option);
                window.addEventListener('resize', function () {
                    outputChart.resize();
                })
                
                
                
            }
        }

    }
</script>

<style>
</style>
