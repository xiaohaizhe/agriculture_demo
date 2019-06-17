<template>
    <div class="sub-ad bg-fff">
            <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ name: 'cropManage' }">作物管理</el-breadcrumb-item>
            <el-breadcrumb-item>{{greenhouse.name}}</el-breadcrumb-item>
            </el-breadcrumb>
            <el-divider></el-divider>
            <el-row :gutter="60">
                <el-col :span="16">
                    <div>
                        <p class="mg-bot-20">作物生长状态</p>
                        <el-row>
                            <el-col :span="6">
                                <ul class="score ad-flex ad-flexCenter ad-justifyCenter">
                                    <li class="font-60">{{greenhouse.score}}</li>
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
                            <el-select v-model="param" @change="paramChange($event,param)">
                                <el-option
                                    v-for="item in params"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                                </el-option>
                            </el-select>
                            <el-popover
                                placement="right"
                                width="800"
                                trigger="click">
                                <div>
                                    <h3 class="ad-yellow">WOFOST</h3>
                                    <p class="ad-gray font-12 mg-bot-20">（WOrld FOod STudies)是用以模拟一年收作物的生长期和收获期的模型。该模型根据光合作用，呼吸作用等基础过程来解释作物生长，并且分析这些过程是如何受到环境条件的影响的。WOFOST根据土壤类型、作物类型、天气数据和作物管理因素（例如播种日期）的知识来计算可获得的作物产量等相关信息。该模型被世界上很多研究人员使用，并在各种气候和管理条件下应用于许多作物。此外，WOFOST的作物生长监测系统被用于监测欧洲的可耕作物，并对当前生长季节进行作物产量预测。</p>
                                    <h3 class="ad-yellow">APSIM</h3>
                                    <p class="ad-gray font-12 mg-bot-20">APSIM是澳大利亚生产系统研究组开发的一种具有模块化结构的作物生产系统模拟器。其功能是分析在不同气候背景条件下，耕作系统的生产力和作物的水肥资源利用，以及水分平衡的变化。该模型的特点是通过控制系统可以进行农业生产管理方式的设置，入品种使用、播种期、灌溉与施肥的时间以及总量、休闲和轮作等等。模型可以进行多年连续模拟，用来分析长期气候波动和气候变化对农田生态系统的影响。主要特色有：对于极端环境变化条件下预测产量变化和经济风险分析具有充分的敏感性；对于干旱地区作物水分关系具有较强的分析能力；可以模拟在作物轮作、间作及留茬等决策管理影响下土壤的生产能力和腐朽趋势；模型体系庞大，适用范围广，可模拟物种数目众多。</p>
                                    <h3 class="ad-yellow">CERES</h3>
                                    <p class="ad-gray font-12 mg-bot-20">CERES模型综合考虑的气象因子、土壤水分和土壤氮素对作物生长的影响，模拟的环境条件已经基本接近作物生长的实际环境条件，注重作物的个性，能完整的描述和预测特定作物的生长及产量形成的整体特点。但在作物生理生态过程模拟方面仍然比较简单，其结构性、激励性、适用性有待进一步加强和提高。</p>
                                </div>
                                <i class="el-icon-question ad-green font-18" slot="reference"></i>
                            </el-popover>
                        </el-row>
                        <el-row class="envParam">
                            <div class="ad-flex ad-flexCenter mg-bot-10 mg-right-20" v-for="item in envParams" :key="item.name">
                                <p style="width:90px" :style="{'color': item.value<=70 && item.value>=30?'':'#CF0505'}">{{item.name}}</p>
                                <el-progress :percentage="item.value" :show-text="false" class="mg-right-20" :color="item.value<=70 && item.value>=30?'#02C1A7':'#CF0505'"></el-progress>
                                <p class="text ad-red" v-if="item.value>70">高</p>
                                <p class="text ad-red" v-if="item.value<30">低</p>
                                <p class="text ad-gray" v-if="item.value<=70 && item.value>=30">适合</p>
                            </div>
                            <el-button type="text" class="ad-gray textRight mg-right-20" @click="goto('envParam')">查看更多></el-button>
                        </el-row>
                        <el-row class="notice">
                            <span class="mg-right-20">生长状态：出现病虫害</span><el-button size="mini" type="primary" round class="mg-bot-10" @click="goto('knowledgeBase')">查看</el-button>
                            <p class="mg-bot-10">大棚环境：{{analysis}}</p>
                            <p class="mg-bot-10">解决办法：{{advice}}</p>
                        </el-row>
                    </div>
                </el-col>
                <el-col :span="8">
                    <div>
                        <p class="mg-bot-20">大棚基本信息</p>
                        <div class="greenhousePic ad-icon mg-bot-20"></div>
                        <ul>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">名称：</p>{{greenhouse.name}}</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">大棚ID：</p>{{greenhouse.id}}</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">分类：</p>{{greenhouse.classifyName}}</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">地区：</p>{{greenhouse.regionName}}</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">状态：</p>{{greenhouse.statusName}}</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">创建时间：</p>2019/05/18</li>
                            <li class="ad-flex mg-bot-10"><p class="gh-text">大棚介绍：</p><span>暂无介绍</span></li>
                        </ul>
                        <el-button type="primary" round style="margin: 20px auto;display: block;" @click="goto('plantLog')">查看种植记录</el-button>
                    </div>
                </el-col>
            </el-row>
    </div>
