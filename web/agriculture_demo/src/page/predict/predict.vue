<template>
  <el-row :gutter="30" class="height100">
    <el-col :span="16" class="height100">
      <div class="sub-ad bg-fff">
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{name:'price'}">行情与预测</el-breadcrumb-item>
            <el-breadcrumb-item>{{vegetable.name}}</el-breadcrumb-item>
        </el-breadcrumb>
        <el-divider></el-divider>
        <el-row v-if="this.analyseActive!='news'">
            <el-col :span="24">
                <ul class="ad-flex ad-flexEnd mg-top-10 ">
                    <li v-for="(item,index) in pramas" :key="item.routeId" class="paramLi mg-right-10" @click="pramaChange(index)">
                        <i class="paramActive mg-right-10" :style="{'background-color':paramActive==item.id?'#FBB02F':'#fff'}"></i>{{item.name}}</li>
                </ul>
                <ul class="ad-flex ad-flexEnd mg-top-20" style="padding-left:20px">
                    <li v-for="(item,index) in analyses" :class="{analyseActive:analyseActive==item.id}" :key="item.id" class="paramLi mg-right-10" style="margin:15px 30px 15px 0" @click="analyseChange(index)" >{{item.name}}</li>
                </ul>
            </el-col>
        </el-row>
        <router-view></router-view>
      </div>
    </el-col>
    <el-col :span="8">
      <news-list :newList="newList"></news-list>
     </el-col>
  </el-row>
    
</template>

<script>
import {getStrawberryNews} from 'service/getData'
import {mapState} from 'vuex'
import newsList from 'components/newsList/newsList'

export default {
  name: 'predict',
  data () {
    return {
      paramActive:'apple',
      activeName:'苹果',
      analyseActive:'price',
      newList:[],
      pramas:[{
          name:'苹果',
          id:'apple'
        },{
          name:'草莓',
          id:'strawberry'
        },{
          name:'青椒',
          id:'pepper'
        }],
      analyses:[{
        name:'价格',
        id:'price'
      },{
        name:'供需',
        id:'supply'
      },{
        name:'行业预测',
        id:'forecast'
      }]
    }
  },
  components:{
      'news-list':newsList
  },
  computed:{
      ...mapState([
          'vegetable'
      ])
  },
  mounted(){
    
    this.paramActive = this.vegetable.id;
    if(this.paramActive=='strawberry'){
      this.getStrawberryNews();
    }
    this.analyseActive = this.$route.name;
  },
  methods:{
    pramaChange(index){
      this.paramActive = this.pramas[index].id;
      if(this.paramActive=='strawberry'){
        this.getStrawberryNews();
      }
      this.$store.commit('HANDLE_VG',this.pramas[index]);
      this.$router.push({path:'/index/predict/'+this.analyseActive});
    },
    analyseChange(index){
      this.analyseActive = this.analyses[index].id;
      this.$router.push({path:'/index/predict/'+this.analyses[index].id});
    },
    async getStrawberryNews(){
        let resp = await getStrawberryNews();
        if(resp.code==0){
            this.newList = resp.data;
        }
    },
    //跳转页面
    goto(val){
      this.activeName = '最新消息';
      this.analyseActive = 'news';
      this.$store.commit('HANDLE_VG',{name:'最新消息',id:'news'});
      this.$router.push({name:val});
    },
  }
}
</script>
