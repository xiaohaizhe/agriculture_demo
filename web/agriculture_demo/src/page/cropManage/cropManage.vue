<template>
  <div>
      <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item :to="{ name: 'cropManage' }">作物管理</el-breadcrumb-item>
          <el-breadcrumb-item></el-breadcrumb-item>
        </el-breadcrumb>
        <el-divider></el-divider>
        <div>
          <el-form class="ad-flex" ref="form" :model="form" label-width="80px">
            <el-form-item label="名称">
              <el-input v-model="form.name" placeholder="请输入大棚名称"></el-input>
            </el-form-item>
            <el-form-item label="分类">
              <el-select v-model="form.classify">
                <el-option
                  v-for="item in classifyData"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="地区">
              <el-select v-model="form.region">
                <el-option
                  v-for="item in regionData"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="状态">
              <el-select v-model="form.status">
                 <el-option
                  v-for="item in statusData"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-form>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'cropManage',
  data () {
    return {
      form:{
        name:'',
        classify:'',
        region:'',
        status:''
      },
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
        value: 'potato',
        label: '生长'
      },{
        value: 'harvest',
        label: '收获'
      },{
        value: 'warn',
        label: '预警'
      }]
    }
  }
}
</script>
