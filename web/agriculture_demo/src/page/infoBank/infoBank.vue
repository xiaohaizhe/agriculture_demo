<template>
   <el-row :gutter="30">
     <el-col :span="16">
       <el-container class="sub-ad bg-fff">
              <el-header height="80px">
                  <el-breadcrumb separator-class="el-icon-arrow-right">
                      <el-breadcrumb-item :to="{ name: 'infoBank' }">病虫害信息库</el-breadcrumb-item>
                      <el-breadcrumb-item >马铃薯常见病虫害</el-breadcrumb-item>
                  </el-breadcrumb>
                  <el-divider></el-divider>
              </el-header>
              <el-main>
                <el-row>
                      <el-col :span="6">
                          <ul class="ad-flex ad-flexBtw mg-top-10">
                              <li v-for="(item,index) in pramas" :key="item.id" class="paramLi" @click="pramaChange(index)">
                                  <i class="paramActive mg-right-10" :style="{'background-color':paramActive==item.id?'#FBB02F':'#fff'}"></i>{{item.name}}</li>
                          </ul>
                      </el-col>
                  </el-row>
                  <el-row v-if="paramActive==1" class="mg-top-50 mg-left-20">
                    <div>
                      <div class="ad-flex ad-flexCenter"><i class="illness ad-icon mg-right-10"></i><span class="font-18">病害</span></div>
                    </div>
                    <div>
                      <div class="ad-flex ad-flexCenter"><i class="bugs ad-icon mg-right-10"></i><span class="font-18">虫害</span></div>
                    </div>
                    
                  </el-row>
                  <el-row v-if="paramActive==2" class="mg-top-50 mg-left-20">

                  </el-row>
              </el-main>
        </el-container>
     </el-col>
     <el-col :span="8">
       <div class="bg-fff">
         <div><i class="news"></i></div>
       </div>
       
     </el-col>
   </el-row>
 
</template>

<script>
export default {
  name: 'infoBank',
  data () {
    return {
      paramActive:'1',
      pramas:[{
            name:'马铃薯见病虫害',
            id:'1',
        },{
            name:'病虫害数据库',
            id:'2'
        }]
    }
  },
  mounted(){

  },
  methods:{
     pramaChange(index){
          this.paramActive = this.pramas[index].id;
        },
  }
}
</script>
