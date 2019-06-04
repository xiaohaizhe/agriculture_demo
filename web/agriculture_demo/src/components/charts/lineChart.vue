<template>
    <div>
        <!-- <p class="center" v-show="!hasData" style="height:50px;line-height:50px;">暂无数据</p> -->
        <div :id="chartId" :style="{height:height}"></div>
    </div>
    
</template>

<script>
    // let echarts = require('echarts/lib/echarts')
    // // 引入折线图
    // require('echarts/lib/chart/line');
    // // 提示框
    // require('echarts/lib/component/tooltip')
    // require('echarts/lib/component/markLine')

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
            this.height = document.getElementById("el-main").clientHeight-300+"px";
        },
        methods: {
            async drawChart(data,unit){
                if(data.data==0){
                    this.$message({
                        message: "暂无统计数据",
                        type: 'warning'
                    });
                }
                let lineChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                        tooltip: {
                            trigger: 'axis',
                            formatter: '{b}：<br/>{c}'+unit
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
                            axisLabel:{
                                formatter : function(params){
                                    var newParamsName = "";// 最终拼接成的字符串
                                    var paramsNameNumber = params.length;// 实际标签的个数
                                    var provideNumber = 10;// 每行能显示的字的个数
                                    var rowNumber = 2// 换行的话，需要显示几行
                                    /**
                                     * 判断标签的个数是否大于规定的个数， 如果大于，则进行换行处理 如果不大于，即等于或小于，就返回原标签
                                     */
                                    // 条件等同于rowNumber>1
                                    if (paramsNameNumber > provideNumber) {
                                        /** 循环每一行,p表示行 */
                                        for (var p = 0; p < rowNumber; p++) {
                                            var tempStr = "";// 表示每一次截取的字符串
                                            var start = p * provideNumber;// 开始截取的位置
                                            var end = start + provideNumber;// 结束截取的位置
                                            // 此处特殊处理最后一行的索引值
                                            if (p == rowNumber - 1) {
                                                // 最后一次不换行
                                                tempStr = params.substring(start, paramsNameNumber);
                                            } else {
                                                // 每一次拼接字符串并换行
                                                tempStr = params.substring(start, end) + "\n";
                                            }
                                            newParamsName += tempStr;// 最终拼成的字符串
                                        }

                                    } else {
                                        // 将旧标签的值赋给新标签
                                        newParamsName = params;
                                    }
                                    //将最终的字符串返回
                                    return newParamsName
                                }

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
