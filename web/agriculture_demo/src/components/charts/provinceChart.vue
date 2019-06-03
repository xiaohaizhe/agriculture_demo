<template>
    <div :id="chartId" style="height:280px"></div>
</template>

<script>
    let echarts = require('echarts/lib/echarts')
    // 地图
    require('echarts/lib/chart/map')
    // 提示框
    require('echarts/lib/component/tooltip')
    require('echarts/lib/component/visualMap')
    require('echarts/lib/component/title')
    require('echarts/map/js/china')

    export default {
        name: 'provinceChart',
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
            drawChart(data){
                let provinceChart = echarts.init(document.getElementById(this.chartId));
                let option = {
                        visualMap: {
                            type: 'continuous',
                            // text: ['', ''],
                            calculable: true,
			                show: true,
                            right: '0',
                            top:'0',
                            min: 0,
                            max: 20
                        },
                        tooltip: {
                            trigger: 'item'
                        },
                        series: [{
                                name: '温度',
                                type: 'map',
                                mapType: 'china',
                                label: {
                                    normal: {
                                        show: false
                                    }
                                },
                                roam:true,
                                data: [{name:"北京",value:7.5}]
                                    }]
                                        }
                provinceChart.setOption(option);
                
            }
        }

    }
</script>
