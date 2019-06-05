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
            async drawChart(){
                let importChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                    xAxis: {
                        type: 'category',
                        axisLine :{
                            show:false,
                        },
                        axisTick:{
                            show:false,
                        },
                        data:['2009', '2010', '2011', '2012', '2013', '2014', '2015','2016','2017']
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: '{a}<br/>{b}：{c}万吨'
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
                        data: [5.4, 6.6, 7.7, 6.1, 3.8, 2.8, 8.7,6.7,6.8],
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
                        data: [117.18, 112.29, 103.46, 97.58, 99.46, 86.50, 83.30,133.90,132.83],
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
