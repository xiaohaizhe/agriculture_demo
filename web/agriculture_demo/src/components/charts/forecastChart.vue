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
                appleData:{
                    label:['2019年1月上旬','2019年1月中旬','2019年1月下旬','2019年2月上旬','2019年2月中旬','2019年2月下旬','2019年3月上旬','2019年3月中旬','2019年3月下旬','2019年4月上旬','2019年4月中旬','2019年4月下旬','2019年5月上旬','2019年5月中旬','2019年5月下旬','2019年6月上旬','2019年6月中旬','2019年6月下旬','2019年7月上旬','2019年7月中旬','2019年7月下旬','2019年8月上旬','2019年8月中旬','2019年8月下旬','2019年9月上旬','2019年9月中旬','2019年9月下旬'],
                    data1:[6.30 ,6.30 ,6.30 ,6.30 ,6.30 ,6.30 ,6.15 ,7.00 ,7.25 ,7.73 ,8.28, 8.69, 9.00, 10.88, 11.96, 11.80],
                    data2:[,,,,,,,,,,,,,,,11.80,11.80 ,12.00 ,12.18 ,11.60 ,11.40 ,10.80 ,10.68 ,10.68 ,10.40 ,10.40 ,10.60],//第一个数据为data1的最后一个数据
                    title:'北京丰台区新发地农产品批发市场苹果价格走势与行情预测'
                },
                strawberryData:{
                    label:['2019年1月上旬','2019年1月中旬','2019年1月下旬','2019年2月上旬','2019年2月中旬','2019年2月下旬','2019年3月上旬','2019年3月中旬','2019年3月下旬','2019年4月上旬','2019年4月中旬','2019年4月下旬','2019年5月上旬','2019年5月中旬','2019年5月下旬','2019年6月上旬','2019年6月中旬','2019年6月下旬','2019年7月上旬','2019年7月中旬','2019年7月下旬','2019年8月上旬','2019年8月中旬','2019年8月下旬','2019年9月上旬','2019年9月中旬','2019年9月下旬'],
                    data1:[35.00 ,28.59,28.59,28.00,27.82,27.82,16.00,17.14,17.14,17.00,17.00,16.00,17.00,17.00,16.00,16.00],
                    data2:[,,,,,,,,,,,,,,,16.00,16.00,16.00,18.00,23.00,28.00,28.00,29.00,30.00,28.00,26.00,26.00],//第一个数据为data1的最后一个数据
                    title:'河北邯郸（魏县）天仙果品农贸批发交易市场草莓价格走势与行情预测'
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
                let nowMonth = new Date().getMonth+1;
                let forecastChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                        title: {
                            text: data.title,
                            left: 'center'
                        },
                        tooltip: {
                            trigger: 'axis',
                            formatter: '{b}：<br/>{c}（元/公斤）'
                        },
                        // visualMap: {
                        //     show: false,
                        //     dimension: 0,
                        //     pieces: [{
                        //         label: '2019年6月上旬',
                        //         color: 'green'
                        //     }]
                        // },
                        xAxis: {
                            type: 'category',
                            boundaryGap: false,
                            axisLine :{
                                show:false,
                            },
                            axisTick:{
                                show:false,
                            },
                            data:data.label
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
                            top:"80px",
                            left:"60px",
                            right:"60px",
                            bottom:"35px"
                        },
                        series: [{
                            data: data.data1,
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
                        },{
                            data: data.data2,
                            type: 'line',
                            // itemStyle : {  
                            //     normal : { 
                            //         color: '#2FD8FB'
                            //     }  
                            // }, 
                            itemStyle:{
                                normal:{
                                    lineStyle:{
                                        width:2,
                                        type:'dotted',  //'dotted'虚线 'solid'实线
                                        color:'#2FD8FB' 
                                    },
                                    color:'#2FD8FB', 
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
