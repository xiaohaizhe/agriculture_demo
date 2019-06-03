<template>
   <div class="sub-ad bg-fff">
            <el-breadcrumb separator-class="el-icon-arrow-right">
                <el-breadcrumb-item :to="{ name: 'cropManage' }">作物管理</el-breadcrumb-item>
                <el-breadcrumb-item :to="{ name: 'greenhouse' }">马铃薯大棚A-1</el-breadcrumb-item>
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
                该大棚已种植 <span class="font-20 ad-gray mg-right-5 mg-left-5"> 20 </span> 批次，
                已收获 <span class="font-20 ad-gray mg-right-5 mg-left-5"> 19 </span> 批次
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
        tableData:[],
        pagination:{
            currentPage:1,
            total:0
        },
        fakeData: [{
            plantTime: '2018/04/21',
            batch: '马铃薯大棚A-1',
            harvestTime: '2018/08/01',
            crops:'potato',
            variety:'品种',
            status:'grow'
            },{
            plantTime: '2018/04/21',
            batch: '马铃薯大棚A-1',
            harvestTime: '2018/08/01',
            crops:'potato',
            variety:'品种',
            status:'grow'
            },{
            plantTime: '2018/04/21',
            batch: '马铃薯大棚A-1',
            harvestTime: '2018/08/01',
            crops:'potato',
            variety:'品种',
            status:'harvest'
            },{
            plantTime: '2018/04/21',
            batch: '马铃薯大棚A-1',
            harvestTime: '2018/08/01',
            crops:'potato',
            variety:'品种',
            status:'harvest'
            },{
            plantTime: '2018/04/21',
            batch: '草莓大棚A-1',
            harvestTime: '2018/08/01',
            crops:'strawberry',
            variety:'品种',
            status:'warn',
            statusTimes:'2'
            },{
            plantTime: '2018/04/21',
            batch: '马铃薯大棚A-1',
            harvestTime: '2018/08/01',
            crops:'potato',
            variety:'品种',
            status:'warn',
            statusTimes:'1'
            },{
            plantTime: '2018/04/21',
            batch: '草莓大棚A-1',
            harvestTime: '2018/08/01',
            crops:'strawberry',
            variety:'品种',
            status:'warn',
            statusTimes:'2'
            },{
            plantTime: '2018/04/21',
            batch: '马铃薯大棚A-1',
            harvestTime: '2018/08/01',
            crops:'potato',
            variety:'品种',
            status:'warn',
            statusTimes:'1'
            },{
            plantTime: '2018/04/21',
            batch: '草莓大棚A-1',
            harvestTime: '2018/08/01',
            crops:'strawberry',
            variety:'品种',
            status:'warn',
            statusTimes:'2'
            },{
            plantTime: '2018/04/21',
            batch: '马铃薯大棚A-1',
            harvestTime: '2018/08/01',
            crops:'potato',
            variety:'品种',
            status:'warn',
            statusTimes:'1'
            },{
            plantTime: '2018/04/21',
            batch: '草莓大棚A-1',
            harvestTime: '2018/08/01',
            crops:'strawberry',
            variety:'品种',
            status:'warn',
            statusTimes:'2'
            },{
            plantTime: '2018/04/21',
            batch: '马铃薯大棚A-1',
            harvestTime: '2018/08/01',
            crops:'potato',
            variety:'品种',
            status:'warn',
            statusTimes:'1'
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
      this.tableData = this.fakeData;
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
