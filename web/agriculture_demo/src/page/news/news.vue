<template>
  <el-row :gutter="30" class="height100">
    <el-col :span="16" class="height100">
      <div class="sub-ad bg-fff">
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{name:'price'}">行情与预测</el-breadcrumb-item>
            <el-breadcrumb-item>最新消息</el-breadcrumb-item>
        </el-breadcrumb>
        <el-divider></el-divider>
      </div>
    </el-col>
    <el-col :span="8">
      <news-list :newList="newList"></news-list>
     </el-col>
  </el-row>
</template>

<script>
  import {getStrawberryNews} from 'service/getData'

  export default {
    name: 'news',
    data () {
      return {
      }
    },
    mounted(){
    },
    methods:{
      
    }
  }
</script>
