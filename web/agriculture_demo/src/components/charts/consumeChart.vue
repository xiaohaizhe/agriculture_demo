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
                let consumeChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                    xAxis: {
                        type: 'category',
                        axisLine :{
                            show:false,
                        },
                        axisTick:{
                            show:false,
                        },
                        data: ['2009', '2010', '2011', '2012', '2013', '2014', '2015','2016','2017']
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
                        data: [2935.72, 3059.30, 3271.52, 3489.92, 3534.20, 3651.70, 3815.35,3912.13,4013.04],
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
