<template>
  <div class="bg-fff sub-ad">
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
          共有<span class="font-20 ad-gray"> 15 </span>个大棚，
          其中<span class="font-20 ad-red"> 3 </span>个大棚发出预警，
          <span class="font-20 ad-yellow"> 6 </span>个大棚需要收获
        </div>
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
            <el-button size="mini" type="primary" round @click="goto(scope.row)">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        background
        :current-page="pagination.currentPage"
        :page-sizes="[15]"
        :page-size="15"
        layout="total, sizes, prev, pager, next"
        :total="pagination.total">
      </el-pagination>
  </div>
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
      tempData:[],
      fakeData: [{
          headIcon: '1',
          name: '大棚A-1',
          id: '431',
          classify:'strawberry',
          classifyName:'草莓',
          region:'2',
          regionName:'东二区',
          status:'grow',
          statusName:'生长',
          score:90,
        },{
          headIcon: '1',
          name: '大棚A-2',
          id: '432',
          classify:'strawberry',
          classifyName:'草莓',
          region:'2',
          regionName:'东二区',
          status:'harvest',
          statusName:'收获',
          score:50,
        },{
          headIcon: '1',
          name: '大棚A-3',
          id: '433',
          classify:'strawberry',
          classifyName:'草莓',
          region:'2',
          regionName:'东二区',
          status:'harvest',
          statusName:'收获',
          score:60,
        },{
          headIcon: '1',
          name: '大棚A-4',
          id: '434',
          classify:'strawberry',
          classifyName:'草莓',
          region:'2',
          regionName:'东二区',
          status:'warn',
          statusName:'预警',
          score:30,
        },{
          headIcon: '1',
          name: '大棚A-5',
          id: '435',
          classify:'strawberry',
          classifyName:'草莓',
          region:'2',
          regionName:'东二区',
          status:'harvest',
          statusName:'收获',
          score:90,
        },{
          headIcon: '1',
          name: '大棚B-1',
          id: '761',
          classify:'apple',
          classifyName:'苹果',
          region:'3',
          regionName:'北一区',
          status:'grow',
          statusName:'生长',
          score:60,
        },{
          headIcon: '1',
          name: '大棚B-2',
          id: '762',
          classify:'apple',
          classifyName:'苹果',
          region:'3',
          regionName:'北一区',
          status:'warn',
          statusName:'预警',
          score:90,
        },{
          headIcon: '1',
          name: '大棚B-3',
          id: '763',
          classify:'apple',
          classifyName:'苹果',
          region:'3',
          regionName:'北一区',
          status:'harvest',
          statusName:'收获',
          score:90,
        },{
          headIcon: '1',
          name: '大棚B-4',
          id: '764',
          classify:'apple',
          classifyName:'苹果',
          region:'3',
          regionName:'北一区',
          status:'harvest',
          statusName:'收获',
          score:90,
        },{
          headIcon: '1',
          name: '大棚B-5',
          id: '765',
          classify:'apple',
          classifyName:'苹果',
          region:'3',
          regionName:'北一区',
          status:'grow',
          statusName:'生长',
          score:90,
        },{
          headIcon: '1',
          name: '大棚C-1',
          id: '361',
          classify:'potato',
          classifyName:'马铃薯',
          region:'1',
          regionName:'东一区',
          status:'grow',
          statusName:'生长',
          score:90,
        },{
          headIcon: '1',
          name: '大棚C-2',
          id: '362',
          classify:'potato',
          classifyName:'马铃薯',
          region:'1',
          regionName:'东一区',
          status:'harvest',
          statusName:'收获',
          score:90,
        },{
          headIcon: '1',
          name: '大棚C-3',
          id: '363',
          classify:'potato',
          classifyName:'马铃薯',
          region:'1',
          regionName:'东一区',
          status:'warn',
          statusName:'预警',
          score:90,
        },{
          headIcon: '1',
          name: '大棚C-4',
          id: '364',
          classify:'potato',
          classifyName:'马铃薯',
          region:'1',
          regionName:'东一区',
          status:'grow',
          statusName:'生长',
          score:90,
        },{
          headIcon: '1',
          name: '大棚C-5',
          id: '365',
          classify:'potato',
          classifyName:'马铃薯',
          region:'1',
          regionName:'东一区',
          status:'grow',
          statusName:'生长',
          score:90,
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
    // debugger;
    this.$store.commit('HANDLE_NAV',this.$route.path.split('/')[2]);
    this.tableData = this.fakeData;
    this.pagination.total = this.tableData.length;
  },
  methods: {
    classifyChange(val){
      if(val !=""){
        let temp = [];
        for(let i of this.fakeData){
          if(this.form.region!='' && this.form.status!=''){
            if(i.classify==val && i.region==this.form.region && i.status==this.form.status){
              temp.push(i);
            }
          }else if(this.form.region!='' && this.form.status==''){
            if(i.classify==val && i.region==this.form.region){
              temp.push(i);
            }
          }else if(this.form.region=='' && this.form.status!=''){
            if(i.classify==val && i.status==this.form.status){
              temp.push(i);
            }
          }else{
            if(i.classify==val){
              temp.push(i);
            }
          }
        }
        this.tableData = temp;
      }else{
        let temp = [];
        for(let i of this.fakeData){
          if(this.form.region!='' && this.form.status!=''){
            if(i.region==this.form.region && i.status==this.form.status){
              temp.push(i);
            }
          }else if(this.form.region!='' && this.form.status==''){
            if(i.region==this.form.region){
              temp.push(i);
            }
          }else if(this.form.region=='' && this.form.status!=''){
            if(i.status==this.form.status){
              temp.push(i);
            }
          }else{
              temp.push(i);
          }
        }
        this.tableData = temp;
      }
      
    },
    regionChange(val){
      if(val !=""){
        let temp = [];
        for(let i of this.fakeData){
          if(this.form.classify!='' && this.form.status!=''){
            if(i.region==val && i.classify==this.form.classify && i.status==this.form.status){
              temp.push(i);
            }
          }else if(this.form.classify!='' && this.form.status==''){
            if(i.region==val && i.classify==this.form.classify){
              temp.push(i);
            }
          }else if(this.form.classify=='' && this.form.status!=''){
            if(i.region==val && i.status==this.form.status){
              temp.push(i);
            }
          }else{
            if(i.region==val){
              temp.push(i);
            }
          }
        }
        this.tableData = temp;
      }else{
        let temp = [];
        for(let i of this.fakeData){
          if(this.form.classify!='' && this.form.status!=''){
            if(i.classify==this.form.classify && i.status==this.form.status){
              temp.push(i);
            }
          }else if(this.form.classify!='' && this.form.status==''){
            if(i.classify==this.form.classify){
              temp.push(i);
            }
          }else if(this.form.classify=='' && this.form.status!=''){
            if(i.status==this.form.status){
              temp.push(i);
            }
          }else{
              temp.push(i);
          }
        }
        this.tableData = temp;
      }
        
    },
    statusChange(val){
      if(val !=""){
        let temp = [];
        for(let i of this.fakeData){
          if(this.form.region!='' && this.form.classify!=''){
            if(i.status==val && i.region==this.form.region && i.classify==this.form.classify){
              temp.push(i);
            }
          }else if(this.form.region!='' && this.form.classify==''){
            if(i.status==val && i.region==this.form.region){
              temp.push(i);
            }
          }else if(this.form.region=='' && this.form.classify!=''){
            if(i.status==val && i.classify==this.form.classify){
              temp.push(i);
            }
          }else{
            if(i.status==val){
              temp.push(i);
            }
          }
        }
        this.tableData = temp;
      }else{
        let temp = [];
        for(let i of this.fakeData){
          if(this.form.region!='' && this.form.classify!=''){
            if(i.region==this.form.region && i.classify==this.form.classify){
              temp.push(i);
            }
          }else if(this.form.region!='' && this.form.classify==''){
            if(i.region==this.form.region){
              temp.push(i);
            }
          }else if(this.form.region=='' && this.form.classify!=''){
            if(i.classify==this.form.classify){
              temp.push(i);
            }
          }else{
              temp.push(i);
          }
        }
        this.tableData = temp;
      }
    },
    //跳转页面
    goto(val){
      //加密
      let b = new Buffer(JSON.stringify(val));
      let s = b.toString('base64');
      let data = encodeURIComponent(s);
      this.$router.push({name:"greenhouse",params:{data:data}})
    },
  }
}
</script>
<style> 
</style>
