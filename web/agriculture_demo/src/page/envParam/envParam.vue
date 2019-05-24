<template>
  <el-container class="sub-ad">
        <el-header height="80px">
            <el-breadcrumb separator-class="el-icon-arrow-right">
                <el-breadcrumb-item :to="{ name: 'cropManage' }">作物管理</el-breadcrumb-item>
                <el-breadcrumb-item :to="{ name: 'greenhouse' }">马铃薯大棚A-1</el-breadcrumb-item>
                <el-breadcrumb-item>大棚环境参数</el-breadcrumb-item>
            </el-breadcrumb>
            <el-divider></el-divider>
        </el-header>
        <el-main>
            <el-form class="ad-flex" ref="form" :model="form"  label-position="left" label-width="50px">
                <el-form-item label="大棚" class="mg-right-20">
                    <el-select v-model="form.greenhouse">
                    <el-option
                        v-for="item in ghData"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                    </el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="日期" class="mg-right-20">
                    <el-date-picker
                        v-model="form.time"
                        type="daterange"
                        range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期">
                    </el-date-picker>
                </el-form-item>
            </el-form>
            <el-row>
                <el-col :span="16" style="margin-left: 55px;">
                    <ul class="ad-flex ad-flexBtw mg-top-10">
                        <li v-for="item,index in pramas" :key="item.id" class="paramLi" @click="pramaChange(index)"><i class="paramActive mg-right-10" :style="{'background-color':paramActive==index?'#FBB02F':'#fff'}"></i>{{item.name}}</li>
                    </ul>
                </el-col>
            </el-row>
            
        </el-main>
    </el-container>
</template>

<script>
export default {
  name: 'envParam',
  data () {
    return {
        paramActive:1,
        form:{
            greenhouse:'1',
            time:''
        },
        pramas:[{
                name:'环境温度',
                id:0
            },{
                name:'棚内光照',
                id:1
            },{
                name:'二氧化碳',
                id:2
            },{
                name:'土壤温度',
                id:3
            },{
                name:'土壤水分',
                id:4
            },{
                name:'土壤盐分',
                id:5
            },{
                name:'土壤PH值',
                id:6
            },{
                name:'土壤氮含量',
                id:7
            },{
                name:'土壤磷含量',
                id:8
            }],
        ghData:[{
            value:'1',
            label:'马铃薯大棚A-1'
            },{
                value:'2',
                label:'马铃薯大棚A-2'
            },{
                value:'3',
                label:'马铃薯大棚A-3'
            }]
    }
  },
  methods:{
      pramaChange(index){
          this.paramActive = index;
      }
  }
}
</script>
<style>
    .paramActive{
        width: 10px;
        height: 10px;
        display: inline-block;
        border-radius: 50%;
    }
    .paramLi{
        cursor: pointer;
        text-align:right;
    }
</style>