<template>
    <div>
        <!-- <p class="center" v-show="!hasData" style="height:50px;line-height:50px;">暂无数据</p> -->
        <div :id="chartId" style="height:200px;"></div>
    </div>
    
</template>

<script>
    // let echarts = require('echarts/lib/echarts')
    // // 引入折线图
    // require('echarts/lib/chart/line');
    // // 提示框
    // require('echarts/lib/component/tooltip')

    export default {
        name: 'lineChart',
        data () {
            return {
                // hasData:false
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
            async drawChart(dsData){
                if(dsData.length==0){
                    this.$message({
                        message: "暂无统计数据",
                        type: 'warning'
                    });
                }
                let lineChart = this.$echarts.init(document.getElementById(this.chartId));
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
                            data: ['1','2','3','4']
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
                            left:"40px",
                            right:"35px",
                            bottom:"35px"
                        },
                        series: [{
                            data: [1,2,3,4],
                            type: 'line',
                            itemStyle : {  
                                normal : { 
                                    color: '#FBB02F'
                                }  
                            }, 
                            lineStyle:{  
                                color:'#FBB02F',
                                width:2
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
