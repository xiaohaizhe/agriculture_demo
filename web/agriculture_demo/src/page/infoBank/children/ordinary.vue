<template>
  <div>
        <el-row class="mg-top-20 mg-left-20 mg-bot-20">
            <div>
                <div class="ad-flex ad-flexCenter mg-bot-10"><i class="illness ad-icon mg-right-10"></i><span class="font-18">病害</span></div>
                <ul class="ad-flex ad-illness">
                <li class="font-16" v-for="item in illness" :key="item" @click="goDetail(item)">{{item}}</li>
                </ul>
                <div class="ad-flex ad-flexCenter mg-bot-10"><i class="bugs ad-icon mg-right-10"></i><span class="font-18">虫害</span></div>
                <ul class="ad-flex ad-illness">
                <li class="font-16" v-for="item in bugs" :key="item" @click="goDetail(item)">{{item}}</li>
                </ul>
            </div>
            
        </el-row>
  </div>
</template>

<script>
    import {getIllnessData} from 'service/getData'
    export default {
        name: 'ordinary',
        data () {
            return {
                illness:[],
                bugs:[],
            }
        },
        mounted(){
            this.$emit('updateRoute', {})
            this.getIllnessData();
        },
        methods:{
            async getIllnessData(){
                let resp = await getIllnessData('薯类','马铃薯');
                if(resp.code==0){
                    this.illness = resp.data["病害"];
                    this.bugs = resp.data['虫害']
                }
            },
            goDetail(item){
                this.$router.push({name:'illDetail',params:{data:item}});
                this.$emit('updateRoute', {name:'illDetail',params:{data:item}})
            }
        }
    }
</script>