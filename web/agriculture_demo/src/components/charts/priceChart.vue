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
        name: 'priceChart',
        data () {
            return {
                appleData:{
                    label:['9.8','10','10.2','10.4','10.6','10.8','11','11.2','11.4','11.6','11.8','12','12.2','12.4','12.6','12.8','13','13.2','13.4','13.6','13.8'],
                    data1:[0 ,3 ,5 ,3 ,12 ,18 ,28 ,35 ,50 ,57 ,66 ,52 ,49 ,42 ,28 ,33 ,8 ,7 ,1 ,1 ,0 ],
                    data2:[0.42501833,1.098974002,2.571211063,5.443253863,10.42677502,18.07223927,28.34291306,40.22050816,51.64415475,60.00194742,63.07831305,60.00194742,51.64415475,40.22050816,28.34291306,18.07223927,10.42677502,5.443253863,2.571211063,1.098974002,0.42501833],
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
                let priceChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                        title: {
                            text: '2019年6月中旬苹果价格预测概率分布图',
                            left: 'center'
                        },
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {
                                type: 'cross',
                                crossStyle: {
                                    color: '#999'
                                }
                            },
                            formatter: '{c}%'
                        },
                        xAxis: [
                            {
                                type: 'category',
                                data: data.label,
                                boundaryGap: false,
                                axisLine :{
                                    show:false,
                                },
                                axisTick:{
                                    show:false,
                                },
                                axisPointer: {
                                    type: 'shadow'
                                }
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLine :{
                                    show:false,
                                },
                                axisTick:{
                                    show:false,
                                },
                            }
                        ],
                        grid:{
                            // top:"20px",
                            left:"40px",
                            right:"35px",
                            bottom:"30px"
                        },
                        series: [
                            {
                                type:'bar',
                                data:data.data1,
                                itemStyle:{
                                    color:'#61a0a8'
                                }
                            },
                            {
                                type:'line',
                                data:data.data2,
                                smooth:true,
                                itemStyle : {  
                                    normal : { 
                                        color: '#FBB02F'
                                    }  
                                }, 
                                lineStyle:{  
                                    color:'#FBB02F',
                                    width:2,
                                    shadowColor : 'rgba(0,0,0,0.16)',
                                    shadowBlur: 6,
                                    shadowOffsetX: 0,
                                    shadowOffsetY: 10
                                }
                            }
                        ]
                    };
                priceChart.setOption(option);
                window.addEventListener('resize', function () {
                    priceChart.resize();
                })
                
                
                
            }
        }

    }
</script>

<style>
</style>
