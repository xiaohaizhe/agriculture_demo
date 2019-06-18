<template>
  <el-row :gutter="30" class="height100">
    <el-col :span="16" class="height100">
      <div class="sub-ad bg-fff">
        <div class="ad-flex ad-flexCenter ad-flexBtw">
          <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{name:'price'}">行情与预测</el-breadcrumb-item>
            <el-breadcrumb-item>最新消息</el-breadcrumb-item>
          </el-breadcrumb>
          <div>
            <el-button type="text" class="ad-black" @click="changeNews(number-1)">上一条</el-button>
            <el-button type="text" class="ad-black" @click="changeNews(number+1)">下一条</el-button>
          </div>
        </div>
        
        <el-divider></el-divider>
        <div  class="textCenter" style="padding: 0 10%;">
          <p class="font-24 mg-bot-10">{{news.title}}</p>
          <p class="font-18 mg-bot-10">{{news.source}}</p>
          <p class="mg-bot-10">{{news.author}} {{news.date}}</p>
          <p v-for="item in news.content" :key="item._id" class="textLeft mg-bot-10">{{item}}</p>
          <img v-for="item in news.images" :key="item" :src="item"/>
        </div>
      </div>
    </el-col>
    <el-col :span="8">
      <news-list :newList="newList" @changeNews="changeNews"></news-list>
     </el-col>
  </el-row>
</template>

<script>
  import {getStrawberryNews,getStrawberryNewsDetail} from 'service/getData'
  import newsList from 'components/newsList/newsList'

  export default {
    name: 'news',
    data () {
      return {
        newList:[],
        news:{}
      }
    },
    mounted(){
      this.$store.commit('HANDLE_NAV',this.$route.path.split('/')[2]);
      this.number = this.$route.params.number;
      this.getStrawberryNews();
      this.getStrawberryNewsDetail();
    },
    components:{
      'news-list':newsList
    },
    methods:{
      async getStrawberryNews(){
        let resp = await getStrawberryNews();
        if(resp.code==0){
            this.newList = resp.data;
        }else if(resp.code==1){
          this.$alert(resp.msg, '提示', {
              confirmButtonText: '确定',
              callback: action => {
              }
          });
        }
      },
      async getStrawberryNewsDetail(){
        let resp = await getStrawberryNewsDetail(this.number);
        if(resp.code==0){
            this.news= resp.data[0];
        }
      },
      changeNews(index){
        this.number = index;
        this.getStrawberryNewsDetail();
      }
    }
  }
</script>
