<template>
    <el-container class="sub-ad">
        <el-header height="80px">
            <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ name: 'cropManage' }">作物管理</el-breadcrumb-item>
            <el-breadcrumb-item> 马铃薯大棚A-1</el-breadcrumb-item>
            </el-breadcrumb>
            <el-divider></el-divider>
        </el-header>
        <el-main>
            <el-row :gutter="60">
                <el-col :span="16">
                    <div>
                        <p class="mg-bot-20">作物生长状态</p>
                        <el-row>
                            <el-col :span="6">
                                <ul class="score ad-flex ad-flexCenter ad-justifyCenter">
                                    <li class="font-60">35</li>
                                    <li style="margin:10px 0"><i class="star ad-icon mg-right-10"></i><span class="font-12 ad-white">综合评分</span></li>
                                    <li class="font-12 ad-white">备注：满分100</li>
                                </ul>
                            </el-col>
                            <el-col :span="18">
                                <area-chart chartId="statusChart"></area-chart>
                            </el-col>
                        </el-row>
                        <el-row class="mg-bot-20 mg-top-20">
                            <span class="mg-right-20">大棚环境参数</span>
                            <el-select v-model="param" @change="paramChange">
                                <el-option
                                    v-for="item in params"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                </el-option>
                            </el-select>
                            <i class="el-icon-question ad-green font-18"></i>
                        </el-row>
                        <el-row class="envParam">
                            <div class="ad-flex ad-flexCenter mg-bot-10 mg-right-20" v-for="item,index in envParams" :key="item.name">
                                <p style="width:90px" :style="{'color': item.value<=70 && item.value>=30?'':'#CF0505'}">{{item.name}}</p>
                                <el-progress :percentage="item.value" :show-text="false" class="mg-right-20" :color="item.value<=70 && item.value>=30?'#02C1A7':'#CF0505'"></el-progress>
                                <p class="text ad-red" v-if="item.value>70">高</p>
                                <p class="text ad-red" v-if="item.value<30">低</p>
                                <p class="text ad-gray" v-if="item.value<=70 && item.value>=30">适合</p>
                            </div>
                            <el-button type="text" class="ad-gray textRight mg-right-20">查看更多></el-button>
                        </el-row>
                        <el-row class="notice">
                            <span class="mg-right-20">生长状态：出现病虫害</span><el-button size="mini" type="primary" round class="mg-bot-10">查看</el-button>
                            <p class="mg-bot-10">大棚环境：根据环境参数，有XX%几率会出现XXX病虫害</p>
                            <p class="mg-bot-10">解决办法：建议修改大棚环境模式二</p>
                        </el-row>
                    </div>
                </el-col>
                <el-col :span="8">
                    <div>
                        <p class="mg-bot-20">大棚基本信息</p>
                        <div class="greenhousePic ad-icon mg-bot-20"></div>
                        <ul>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">名称：</p>马铃薯大棚A-1</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">大棚ID：</p>1212</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">分类：</p>马铃薯</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">地区：</p>三鲜农业种植场北三</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">状态：</p>开花期</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">创建时间：</p>2019/01/18</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">大棚介绍：</p><span>该大棚主要用于种植马铃薯，已是2019年第三期种植内容已是2019年第三期种植内容已是2019年第三期种植内容已是2019年第三期种植内容。</span></li>
                        </ul>
                    </div>
                </el-col>
            </el-row>
            
        </el-main>
    </el-container>
</template>

<script>
    import areaChart from 'components/charts/areaChart'
    

    export default {
        name: 'greenhouse',
        data () {
            return {
                param:'',
                params:[{
                    value: 'MOFOST',
                    label: 'MOFOST'
                    },{
                    value: 'ORYZA',
                    label: 'ORYZA'
                    },{
                    value: 'APSIM',
                    label: 'APSIM'
                    },{
                    value: 'EPIC',
                    label: 'EPIC'
                    },{
                    value: 'CERES',
                    label: 'CERES'
                    },{
                    value: 'RCSODS',
                    label: 'RCSODS'
                    }],
                envParams:[{
                        name:'土壤温度',
                        value:50
                    },{
                        name:'土壤水分',
                        value:60
                    },{
                        name:'土壤盐分',
                        value:80
                    },{
                        name:'土壤PH值',
                        value:20
                    },{
                        name:'土壤氮含量',
                        value:30
                    },{
                        name:'土壤磷含量',
                        value:40
                    },{
                        name:'环境温度',
                        value:90
                    },{
                        name:'棚内光照',
                        value:10
                    },{
                        name:'二氧化碳',
                        value:55
                    }]
            }
        },
        components:{
            'area-chart':areaChart
        },
        methods:{
            paramChange(val){

            }
        }
    }
</script>
