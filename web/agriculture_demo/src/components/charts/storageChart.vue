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
        name: 'storageChart',
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
                let storageChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                    xAxis: {
                        type: 'value',
                        axisLine :{
                            show:false,
                        },
                        axisTick:{
                            show:false,
                        },
                    },
                    tooltip: {
                        trigger: 'axis',
                        formatter: '{b}：{c}'
                    },
                    yAxis: {
                        type: 'category',
                        axisLine :{
                            show:false,
                        },
                        axisTick:{
                            show:false,
                        },
                        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                    },
                    series: [{
                        data: [120, 200, 150, 80, 70, 110, 130],
                        type: 'bar',
                        barMaxWidth :20,
                        itemStyle: {
                            normal: {
                                barBorderRadius :[0,100,100,0],
                                color: new this.$echarts.graphic.LinearGradient(
                                    0, 0, 1, 0,
                                    [
                                        {offset: 0, color: 'rgba(90,210,178,0)'},
                                        {offset: 0.5, color: 'rgba(73,208,182,0.5)'},
                                        {offset: 1, color: '#38CEB9'}
                                    ]
                                )
                            },
                        }
                    }]
                };
                storageChart.setOption(option);
                window.addEventListener('resize', function () {
                    storageChart.resize();
                })
                
                
                
            }
        }

    }
</script>

<style>
</style>
