<template>
    <div :id="chartId"></div>
</template>

<script>
    let echarts = require('echarts/lib/echarts')
    // 地图
    require('echarts/lib/chart/map')
    // 提示框
    require('echarts/lib/component/tooltip')
    require('echarts/lib/component/visualMap')
    require('echarts/lib/component/title')
    import china from 'static/cities.json'
    
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
            
        },
        methods: {
            drawChart(data){
                //获取当前时间
                let date = new Date();
                let year = date.getFullYear();
                let month = date.getMonth() + 1;
                let day = date.getDate();
                let nowDate = year + "年" + month + "月" + day + "日";
                data.data.push({"name":"南海诸岛","value":data.max});
                echarts.registerMap('china', china);
                let areaChart = echarts.init(document.getElementById(this.chartId));
                let option = {
                        // backgroundColor: '#021926',
                        title: {
                            text: nowDate+'全国气温分布图',
                            left: 'center',
                        },
                        visualMap: {
                            type: 'continuous',
                            // text: ['', ''],
                            calculable: true,
			                show: true,
                            right: '50',
                            top:'50',
                            min: data.min,
                            max: data.max
                        },
                        tooltip: {
                            trigger: 'item',
                            formatter: function (params, ticket, callback) {
                                    if(isNaN(params.value)){
                                        return params.name+"："+"无";
                                    }else{
                                        return params.name+"："+params.value+"℃";
                                    }
                                    
                                }
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
                        areaChart.setOption(option);
                
            }
        }

    }
</script>
