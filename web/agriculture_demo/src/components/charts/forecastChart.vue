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
        name: 'forecastChart',
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
                let forecastChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                        tooltip: {
                            trigger: 'axis',
                            formatter: '{b}：<br/>{c}'
                        },
                        xAxis: {
                            type: 'category',
                            boundaryGap: false,
                            axisLine :{
                                show:false,
                            },
                            axisTick:{
                                show:false,
                            },
                            data:['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
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
                        grid:{
                            top:"20px",
                            left:"60px",
                            right:"60px",
                            bottom:"35px"
                        },
                        series: [{
                            data: [120, 200, 150, 80, 70, 110, 130],
                            type: 'line',
                            itemStyle : {  
                                normal : { 
                                    color: '#2FD8FB'
                                }  
                            }, 
                            // smooth:true,
                            lineStyle:{  
                                color:'#2FD8FB',
                                width:2,
                                shadowColor : 'rgba(0,0,0,0.16)',
                                shadowBlur: 6,
                                shadowOffsetX: 0,
                                shadowOffsetY: 10
                            }
                        }]
                    };
                forecastChart.setOption(option);
                window.addEventListener('resize', function () {
                    forecastChart.resize();
                })
                
                
                
            }
        }

    }
</script>

<style>
</style>
