<template>
    <div class="bg-fff">
         <div>
           <el-carousel trigger="click" height="250px">
            <el-carousel-item v-for="item in 3" :key="item">
              <i class="news"></i>
            </el-carousel-item>
          </el-carousel>
          </div>
          <div style="padding:25px">
              <div class="ad-flex ad-flexBtw ad-flexCenter mg-bot-10">
                <div>
                  <i class="el-icon-chat-line-square ad-green font-18"></i>
                  <span class="ad-gray font-18">最新消息</span>
                </div>
                <!-- <el-button type="text" class="ad-lightgray textRight">查看更多></el-button> -->
              </div>
              <ul>
                <li v-for="(news,index) in newList" :key="news._id" class="ad-flex ad-flexBtw mg-bot-20">
                  <span class="ad-gray" style="cursor: pointer;" @click="change(index+1)">{{news.title}}</span>
                  <span class="ad-lightgray">{{news.date}}</span>
                </li>
              </ul>
          </div>
       </div>
</template>

<script>
  export default {
    name: 'newsList',
    data () {
      return {
      }
    },
    props:{
        newList:Array
    },
    methods:{
        //跳转页面
        change(index){
            this.$emit('changeNews',index);
        },
    }
  }
</script>
