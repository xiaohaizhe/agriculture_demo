<template>
    <div :id="chartId" style="height:500px"></div>
</template>

<script>
    // let echarts = require('echarts/lib/echarts')
    // // 地图
    // require('echarts/lib/chart/map')
    // require('echarts/lib/chart/scatter')
    // require('echarts/lib/chart/effectScatter')
    // // 提示框
    // require('echarts/lib/component/tooltip')
    // require('echarts/lib/component/visualMap')
    // require('echarts/lib/component/title')
    require('echarts/map/js/china')
    // // 地图geo
    // require('echarts/lib/component/geo')
    // require('echarts/lib/component/markPoint')
    export default {
        name: 'productChart',
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
            convertData(data,geoCoordMap) {
                var res = [];
                for (var i = 0; i < data.length; i++) {
                    var geoCoord = geoCoordMap[data[i].name];
                    if (geoCoord) {
                        res.push({
                            name: data[i].name,
                            value: geoCoord.concat(data[i].value)
                        });
                    }
                }
                return res;
            },
            drawChart(){
                var geoCoordMap = {
                    "山东": [118.01 , 36.37],
                    "陕西": [108.94 , 34.46],
                    '山西':[111.95,37.65]
                }
                var data = [{
                        name: '山东',
                        value: 9416.8
                    },
                    {
                        name: '陕西',
                        value: 7605.31
                    },
                    {
                        name: '山西',
                        value: 3723.03
                    }
                ];
                var max = 100000,
                    min = 900; // todo 
                var maxSize4Pin = 100,
                    minSize4Pin = 20;
                let productChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                            tooltip: {
                                trigger: 'item',
                                formatter: function(params) {debugger
                                    if (typeof(params.value)[2] == "undefined") {
                                        if(params.value){
                                            return params.name + ' : ' + params.value+'（万吨）';
                                        }else{
                                            return params.name + ' : ' + '暂无';
                                        }
                                        
                                    } else {
                                        return params.name + ' : ' + params.value[2]+'（万吨）';
                                    }
                                }
                            },
                            visualMap: {
                                show: false,
                                min: 0,
                                max: 500,
                                left: 'left',
                                top: 'bottom',
                                text: ['高', '低'], // 文本，默认为数值文本
                                calculable: true,
                                seriesIndex: [1],
                                inRange: {
                                    color: ['#204AAC'] // 黑紫黑

                                }
                            },
                            geo: {
                                show: true,
                                map: 'china',
                                label: {
                                    normal: {
                                        show: false
                                    },
                                    emphasis: {
                                        show: false,
                                    }
                                },
                                roam: true,
                                itemStyle: {
                                    normal: {
                                        areaColor: '#F6FBFF',
                                        borderColor: '#E0E2EE',
                                    },
                                    emphasis: {
                                        areaColor: '#204AAC'
                                    }
                                }
                            },
                            series: [{
                                    type: 'scatter',
                                    coordinateSystem: 'geo',
                                    data: this.convertData(data,geoCoordMap),
                                    symbolSize: function(val) {
                                        return 5;
                                    },
                                    label: {
                                        normal: {
                                            formatter: '{b}',
                                            position: 'right',
                                            show: false
                                        },
                                        emphasis: {
                                            show: false
                                        }
                                    },
                                    itemStyle: {
                                        normal: {
                                            color: '#FBB02F'
                                        }
                                    }
                                },
                                {
                                    type: 'map',
                                    map: 'china',
                                    geoIndex: 0,
                                    aspectScale: 0.75, //长宽比
                                    showLegendSymbol: false, // 存在legend时显示
                                    label: {
                                        normal: {
                                            show: false
                                        },
                                        emphasis: {
                                            show: false,
                                            textStyle: {
                                                color: '#fff'
                                            }
                                        }
                                    },
                                    roam: true,
                                    itemStyle: {
                                        normal: {
                                            areaColor: '#F6FBFF',
                                            borderColor: '#E0E2EE',
                                        },
                                        emphasis: {
                                            areaColor: '#204AAC'
                                        }
                                    },
                                    animation: false,
                                    data: data
                                },
                                {
                                    name: '点',
                                    type: 'scatter',
                                    coordinateSystem: 'geo',
                                    symbol: 'roundRect', //气泡
                                    symbolSize: function(val) {
                                        return [50,25]
                                    },
                                    symbolOffset :[0,'-20'],
                                    label: {
                                        normal: {
                                            formatter: '{@[2]}',
                                            show: true,
                                            textStyle: {
                                                color: '#fff',
                                                fontSize: 12,
                                            }
                                        }
                                    },
                                    itemStyle: {
                                        normal: {
                                            color: 'rgba(0,0,0,0.16)', //标志颜色
                                        }
                                    },
                                    zlevel: 6,
                                    data: this.convertData(data,geoCoordMap),
                                },

                            ]
                        };
                productChart.setOption(option);
                window.addEventListener('resize', function () {
                    productChart.resize();
                })
            }
        }

    }
</script>
