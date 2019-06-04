<template>
    <div :id="chartId" style="height:280px"></div>
</template>

<script>
    // let echarts = require('echarts/lib/echarts')
    // // 地图
    // require('echarts/lib/chart/map')
    // // 提示框
    // require('echarts/lib/component/tooltip')
    // require('echarts/lib/component/visualMap')
    // require('echarts/lib/component/title')
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
                let provinceChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                        visualMap: {
                            type: 'continuous',
                            // text: ['', ''],
                            calculable: true,
			                show: true,
                            right: '0',
                            top:'0',
                            color:['#0756AF','rgba(7,86,175,0.05)'],
                            min: 0,
                            max: data.data[0].value
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
                                data: data.data
                                    }]
                                        }
                provinceChart.setOption(option);
                window.addEventListener('resize', function () {
                    provinceChart.resize();
                })
            }
        }

    }
</script>
