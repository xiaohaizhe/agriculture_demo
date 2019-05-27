<template>
  <el-container class="cropManage bg-fff">
    <el-header height="220px" >
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ name: 'cropManage' }">作物管理</el-breadcrumb-item>
          <el-breadcrumb-item></el-breadcrumb-item>
        </el-breadcrumb>
        <el-divider></el-divider>
        <el-form class="ad-flex" ref="form" :model="form"  label-position="left" label-width="50px">
          <el-form-item label="名称" class="mg-right-20">
            <el-input v-model="form.name" placeholder="请输入大棚名称"></el-input>
          </el-form-item>
          <el-form-item label="分类" class="mg-right-20">
            <el-select v-model="form.classify" @change="classifyChange">
              <el-option
                v-for="item in classifyData"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="地区" class="mg-right-20">
            <el-select v-model="form.region" @change="regionChange">
              <el-option
                v-for="item in regionData"
                :key="item.value"
                :label="item.label"
                :value="item.value">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="状态" class="mg-right-20">
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
          共有<span class="font-20 ad-gray"> 45 </span>个大棚，
          其中<span class="font-20 ad-red"> 3 </span>个大棚发出预警，
          <span class="font-20 ad-yellow"> 8 </span>个大棚需要收获
        </div>
    </el-header>
    <el-main>
      <el-table :data="tableData.filter(data => !form.name || data.name.toLowerCase().includes(form.name.toLowerCase()))">
        <el-table-column prop="headIcon" label=" " width="110">
          <template slot-scope="scope">
            <i class="greenhouse ad-icon"></i>
          </template>
        </el-table-column>
        <el-table-column prop="name" label="大棚名称"></el-table-column>
        <el-table-column prop="id" label="大棚ID"></el-table-column>
        <el-table-column prop="classify" label="分类">
          <template slot-scope="scope">
            <span v-if="scope.row.classify=='potato'">马铃薯</span>
            <span v-if="scope.row.classify=='strawberry'">草莓</span>
            <span v-if="scope.row.classify=='apple'">苹果</span>
          </template>
        </el-table-column>
        <el-table-column prop="region" label="地区">
          <template slot-scope="scope">
            <span v-if="scope.row.region=='1'">东一区</span>
            <span v-if="scope.row.region=='2'">东二区</span>
            <span v-if="scope.row.region=='3'">北一区</span>
          </template>
        </el-table-column>
        <el-table-column prop="status" label="状态">
          <template slot-scope="scope">
            <span v-if="scope.row.status=='grow'">生长</span>
            <span v-if="scope.row.status=='harvest'" class="ad-yellow">收获</span>
            <span v-if="scope.row.status=='warn'" class="ad-red">预警 <i class="el-icon-warning"></i></span>
          </template>
        </el-table-column>
        <el-table-column prop="operation" label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="primary" round @click="goto()">查看</el-button>
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
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'cropManage',
  data () {
    return {
      height:'',
      pagination:{
        currentPage:1,
        total:0
      },
      form:{
        name:'',
        classify:'',
        region:'',
        status:''
      },
      tableData:[],
      fakeData: [{
          headIcon: '1',
          name: '马铃薯大棚A-1',
          id: '361',
          classify:'potato',
          region:'1',
          status:'grow'
        },{
          headIcon: '1',
          name: '马铃薯大棚A-1',
          id: '361',
          classify:'potato',
          region:'1',
          status:'harvest'
        },{
          headIcon: '1',
          name: '大棚名称2',
          id: '361',
          classify:'potato',
          region:'1',
          status:'warn'
        },{
          headIcon: '1',
          name: '大棚名称2',
          id: '361',
          classify:'strawberry',
          region:'3',
          status:'warn'
        },{
          headIcon: '1',
          name: '大棚名称',
          id: '361',
          classify:'apple',
          region:'2',
          status:'warn'
        },{
          headIcon: '1',
          name: '大棚名称',
          id: '361',
          classify:'potato',
          region:'1',
          status:'warn'
        }],
      //假数据
      classifyData:[{
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
      regionData:[{
          value: '',
          label: '全部'
        },{
          value: '1',
          label: '东一区'
        },{
          value: '2',
          label: '东二区'
        },{
          value: '3',
          label: '北一区'
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
  methods: {
    classifyChange(val){
      if(val !=""){
        let temp = [];
        for(let i of this.fakeData){
          if(i.classify==val){
              temp.push(i);
          }
        }
        this.tableData = temp;
      }else
        this.tableData = this.fakeData;
      
    },
    regionChange(val){
      if(val !=""){
        let temp = [];
        for(let i of this.fakeData){
          if(i.region==val){
              temp.push(i);
          }
        }
        this.tableData = temp;
      }else
        this.tableData = this.fakeData;
    },
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
    //跳转页面
    goto(){
      this.$router.push({name:"greenhouse"})
    },
  }
}
</script>
<style> 
</style>