</template>

<script>
    import areaChart from 'components/charts/areaChart'
    

    export default {
        name: 'greenhouse',
        data () {
            return {
                greenhouse:{},
                oldParam:'',
                param:'1',
                analysis:'环境参数中水分较低，植物会出现干燥脱水。',
                advice:'根据环境参数，建议多给大棚浇水！',
                params:[{
                    value: '1',
                    label: 'WOFOST'
                    },{
                    value: '2',
                    label: 'ORYZA'
                    },{
                    value: '3',
                    label: 'APSIM'
                    },{
                    value: '4',
                    label: 'EPIC'
                    },{
                    value: '5',
                    label: 'CERES'
                    },{
                    value: '6',
                    label: 'RCSODS'
                    }],
                envParams:[],
                fakeEnv1:[{
                        name:'土壤温度',
                        value:50
                    },{
                        name:'土壤水分',
                        value:10
                    },{
                        name:'土壤盐分',
                        value:70
                    },{
                        name:'土壤PH值',
                        value:40
                    },{
                        name:'土壤氮含量',
                        value:30
                    },{
                        name:'土壤磷含量',
                        value:40
                    },{
                        name:'环境温度',
                        value:60
                    },{
                        name:'棚内光照',
                        value:40
                    },{
                        name:'二氧化碳',
                        value:55
                    }],
                fakeEnv2:[{
                        name:'土壤温度',
                        value:60
                    },{
                        name:'土壤水分',
                        value:70
                    },{
                        name:'土壤盐分',
                        value:90
                    },{
                        name:'土壤PH值',
                        value:30
                    },{
                        name:'土壤氮含量',
                        value:20
                    },{
                        name:'土壤磷含量',
                        value:30
                    },{
                        name:'环境温度',
                        value:100
                    },{
                        name:'棚内光照',
                        value:50
                    },{
                        name:'二氧化碳',
                        value:40
                    }],
                fakeEnv3:[{
                        name:'土壤温度',
                        value:10
                    },{
                        name:'土壤水分',
                        value:5
                    },{
                        name:'土壤盐分',
                        value:30
                    },{
                        name:'土壤PH值',
                        value:90
                    },{
                        name:'土壤氮含量',
                        value:60
                    },{
                        name:'土壤磷含量',
                        value:30
                    },{
                        name:'环境温度',
                        value:20
                    },{
                        name:'棚内光照',
                        value:90
                    },{
                        name:'二氧化碳',
                        value:20
                    }],
            }
        },
        components:{
            'area-chart':areaChart
        },
        mounted(){
             //解密
            var x = new Buffer(decodeURIComponent(this.$route.params.data), 'base64')
            var y = x.toString('utf8');
            this.greenhouse = JSON.parse(y);
            this.envParams = this.fakeEnv1;
        },
        watch:{
            param(curVal,oldVal){
                this.oldParam = oldVal;
    　　　},
        },
        methods:{
            paramChange(val){
                this.$confirm('更改大棚环境模式后，大棚内参数将自动修改对应模式参数，且将会影响大棚内作物生长。请确认是否修改大棚模式？', '', {
                    confirmButtonText: '确定',
                    confirmButtonClass:'is-round',
                    cancelButtonClass:'is-round',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    switch(val){
                        case '1' :this.envParams = this.fakeEnv1;this.analysis="环境参数中水分较低，植物会出现干燥脱水。";this.advice="根据环境参数，建议多给大棚浇水！";break;
                        case '2' :this.envParams = this.fakeEnv2;this.analysis="环境参数中温度较高，植物生长缓慢,叶子将干枯掉落,甚至可能会出现死亡。";this.advice="根据环境参数，建议降低大棚温度！";break;
                        case '3' :this.envParams = this.fakeEnv3;this.analysis="环境参数中多重预警。";this.advice="建议修改大棚环境模式!";break;
                        case '4' :this.envParams = this.fakeEnv2;this.analysis="环境参数中温度较高，植物生长缓慢,叶子将干枯掉落,甚至可能会出现死亡。";this.advice="根据环境参数，建议降低大棚温度！";break;
                        case '5' :this.envParams = this.fakeEnv1;this.analysis="环境参数中水分较低，植物会出现干燥脱水。";this.advice="根据环境参数，建议多给大棚浇水！";break;
                        case '6' :this.envParams = this.fakeEnv3;this.analysis="环境参数中多重预警。";this.advice="建议修改大棚环境模式!";break;
                    }
                }).catch(() => {
                    this.param = this.oldParam;   
                });
            },
            //跳转页面
            goto(name){
                this.$router.push({name:name});
            },
        }
    }
</script>
