<template>
    <div>
        <!-- <p class="center" v-show="!hasData" style="height:50px;line-height:50px;">暂无数据</p> -->
        <div :id="chartId" :style="{height:height}"></div>
    </div>
    
</template>

<script>
    let echarts = require('echarts/lib/echarts')
    // 引入折线图
    require('echarts/lib/chart/line');
    // 提示框
    require('echarts/lib/component/tooltip')
    require('echarts/lib/component/markLine')

    export default {
        name: 'lineChart',
        data () {
            return {
                height:0
            }
        },
        props: {
            chartId:{
                type:String
            }
        },
        mounted(){
            this.height = window.innerHeight *0.5 +'px'
        },
        methods: {
            async drawChart(data){
                if(data.data==0){
                    this.$message({
                        message: "暂无统计数据",
                        type: 'warning'
                    });
                }
                let lineChart = echarts.init(document.getElementById(this.chartId));
                let option = {
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
                            data: data.time
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
                            data: data.data,
                            markLine: {
                                data: [
                                    {
                                        name: '平均值',
                                        yAxis: data.mean
                                    }
                                ],
                                lineStyle:{
                                    color:'#FF0000',
                                } 
                            },
                            type: 'line',
                            itemStyle : {  
                                normal : { 
                                    color: '#FBB02F'
                                }  
                            }, 
                            smooth:true,
                            lineStyle:{  
                                color:'#FBB02F',
                                width:2,
                                shadowColor : 'rgba(0,0,0,0.16)',
                                shadowBlur: 6,
                                shadowOffsetX: 0,
                                shadowOffsetY: 10
                            }
                        }]
                    };
                lineChart.setOption(option);
                window.addEventListener('resize', function () {
                    lineChart.resize();
                })
                
                
                
            }
        }

    }
</script>

<style>
</style>
