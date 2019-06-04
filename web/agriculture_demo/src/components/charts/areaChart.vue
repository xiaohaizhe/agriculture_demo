<template>
    <div :id="chartId" style="height:250px;border-radius:6px;"></div>
</template>

<script>
    // // 引入基本模板
    // let echarts = require('echarts/lib/echarts')
    // // 引入line图组件
    // require('echarts/lib/chart/line')
    // require('echarts/lib/component/tooltip')

    export default {
        name: 'areaChart',
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
            this.drawChart(this.data);
        },
        methods: {
            drawChart(){
                let areaChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                        backgroundColor:new this.$echarts.graphic.LinearGradient(0, 0, 1, 0,[{
                                        offset: 0, color: '#32A7F4' // 0% 处的颜色
                                    },{
                                        offset: 1, color: '#59ECDD' // 100% 处的颜色
                                    }]
                                ), //背景渐变色,
                        tooltip: {
                            trigger: 'axis',
                            formatter: '{c}'
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
                            splitLine:{
                                show:true,
                                lineStyle:{
                                    type :'dotted'
                                }
                            },
                            axisLabel:{
                                color:'#fff'
                            },
                            data: ['幼苗期','生长期','开花期','结果期','收获期']
                        },
                        yAxis: {
                            type: 'value',
                            boundaryGap: false,
                            axisLine :{
                                show:false,
                            },
                            splitLine:{
                                show:false
                            },
                            axisTick:{
                                show:false,
                            },
                            axisLabel:{
                                show:false,
                            }
                        },
                        grid:{
                            top:"20px",
                            left:"40px",
                            right:"35px",
                            bottom:"30px"
                        },
                        series: [{
                            data: [10,50,30,80,20],
                            type: 'line',
                            smooth: true,
                            itemStyle : {  
                                normal : { 
                                    opacity :0
                                }  
                            }, 
                            lineStyle:{  
                                color:'#FFFFFF',
                                width:0
                            }, 
                            areaStyle: {
                                color:new this.$echarts.graphic.LinearGradient(0, 0, 0, 1,[{
                                        offset: 1, color: 'rgba(255, 255, 255, 0.1)' // 0% 处的颜色
                                    },{
                                        offset: 0.5, color: 'rgba(255, 255, 255, 0.7)' // 100% 处的颜色
                                    },{
                                        offset: 0, color: '#fff' // 100% 处的颜色
                                    }]
                                ), //背景渐变色
                            }
                        }]
                    };
                areaChart.setOption(option);
                window.addEventListener('resize', function () {
                    areaChart.resize();
                })
                
                
                
            }
        }

    }
</script>
