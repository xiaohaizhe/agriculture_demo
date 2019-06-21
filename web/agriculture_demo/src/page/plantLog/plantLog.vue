<template>
   <div class="sub-ad bg-fff">
            <el-breadcrumb separator-class="el-icon-arrow-right">
                <el-breadcrumb-item :to="{ name: 'cropManage' }">数字化种植</el-breadcrumb-item>
                <el-breadcrumb-item :to="{ name: 'greenhouse' ,pramas:{data:secretGh}}">{{greenhouse.name}}</el-breadcrumb-item>
                <el-breadcrumb-item>种植记录</el-breadcrumb-item>
            </el-breadcrumb>
            <el-divider></el-divider>
            <el-form class="ad-flex" ref="form" :model="form"  label-position="left" label-width="80px">
                <el-form-item label="种植日期" class="mg-right-20">
                    <el-date-picker
                        v-model="form.plantTime"
                        type="daterange"
                        range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="收获日期" class="mg-right-20">
                    <el-date-picker
                        v-model="form.harvestTime"
                        type="daterange"
                        range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期">
                    </el-date-picker>
                </el-form-item>
                <el-form-item label="种植作物" class="mg-right-20">
                    <el-select v-model="form.crops" @change="cropsChange">
                        <el-option
                            v-for="item in cropsData"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                        </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="历史状态" class="mg-right-20">
                    <el-select v-model="form.status" @change="statusChange">
                    <el-option
                        v-for="item in statusData"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                    </el-select>
                </el-form-item>
            </el-form>
            <div class="crop-sum ad-flex ad-flexCenter ad-justifyCenter">
                <i class="analysis ad-icon mg-right-10"></i>
                该大棚已种植 <span class="font-20 ad-gray mg-right-5 mg-left-5"> 5 </span> 批次，
                已收获 <span class="font-20 ad-gray mg-right-5 mg-left-5"> 2 </span> 批次
            </div>
            <el-table :data="tableData.filter(data => !form.name || data.name.toLowerCase().includes(form.name.toLowerCase()))">
                <el-table-column prop="plantTime" label="种植时间"></el-table-column>
                <el-table-column prop="batch" label="种植批次"></el-table-column>
                <el-table-column prop="crops" label="种植作物">
                    <template slot-scope="scope">
                        <span v-if="scope.row.crops=='potato'">马铃薯</span>
                        <span v-if="scope.row.crops=='strawberry'">草莓</span>
                        <span v-if="scope.row.crops=='apple'">苹果</span>
                    </template>
                </el-table-column>
                <el-table-column prop="variety" label="作物品种"></el-table-column>
                <el-table-column prop="harvestTime" label="收获时间"></el-table-column>
                <el-table-column prop="status" label="作物历史状态">
                    <template slot-scope="scope">
                        <span v-if="scope.row.status=='grow'">生长</span>
                        <span v-if="scope.row.status=='harvest'">收获</span>
                        <span v-if="scope.row.status=='warn'">预警{{scope.row.statusTimes}}次</span>
                    </template>
                </el-table-column>
            </el-table>
            <el-pagination
                background
                :current-page="pagination.currentPage"
                :page-sizes="[10]"
                :page-size="10"
                layout="total, sizes, prev, pager, next"
                :total="pagination.total">
            </el-pagination>
    </div>
</template>

