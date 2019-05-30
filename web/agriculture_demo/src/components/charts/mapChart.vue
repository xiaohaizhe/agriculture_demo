<template>
    <div :id="chartId" style="height:500px"></div>
</template>

<script>
    // 引入基本模板
    let echarts = require('echarts/lib/echarts')
    // 引入line图组件
    require('echarts/lib/chart/map')
    require('echarts/lib/component/tooltip')
    import china from 'echarts/map/json/china.json'
    echarts.registerMap('china', china)

    export default {
        name: 'mapChart',
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
            this.drawChart();
        },
        methods: {
            drawChart(){
                let areaChart = echarts.init(document.getElementById(this.chartId));
                let option = {
                        title: {
                            text: 'iphone销量',
                            subtext: '纯属虚构',
                            left: 'center'
                        },
                        tooltip: {
                            trigger: 'item'
                        },
                        legend: {
                            orient: 'vertical',
                            left: 'left',
                            data:['iphone3']
                        },
                        visualMap: {
                            min: 0,
                            max: 2500,
                            left: 'left',
                            top: 'bottom',
                            text: ['高','低'],           // 文本，默认为数值文本
                            calculable: true
                        },
                        toolbox: {
                            show: true,
                            orient: 'vertical',
                            left: 'right',
                            top: 'center',
                            feature: {
                                dataView: {readOnly: false},
                                restore: {},
                                saveAsImage: {}
                            }
                        },
                        series: [
                            {
                                name: 'iphone3',
                                type: 'map',
                                mapType: 'china',
                                roam: false,
                                label: {
                                    normal: {
                                        show: true
                                    },
                                    emphasis: {
                                        show: true
                                    }
                                },
                                data:[
                                    {name: '北京',value: Math.round(Math.random()*1000) },
                                    {name: '天津',value: Math.round(Math.random()*1000) },
                                    {name: '上海',value: Math.round(Math.random()*1000) },
                                    {name: '重庆',value: Math.round(Math.random()*1000) },
                                    {name: '河北',value: Math.round(Math.random()*1000) },
                                    {name: '河南',value: Math.round(Math.random()*1000) },
                                ]
                            }
                        ]
                    };
                areaChart.setOption(option);
                window.addEventListener('resize', function () {
                    areaChart.resize();
                })
                
                
                
            }
        }

    }
</script>
