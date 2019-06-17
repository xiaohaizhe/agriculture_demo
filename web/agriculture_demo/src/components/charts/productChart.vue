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
                appleData:[{
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
                ],
                strawberryData:[{
                        name: '北京',
                        value: 1
                    },
                    // {
                    //     name: '天津',
                    //     value: 0
                    // },
                    {
                        name: '河北',
                        value: 44
                    },{
                        name: '山西',
                        value: 1
                    },
                    {
                        name: '内蒙古',
                        value: 1
                    },
                    {
                        name: '辽宁',
                        value: 42
                    },{
                        name: '吉林',
                        value: 2
                    },
                    {
                        name: '黑龙江',
                        value: 3
                    },
                    {
                        name: '上海',
                        value: 2
                    },{
                        name: '江苏',
                        value: 46
                    },
                    {
                        name: '浙江',
                        value: 14
                    },
                    {
                        name: '安徽',
                        value: 46
                    },{
                        name: '福建',
                        value: 3
                    },
                    {
                        name: '江西',
                        value: 2
                    },
                    {
                        name: '山东',
                        value: 69
                    },{
                        name: '河南',
                        value: 21
                    },
                    {
                        name: '湖北',
                        value: 5
                    },
                    {
                        name: '湖南',
                        value: 7
                    },{
                        name: '广东',
                        value: 3
                    },
                    {
                        name: '广西',
                        value: 1
                    },
                    // {
                    //     name: '海南',
                    //     value: 0
                    // },
                    {
                        name: '重庆',
                        value: 2
                    },
                    {
                        name: '四川',
                        value: 11
                    },{
                        name: '贵州',
                        value: 3
                    },
                    {
                        name: '云南',
                        value: 2
                    },
                    // {
                    //     name: '西藏',
                    //     value: 0
                    // },
                    {
                        name: '陕西',
                        value: 8
                    },
                    {
                        name: '甘肃',
                        value: 2
                    },
                    // {
                    //     name: '青海',
                    //     value: 0
                    // },
                    // {
                    //     name: '宁夏',
                    //     value: 0
                    // },
                    {
                        name: '新疆',
                        value: 3
                    }]
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
            drawChart(type){
                let data= {}
                if(type=="apple"){
                    data=this.appleData;
                }else{
                    data= this.strawberryData;
                }
                var geoCoordMap = {
                    '新疆': [86.61 , 40.79],
                    '西藏':[89.13 , 30.66],
                    '黑龙江':[128.34 , 47.05],
                    '吉林':[126.32 , 43.38],
                    '辽宁':[123.42 , 41.29],
                    '内蒙古':[112.17 , 42.81],
                    '北京':[116.40 , 40.40 ],
                    '宁夏':[106.27 , 36.76],
                    '山西':[111.95,37.65],
                    '河北':[115.21 , 38.44],
                    '天津':[117.04 , 39.52],
                    '青海':[97.07 , 35.62],
                    '甘肃':[103.82 , 36.05],
                    '山东':[118.01 , 36.37],
                    '陕西':[108.94 , 34.46],
                    '河南':[113.46 , 34.25],
                    '安徽':[117.28 , 31.86],
                    '江苏':[120.26 , 32.54],
                    '上海':[121.46 , 31.28],
                    '四川':[103.36 , 30.65],
                    '湖北':[112.29 , 30.98],
                    '浙江':[120.15 , 29.28],
                    '重庆':[107.51 , 29.63],
                    '湖南':[112.08 , 27.79],
                    '江西':[115.89 , 27.97],
                    '贵州':[106.91 , 26.67],
                    '福建':[118.31 , 26.07],
                    '云南':[101.71 , 24.84],
                    '台湾':[121.01 , 23.54],
                    '广西':[108.67 , 23.68],
                    '广东':[113.98 , 22.82],
                    '海南':[110.03 , 19.33],
                    '澳门':[113.54 , 22.19],
                    '香港':[114.17 , 22.32]
                }
                var max = 100000,
                    min = 900; // todo 
                var maxSize4Pin = 100,
                    minSize4Pin = 20;
                let productChart = this.$echarts.init(document.getElementById(this.chartId));
                let option = {
                            tooltip: {
                                trigger: 'item',
                                formatter: function(params) {
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