<script>
export default {
  name: 'plantLog',
  data () {
    return {
        form:{
            plantTime:'',
            harvestTime:'',
            crops:'',
            status:''
        },
        secretGh:'',
        greenhouse:{},
        tableData:[],
        pagination:{
            currentPage:1,
            total:0
        },
        fakeData:[],
        fakeData1: [{
            plantTime: '2018/10/21',
            batch: '批次1',
            harvestTime: '2019/02/01',
            crops:'strawberry',
            variety:'硕丰',
            status:'harvest'
            },{
            plantTime: '2019/11/01',
            batch: '批次2',
            harvestTime: '2019/02/20',
            crops:'strawberry',
            variety:'明晶',
            status:'harvest'
            },{
            plantTime: '2019/04/21',
            batch: '批次3',
            harvestTime: '-',
            crops:'strawberry',
            variety:'明旭',
            status:'grow'
            },{
            plantTime: '2019/05/01',
            batch: '批次4',
            harvestTime: '-',
            crops:'strawberry',
            variety:'戈雷拉',
            status:'grow'
            },{
            plantTime: '2019/05/21',
            batch: '批次5',
            harvestTime: '-',
            crops:'strawberry',
            variety:'白草莓',
            status:'warn',
            statusTimes:'2'
            }],
        fakeData2: [{
            plantTime: '2018/10/21',
            batch: '批次1',
            harvestTime: '2019/02/01',
            crops:'apple',
            variety:'红富士',
            status:'harvest'
            },{
            plantTime: '2019/11/01',
            batch: '批次2',
            harvestTime: '2019/02/20',
            crops:'apple',
            variety:'黄元帅',
            status:'harvest'
            },{
            plantTime: '2019/04/21',
            batch: '批次3',
            harvestTime: '-',
            crops:'apple',
            variety:'嘎拉',
            status:'grow'
            },{
            plantTime: '2019/05/01',
            batch: '批次4',
            harvestTime: '-',
            crops:'apple',
            variety:'国光',
            status:'grow'
            },{
            plantTime: '2019/05/21',
            batch: '批次5',
            harvestTime: '-',
            crops:'apple',
            variety:'红星',
            status:'warn',
            statusTimes:'2'
            }],
        fakeData3: [{
            plantTime: '2018/10/21',
            batch: '批次1',
            harvestTime: '2019/02/01',
            crops:'potato',
            variety:'早大白',
            status:'harvest'
            },{
            plantTime: '2019/11/01',
            batch: '批次2',
            harvestTime: '2019/02/20',
            crops:'potato',
            variety:'超白',
            status:'harvest'
            },{
            plantTime: '2019/04/21',
            batch: '批次3',
            harvestTime: '-',
            crops:'potato',
            variety:'黄麻子',
            status:'grow'
            },{
            plantTime: '2019/05/01',
            batch: '批次4',
            harvestTime: '-',
            crops:'potato',
            variety:'尤金',
            status:'grow'
            },{
            plantTime: '2019/05/21',
            batch: '批次5',
            harvestTime: '-',
            crops:'potato',
            variety:'中薯2号',
            status:'warn',
            statusTimes:'2'
            }],
        cropsData:[{
            value: '',
            label: '全部'
            },{
            value: 'potato',
            label: '马铃薯'
            },{
            value: 'strawberry',
            label: '草莓'
            },{
            value: 'apple',
            label: '苹果'
            }],
        statusData:[{
            value: '',
            label: '全部'
            },{
            value: 'grow',
            label: '生长'
            },{
            value: 'harvest',
            label: '收获'
            },{
            value: 'warn',
            label: '预警'
            }]
    }
  },
  mounted(){
        this.$store.commit('HANDLE_NAV',this.$route.path.split('/')[2]);
        //解密
        var x = new Buffer(decodeURIComponent(this.$route.params.data), 'base64')
        var y = x.toString('utf8');
        this.secretGh = y;
        this.greenhouse = JSON.parse(y);
        if(this.greenhouse.classify=='apple'){
            this.fakeData = this.fakeData2;
        }else if(this.greenhouse.classify=='strawberry'){
            this.fakeData = this.fakeData1;
        }else {
            this.fakeData = this.fakeData3;
        }
        this.tableData=this.fakeData;
        this.pagination.total = this.tableData.length;
  },
  methods:{
        statusChange(val){
            if(val !=""){
                let temp = [];
                for(let i of this.fakeData){
                if(i.status==val){
                    temp.push(i);
                }
                }
                this.tableData = temp;
            }else
                this.tableData = this.fakeData;
        },
        cropsChange(val){
            if(val !=""){
                let temp = [];
                for(let i of this.fakeData){
                if(i.crops==val){
                    temp.push(i);
                }
                }
                this.tableData = temp;
            }else
                this.tableData = this.fakeData;
        }
  }
}
</script>
